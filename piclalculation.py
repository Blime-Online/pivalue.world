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
    
    print(f"\n💾 Results saved to: {result_file}")
    
    # Copy instructions
    print("\n" + "=" * 60)
    print("📋 Next Steps:")
    print("=" * 60)
    print("1. Copy your Verification Code and Submission ID")
    print("2. Go to the verification page in the repository")
    print("3. Submit your code for verification")
    print("4. Wait for approval and receive your certificate!\n")
    
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
