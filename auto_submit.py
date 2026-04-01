#!/usr/bin/env python3
"""
Pi Value World - Auto-Submit Helper (ROOT VERSION with Branch Support)
Run this from anywhere! Automatically finds your repository.
Creates a new branch for your submission automatically!
"""

import os
import subprocess
import sys
import json
import time

def find_repo_root():
    """Find the pivalue.world repository root directory"""
    current = os.path.abspath(os.getcwd())
    
    if os.path.exists(os.path.join(current, 'verification_list')):
        return current
    
    while current != os.path.dirname(current):
        if os.path.exists(os.path.join(current, 'verification_list')):
            return current
        current = os.path.dirname(current)
    
    return None

def run_command(command):
    """Run a shell command and return output"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout + result.stderr
    except Exception as e:
        return False, str(e)

def main():
    print("=" * 60)
    print("🥧 Pi Value World - Auto-Submit Helper")
    print("=" * 60)
    
    repo_root = find_repo_root()
    
    if not repo_root:
        print("\n❌ Error: Could not find pivalue.world repository!")
        print("\n💡 SOLUTION:")
        print("   Make sure you've cloned the repository first.")
        print("\n   Steps:")
        print("   1. Fork: https://github.com/harinandsindukumar/pivalue.world")
        print("   2. Clone your fork:")
        print("      git clone https://github.com/YOUR_USERNAME/pivalue.world.git")
        print("   3. Navigate to folder:")
        print("      cd pivalue.world")
        print("   4. Run calculation first:")
        print("      python src/piclalculation.py")
        print("   5. Then run this script:")
        print("      python auto_submit.py")
        sys.exit(1)
    
    os.chdir(repo_root)
    print(f"\n✅ Found repository at: {repo_root}")
    
    json_files = [f for f in os.listdir('verification_list') 
                  if f.startswith('pi_result_') and f.endswith('.json')]
    
    if not json_files:
        print("\n❌ No submission files found in verification_list/")
        print("\n💡 You need to run the calculation script first:")
        print("   python src/piclalculation.py")
        sys.exit(1)
    
    print(f"\n📂 Found {len(json_files)} submission file(s):")
    for i, filename in enumerate(json_files, 1):
        print(f"   {i}. {filename}")
    
    latest_file = max(json_files, key=lambda x: os.path.getmtime(os.path.join('verification_list', x)))
    print(f"\n✅ Using most recent: {latest_file}")
    
    with open(os.path.join('verification_list', latest_file), 'r') as f:
        data = json.load(f)
        username = data.get('github_username', 'unknown')
    
    print(f"👤 GitHub Username: @{username}")
    
    # Create branch name
    branch_name = f"submission/{username}-{int(time.time())}"
    
    print("\n🎯 This will:")
    print(f"   1. Create new branch: {branch_name}")
    print("   2. Add verification_list/ to git")
    print("   3. Commit with your submission")
    print("   4. Push to your forked repository")
    print("\n   Then you'll need to create a Pull Request on GitHub!")
    
    choice = input("\nContinue? (y/n): ").strip().lower()
    if choice != 'y':
        print("❌ Cancelled by user")
        sys.exit(0)
    
    # Step 0: Create new branch
    print(f"\n🌿 Step 0/4: Creating new branch: {branch_name}...")
    success, output = run_command(f'git checkout -b {branch_name}')
    if not success:
        if "already exists" in output.lower():
            print(f"⚠️  Branch {branch_name} already exists, using it")
        else:
            print(f"❌ Failed to create branch: {output}")
            sys.exit(1)
    else:
        print(f"✅ Created branch: {branch_name}")
    
    # Step 1: Git add
    print("\n📝 Step 1/4: Adding files to git...")
    success, output = run_command("git add verification_list/")
    if not success:
        print(f"❌ Failed to add files: {output}")
        sys.exit(1)
    print("✅ Files added successfully!")
    
    # Step 2: Git commit
    print("\n💾 Step 2/4: Committing changes...")
    commit_msg = f"feat: add Pi Value World submission for {username}"
    success, output = run_command(f'git commit -m "{commit_msg}"')
    if not success:
        if "nothing to commit" in output:
            print("⚠️  No changes to commit (already committed)")
        else:
            print(f"❌ Failed to commit: {output}")
            sys.exit(1)
    else:
        print("✅ Committed successfully!")
    
    # Step 3: Git push
    print(f"\n🚀 Step 3/4: Pushing to GitHub ({branch_name})...")
    success, output = run_command(f'git push -u origin {branch_name}')
    if not success:
        print(f"❌ Failed to push: {output}")
        print("\n⚠️  You can push manually with:")
        print(f"   git push -u origin {branch_name}")
    else:
        print("✅ Pushed successfully!")
    
    # Final instructions
    print("\n" + "=" * 60)
    print("🎉 SUCCESS! Your submission is on GitHub!")
    print("=" * 60)
    print("\n📋 NEXT STEP: Create Pull Request")
    print(f"\n✨ Good news! Git usually shows a link automatically.")
    print(f"   Look for this message in your terminal:")
    print(f"   👉 'Create a pull request for {branch_name}'")
    print(f"\nIf not shown, go to:")
    print("1. https://github.com/harinandsindukumar/pivalue.world")
    print("2. Click 'Pull requests' → 'New pull request'")
    print("3. Select your branch:")
    print(f"   base: main ← compare: {branch_name}")
    print("4. Use this title:")
    print(f"   feat: add submission for {username}")
    print("\n5. Include details from your JSON file in the description:")
    print(f"   - GitHub Username: @{username}")
    print(f"   - Submission ID: {data.get('submission_id', 'N/A')}")
    print(f"   - Verification Code: {data.get('verification_code', 'N/A')}")
    print("\n6. Wait for merge (1-3 days)")
    print("\n✨ After merge:")
    print("   • Website auto-verifies your submission")
    print("   • Status: Not Verified → ✅ VERIFIED")
    print("   • Pi counter increases: 3.14 → 3.15 (+0.01)")
    print("   • Certificate ready: https://pivalue.iths.online/search")
    print("=" * 60)
    
    # Offer to open GitHub
    open_choice = input("\n🌐 Open GitHub to create PR now? (y/n): ").strip().lower()
    if open_choice == 'y':
        try:
            import webbrowser
            webbrowser.open("https://github.com/harinandsindukumar/pivalue.world")
            print("✅ GitHub opened in your browser!")
        except:
            print("⚠️  Could not open browser. Please go to GitHub manually.")
    
    print("\n🌟 Thank you for participating in Pi Value World!")
    print("💡 Tip: Each merged PR increases the Pi value on website by 0.01!\n")

if __name__ == "__main__":
    main()
