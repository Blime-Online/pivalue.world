#!/usr/bin/env python3
"""
Quick Fix Script - Adds files to your empty submission branch
Run this AFTER auto_submit.py created an empty branch
"""

import os
import subprocess
import sys
import json

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout + result.stderr
    except Exception as e:
        return False, str(e)

print("=" * 60)
print("🔧 Fixing Empty Submission Branch")
print("=" * 60)

# Find JSON files
json_files = []
if os.path.exists('verification_list'):
    json_files = [f for f in os.listdir('verification_list') 
                  if f.startswith('pi_result_') and f.endswith('.json')]

if not json_files:
    print("\n❌ No submission files found in verification_list/")
    print("\n💡 You need to run calculation FIRST:")
    print("   python src/piclalculation.py")
    sys.exit(1)

print(f"\n✅ Found {len(json_files)} file(s):")
for f in json_files:
    print(f"   📄 {f}")

# Get current branch
success, current_branch = run_command("git rev-parse --abbrev-ref HEAD")
current_branch = current_branch.strip()

print(f"\n📍 Current branch: {current_branch}")

if not current_branch.startswith('submission/'):
    print("\n⚠️  You're not on a submission branch!")
    print("Auto-submit should have created one.")
    print("\nAvailable branches:")
    success, branches = run_command("git branch")
    print(branches)
    print("\n💡 Try running auto-submit again:")
    print("   python auto_submit.py")
    sys.exit(1)

# Add files
print(f"\n📝 Adding files to git...")
success, output = run_command("git add -A verification_list/")
if not success:
    print(f"❌ Failed: {output}")
    sys.exit(1)

# Check if anything was staged
success, staged = run_command("git diff --cached --name-only")
if not staged.strip():
    print("\n⚠️  No new files to commit!")
    print("Files may already be committed or don't exist.")
    sys.exit(1)

print("✅ Files staged successfully!")

# Read username from first file
with open(os.path.join('verification_list', json_files[0]), 'r') as f:
    data = json.load(f)
    username = data.get('github_username', 'unknown')

# Commit
print(f"\n💾 Committing changes...")
commit_msg = f"feat: add Pi Value World submission for {username}"
success, output = run_command(f'git commit -m "{commit_msg}"')
if not success:
    if "nothing to commit" in output:
        print("⚠️  Nothing to commit (already committed)")
    else:
        print(f"❌ Failed: {output}")
        sys.exit(1)
else:
    print("✅ Committed successfully!")

# Push
print(f"\n🚀 Pushing to GitHub...")
success, output = run_command(f"git push -u origin {current_branch}")
if not success:
    print(f"❌ Failed: {output}")
    print(f"\n⚠️  Try manually: git push -u origin {current_branch}")
else:
    print("✅ Pushed successfully!")

print("\n" + "=" * 60)
print("🎉 SUCCESS! Your branch now has files!")
print("=" * 60)
print(f"\n📋 NEXT: Create Pull Request")
print(f"1. Go to: https://github.com/harinandsindukumar/pivalue.world")
print(f"2. Click 'Pull requests' → 'New pull request'")
print(f"3. Select: base: main ← compare: {current_branch}")
print(f"4. Title: feat: add submission for {username}")
print(f"5. Include your Submission ID + Verification Code")
print("\n✨ GitHub should now show your files!")
print("=" * 60)
