#!/usr/bin/env python3
"""
Pi Value World - Auto-Submit Helper (ROOT VERSION)
Run this from anywhere! Automatically finds your repository.
"""

import os
import subprocess
import sys
import json

def find_repo_root():
    """Find the pivalue.world repository root directory"""
    # Start from current directory
    current = os.path.abspath(os.getcwd())
    
    # Check if we're already in repo root
    if os.path.exists(os.path.join(current, 'verification_list')):
        return current
    
    # Walk up directories to find repo
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
    
    # Find repository root
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
    
    # Change to repo directory
    os.chdir(repo_root)
    print(f"\n✅ Found repository at: {repo_root}")
    
    # Find JSON files in verification_list
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
    
    # Select the most recent one
    latest_file = max(json_files, key=lambda x: os.path.getmtime(os.path.join('verification_list', x)))
    print(f"\n✅ Using most recent: {latest_file}")
    
    # Read the file to get username
    with open(os.path.join('verification_list', latest_file), 'r') as f:
        data = json.load(f)
        username = data.get('github_username', 'unknown')
    
    print(f"👤 GitHub Username: @{username}")
    
    # Ask for confirmation
    print("\n🎯 This will:")
    print("   1. Add verification_list/ to git")
    print("   2. Commit with your submission")
    print("   3. Push to your forked repository")
    print("\n   Then you'll need to create a Pull Request on GitHub!")
    
    choice = input("\nContinue? (y/n): ").strip().lower()
    if choice != 'y':
        print("❌ Cancelled by user")
        sys.exit(0)
    
    # Step 1: Git add
    print("\n📝 Step 1/3: Adding files to git...")
    success, output = run_command("git add verification_list/")
    if not success:
        print(f"❌ Failed to add files: {output}")
        sys.exit(1)
    print("✅ Files added successfully!")
    
    # Step 2: Git commit
    print("\n💾 Step 2/3: Committing changes...")
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
    print("\n🚀 Step 3/3: Pushing to GitHub...")
    success, output = run_command("git push")
    if not success:
        print(f"❌ Failed to push: {output}")
        print("\n⚠️  You can push manually with:")
        print("   git push")
    else:
        print("✅ Pushed successfully!")
    
    # Final instructions
    print("\n" + "=" * 60)
    print("🎉 SUCCESS! Your submission is on GitHub!")
    print("=" * 60)
    print("\n📋 NEXT STEP: Create Pull Request")
    print("\n1. Go to: https://github.com/harinandsindukumar/pivalue.world")
    print("2. Click 'Contribute' → 'Open Pull Request'")
    print("3. Use this title:")
    print(f"   feat: add submission for {username}")
    print("\n4. Include details from your JSON file in the description:")
    print(f"   - GitHub Username: @{username}")
    print(f"   - Submission ID: {data.get('submission_id', 'N/A')}")
    print(f"   - Verification Code: {data.get('verification_code', 'N/A')}")
    print("\n5. Wait for merge (1-3 days)")
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
