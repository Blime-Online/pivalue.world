#!/usr/bin/env python3
"""
Complete Submission - Creates branch, adds files, commits, and pushes
Run this ONCE to do everything automatically
"""

import os
import subprocess
import sys
import json
import time

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout + result.stderr
    except Exception as e:
        return False, str(e)

print("=" * 60)
print("🥧 Pi Value World - Complete Submission")
print("=" * 60)

# Find JSON files
json_files = [f for f in os.listdir('verification_list') 
              if f.startswith('pi_result_') and f.endswith('.json')]

if not json_files:
    print("\n❌ No submission files found!")
    print("Run: python src/piclalculation.py")
    sys.exit(1)

print(f"\n✅ Found {len(json_files)} file(s)")

# Read username
with open(os.path.join('verification_list', json_files[0]), 'r') as f:
    data = json.load(f)
    username = data.get('github_username', 'unknown')

print(f"👤 Username: @{username}")

# Create branch name
branch_name = f"submission/{username}-{int(time.time())}"

# Step 1: Create branch
print(f"\n🌿 Step 1/4: Creating branch: {branch_name}...")
success, output = run_command(f'git checkout -b {branch_name}')
if not success:
    print(f"❌ Failed: {output}")
    sys.exit(1)
print(f"✅ Created branch: {branch_name}")

# Step 2: Add files
print("\n📝 Step 2/4: Adding files...")
success, output = run_command("git add -A verification_list/")
if not success:
    print(f"❌ Failed: {output}")
    sys.exit(1)

# Verify files staged
success, staged = run_command("git diff --cached --name-only")
if not staged.strip():
    print("\n⚠️  No files to add!")
    print("Maybe already committed?")
    sys.exit(1)

print(f"✅ Added {len(staged.strip().split())} file(s)")

# Step 3: Commit
print("\n💾 Step 3/4: Committing...")
commit_msg = f"feat: add Pi Value World submission for {username}"
success, output = run_command(f'git commit -m "{commit_msg}"')
if not success:
    print(f"❌ Failed: {output}")
    sys.exit(1)
print("✅ Committed successfully!")

# Step 4: Push
print("\n🚀 Step 4/4: Pushing to GitHub...")
success, output = run_command(f'git push -u origin {branch_name}')
if not success:
    print(f"❌ Failed: {output}")
    print(f"\nManual fix: git push -u origin {branch_name}")
    sys.exit(1)
print("✅ Pushed successfully!")

print("\n" + "=" * 60)
print("🎉 SUCCESS!")
print("=" * 60)
print(f"\n✨ Your branch is ready: {branch_name}")
print("\n📋 Create Pull Request:")
print("1. GitHub will show link automatically")
print("2. Or go to: https://github.com/harinandsindukumar/pivalue.world")
print("3. Click 'Pull requests' → 'New pull request'")
print(f"4. Select: base: main ← compare: {branch_name}")
print(f"5. Title: feat: add submission for {username}")
print("\n💡 Include your codes from the JSON file!")
print("=" * 60)
