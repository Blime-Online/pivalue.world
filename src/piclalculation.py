#!/usr/bin/env python3
"""
Pi Value World - Calculation Script
Calculate 22/7 with precision and earn your certificate!
"""

import time
import hashlib
import random
import json
from decimal import Decimal, getcontext
from datetime import datetime

def generate_unique_code():
    """Generate a unique 16-character verification code"""
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(chars) for _ in range(16))

def generate_id():
    """Generate a unique ID"""
    timestamp = str(time.time())
    random_part = str(random.randint(1000, 9999))
    hash_input = timestamp + random_part
    return hashlib.sha256(hash_input.encode()).hexdigest()[:12]

def calculate_pi(time_limit_minutes):
    """
    Calculate 22/7 repeatedly for the specified time
    Returns the number of calculations performed and final result
    """
    # Set high precision
    getcontext().prec = 1000
    
    start_time = time.time()
    end_time = start_time + (time_limit_minutes * 60)
    
    calculations = 0
    last_result = None
    
    print(f"\n🔢 Starting calculation for {time_limit_minutes} minute(s)...")
    print("⏳ Press Ctrl+C to stop early\n")
    
    try:
        while time.time() < end_time:
            # Calculate 22/7 with high precision
            numerator = Decimal(22)
            denominator = Decimal(7)
            last_result = numerator / denominator
            calculations += 1
            
            # Show progress every 1000 calculations
            if calculations % 1000 == 0:
                elapsed = time.time() - start_time
                print(f"⚡ Calculations: {calculations} | Elapsed: {elapsed:.2f}s", end='\r')
        
        # Final calculation for accurate result
        final_result = Decimal(22) / Decimal(7)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Calculation stopped by user")
        final_result = last_result if last_result else Decimal(22) / Decimal(7)
    
    elapsed_time = time.time() - start_time
    
    return calculations, final_result, elapsed_time

def main():
    print("=" * 60)
    print("🥧 Welcome to Pi Value World! 🥧")
    print("=" * 60)
    print("\nCalculate 22/7 and test your PC power!")
    print("Earn a unique certificate for your GitHub profile\n")
    
    # Get GitHub username
    while True:
        github_username = input("Enter your GitHub username: ").strip()
        if github_username:
            break
        print("❌ Username cannot be empty!\n")
    
    # Get time limit selection
    print("\nSelect time limit:")
    print("1. 2 minutes")
    print("2. 5 minutes")
    print("3. 10 minutes")
    
    while True:
        choice = input("\nEnter choice (1/2/3): ").strip()
        if choice == '1':
            time_limit = 2
            break
        elif choice == '2':
            time_limit = 5
            break
        elif choice == '3':
            time_limit = 10
            break
        print("❌ Invalid choice! Please enter 1, 2, or 3")
    
    # Perform calculation
    calculations, result, elapsed_time = calculate_pi(time_limit)
    
    # Generate unique identifiers
    verification_code = generate_unique_code()
    submission_id = generate_id()
    
    # Format the result
    result_str = str(result)
    precision = len(result_str.split('.')[1]) if '.' in result_str else 0
    
    # Display results
    print("\n" + "=" * 60)
    print("🎉 Calculation Complete!")
    print("=" * 60)
    print(f"👤 GitHub Username: {github_username}")
    print(f"⏱️  Time Limit: {time_limit} minute(s)")
    print(f"⚡ Actual Time: {elapsed_time:.2f} seconds")
    print(f"🔢 Total Calculations: {calculations}")
    print(f"📊 Precision Achieved: {precision} decimal places")
    print(f"\n🎫 Your Verification Code: {verification_code}")
    print(f"🆔 Your Submission ID: {submission_id}")
    print(f"\n📝 Result (first 50 digits): {result_str[:52]}...")
    
    # Save results to file
    result_data = {
        "github_username": github_username,
        "time_limit": time_limit,
        "calculations_performed": calculations,
        "elapsed_seconds": elapsed_time,
        "precision_digits": precision,
        "verification_code": verification_code,
        "submission_id": submission_id,
        "result": result_str,
        "timestamp": datetime.now().isoformat()
    }
    
    result_file = f"pi_result_{github_username}.json"
    with open(result_file, 'w') as f:
        json.dump(result_data, f, indent=2)
    
    # Also place in verification_list for auto sync to the website
    import os
    verification_dir = 'verification_list'
    os.makedirs(verification_dir, exist_ok=True)
    verification_path = os.path.join(verification_dir, result_file)
    with open(verification_path, 'w') as f:
        json.dump(result_data, f, indent=2)

    # 🆕 INSERT INTO DATABASE IMMEDIATELY AS PENDING!
    print("\n🔄 Inserting into database as 'pending'...")
    try:
        # Check if .env file exists for Supabase credentials
        env_file = '.env'
        if os.path.exists(env_file):
            from dotenv import load_dotenv
            load_dotenv()
            
            SUPABASE_URL = os.getenv('SUPABASE_URL')
            SUPABASE_SERVICE_ROLE_KEY = os.getenv('SUPABASE_SERVICE_ROLE_KEY')
            
            if SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY:
                import requests
                
                # Insert as pending status with COMPLETE data
                db_payload = {
                    'github_username': str(github_username),
                    'verification_code': str(verification_code),
                    'submission_id': str(submission_id),
                    'time_limit': int(time_limit),
                    'calculations_performed': int(calculations),
                    'precision_digits': int(precision),
                    'elapsed_seconds': float(round(elapsed_time, 2)),
                    'result': str(result_str),
                    'status': 'pending',  # ← PENDING until PR merge!
                    'submitted_at': datetime.now().isoformat(),
                    # Store complete JSON data for reference
                    'verified_by': None,
                    'verified_at': None
                }
                
                print(f"📊 Complete data being inserted:")
                print(f"   - Username: {github_username}")
                print(f"   - Time Limit: {time_limit} min")
                print(f"   - Calculations: {calculations:,}")
                print(f"   - Precision: {precision} digits")
                print(f"   - Elapsed: {elapsed_time:.2f}s")
                print(f"   - Status: pending")
                
                headers = {
                    'Content-Type': 'application/json',
                    'apikey': SUPABASE_SERVICE_ROLE_KEY,
                    'Authorization': f'Bearer {SUPABASE_SERVICE_ROLE_KEY}'
                }
                
                insert_url = f'{SUPABASE_URL}/rest/v1/submissions'
                response = requests.post(insert_url, headers=headers, json=db_payload)
                
                if response.ok:
                    print("✅ Record created in database with status: PENDING")
                    print("   Search will show your submission (but marked as pending)")
                    print("   After PR merge → GitHub Actions will update to VERIFIED")
                else:
                    print(f"⚠️  Could not insert into database: {response.status_code}")
                    print("   No worries - will be inserted after PR merge!")
            else:
                print("⚠️  Supabase credentials not found in .env")
                print("   Record will be created after PR merge via GitHub Actions")
        else:
            print("⚠️  No .env file found - skipping immediate database insert")
            print("   Record will be created after PR merge via GitHub Actions")
    except Exception as e:
        print(f"⚠️  Database insert failed: {e}")
        print("   No worries - GitHub Actions will handle it after PR merge!")

    print(f"\n💾 Results saved to: {result_file}")
    print(f"📂 Verification copy saved to: {verification_path}")
    print("=" * 60)
    print("\n🎯 NEXT STEPS - SUPER SIMPLE!")
    print("=" * 70)
    print("⚠️  IMPORTANT: Your data is NOT in database yet!")
    print("   You MUST upload this file to GitHub first.")
    print("=" * 70)
    print("\n📋 STEP-BY-STEP:")
    print("1. ✅ Result file created in verification_list/ folder")
    print(f"   File: verification_list/pi_result_{github_username}.json")
    print("\n2. 📋 Copy the ENTIRE JSON content shown above")
    print("   (Select all text from { to } and copy)")
    print("\n3. 🌐 Go to YOUR fork on GitHub:")
    print(f"   https://github.com/{github_username}/pivalue.world")
    print("\n4. 📁 Navigate to 'verification_list' folder")
    print("\n5. ➕ Click 'Add file' → 'Create new file'")
    print(f"\n6. 📝 Name it EXACTLY: pi_result_{github_username}.json")
    print("\n7. 📋 PASTE the JSON data into the file editor")
    print("\n8. ✍️  Add commit message: 'Add my submission'")
    print("\n9. ✅ Click 'Commit changes'")
    print("\n10. 🔄 Create Pull Request:")
    print("    - Click 'Pull requests' tab")
    print("    - Click 'New pull request'")
    print("    - Select your branch")
    print("    - Click 'Create pull request'")
    print("\n11. ⏳ Wait for merge (1-3 days)")
    print("\n12. 🎉 AFTER MERGE:")
    print("    - GitHub Actions auto-syncs to database")
    print("    - Search works at: https://pivalue.iths.online/search")
    print("    - Download certificate!")
    print("=" * 70)
    print("\n💡 REMEMBER: Database record is created ONLY after PR merge!")
    print("   Until then, searching won't find your submission.\n")
    
    # Offer to copy code
    copy_choice = input("Would you like to save the code to clipboard? (y/n): ").strip().lower()
    if copy_choice == 'y':
        try:
            import pyperclip
            pyperclip.copy(f"ID: {submission_id}\nCode: {verification_code}")
            print("✅ Code copied to clipboard!")
        except ImportError:
            print("⚠️  pyperclip not installed. Please install with: pip install pyperclip")
            print("📋 Manual copy from the result file instead.\n")
    
    print("\n🌟 Thank you for participating in Pi Value World!")
    print("🔗 Visit our website to see all submissions and certificates\n")

if __name__ == "__main__":
    main()

