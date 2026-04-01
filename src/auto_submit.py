#!/usr/bin/env python3
"""
Pi Value World - Auto-Submit Helper
Automatically commits and pushes your submission to GitHub!
"""

import os
import subprocess
import sys

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
    
    # Check if we're in the right directory
    if not os.path.exists('verification_list'):
        print("❌ Error: Not in the pivalue.world directory!")
        print("Please navigate to your cloned repository first.")
        sys.exit(1)
    
    # Find JSON files in verification_list
    json_files = [f for f in os.listdir('verification_list') if f.startswith('pi_result_') and f.endswith('.json')]
    
    if not json_files:
        print("\n❌ No submission files found in verification_list/")
        print("Please run src/piclalculation.py first to generate your result.")
        sys.exit(1)
    
    print(f"\n📂 Found {len(json_files)} submission file(s):")
    for i, filename in enumerate(json_files, 1):
        print(f"   {i}. {filename}")
    
    # Select the most recent one
    latest_file = max(json_files, key=lambda x: os.path.getmtime(os.path.join('verification_list', x)))
    print(f"\n✅ Using most recent: {latest_file}")
    
    # Read the file to get username
    import json
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
        print("\n⚠️  You can push manually with: git push")
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
    print("\n4. Include details from your JSON file in the description")
    print("5. Wait for merge (1-3 days)")
    print("\n✨ After merge:")
    print("   • Website auto-verifies your submission")
    print("   • Pi counter increases by +0.01")
    print("   • Certificate ready at: https://pivalue.iths.online/search")
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
    
    print("\n🌟 Thank you for participating in Pi Value World!\n")

if __name__ == "__main__":
    main()
