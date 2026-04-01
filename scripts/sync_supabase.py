#!/usr/bin/env python3
"""
⚠️ IMPORTANT: This script runs AUTOMATICALLY via GitHub Actions!

DO NOT run this manually unless you're a repository maintainer.

How it works:
1. User uploads JSON file to verification_list/ folder on GitHub
2. User creates Pull Request and waits for merge
3. After merge, GitHub Actions automatically runs this script
4. Script syncs data to Supabase database
5. Certificate becomes available on website

Requirements (set in GitHub Secrets):
- SUPABASE_URL
- SUPABASE_SERVICE_ROLE_KEY
"""
import glob
import json
import os
import requests

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_SERVICE_ROLE_KEY = os.getenv('SUPABASE_SERVICE_ROLE_KEY')

if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
    print("❌ Error: SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY environment variables are required")
    print("\n💡 For maintainers: Set these in GitHub Repository Settings → Secrets → Actions")
    print("\n📋 Steps:")
    print("1. Go to: https://github.com/YOUR_USERNAME/pivalue.world/settings/secrets/actions")
    print("2. Add new secret: SUPABASE_URL")
    print("3. Add new secret: SUPABASE_SERVICE_ROLE_KEY")
    print("\nℹ️  Users don't need to run this - it's automatic after PR merge!")
    raise SystemExit(1)

HEADERS = {
    'Content-Type': 'application/json',
    'apikey': SUPABASE_SERVICE_ROLE_KEY,
    'Authorization': f'Bearer {SUPABASE_SERVICE_ROLE_KEY}',
    'Prefer': 'return=minimal'
}

verification_files = glob.glob('verification_list/*.json')
if not verification_files:
    print('No files found in verification_list/. Nothing to sync.')
    raise SystemExit(0)

verified_count = 0

print(f"\n📊 Found {len(verification_files)} verification file(s) to process...")

for filepath in verification_files:
    print(f"\n📄 Processing: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"  ❌ Error reading file: {e}")
        continue

    # Validate required fields
    if not data.get('submission_id') or not data.get('verification_code'):
        print(f'  ⚠️  Skipping (missing submission_id or verification_code)')
        continue

    # Prepare COMPLETE submission data matching database schema
    submission_payload = {
        'github_username': str(data.get('github_username', '')),
        'verification_code': str(data.get('verification_code', '')),
        'submission_id': str(data.get('submission_id', '')),
        'time_limit': int(data.get('time_limit', 0)),
        'calculations_performed': int(data.get('calculations_performed', 0)),
        'precision_digits': int(data.get('precision_digits', 0)),
        'elapsed_seconds': float(data.get('elapsed_seconds', 0)),
        'result': str(data.get('result', '')),
        'status': 'verified',
        'submitted_at': data.get('timestamp', ''),
        'verified_at': data.get('timestamp', ''),
        'verified_by': 'GitHub Actions (PR merge)'
    }
    
    print(f"  📊 Complete data being synced:")
    print(f"     - All fields from JSON file included")
    print(f"     - Status updated: pending → verified")
    print(f"     - Verified by: GitHub Actions")

    print(f"  📝 Submission ID: {submission_payload['submission_id']}")
    print(f"  👤 Username: {submission_payload['github_username']}")
    print(f"  🎫 Verification Code: {submission_payload['verification_code']}")

    # Step 1: Check if submission already exists (might be pending from script run)
    check_url = f"{SUPABASE_URL}/rest/v1/submissions?submission_id=eq.{submission_payload['submission_id']}"
    check_res = requests.get(check_url, headers=HEADERS)
    
    if check_res.ok and len(check_res.json()) > 0:
        existing_record = check_res.json()[0]
        current_status = existing_record.get('status', 'pending')
        
        if current_status == 'pending':
            print(f"  ✅ Found PENDING record - UPDATING to VERIFIED!")
            # Update from pending to verified
            update_url = f"{SUPABASE_URL}/rest/v1/submissions?submission_id=eq.{submission_payload['submission_id']}"
            update_payload = {
                'status': 'verified',
                'verified_at': submission_payload['verified_at'],
                'verified_by': 'GitHub Actions (PR merge)'
            }
            update_res = requests.patch(update_url, headers=HEADERS, json=update_payload)
            if update_res.ok:
                print(f"  ✅ Successfully updated to VERIFIED!")
            else:
                print(f"  ❌ Error updating: {update_res.status_code} - {update_res.text}")
                continue
        else:
            print(f"  ℹ️  Already {current_status} - skipping")
    else:
        print(f"  ✨ No pending record found - inserting as VERIFIED directly")
        # Insert new record (fallback if no pending was created)
        insert_url = f'{SUPABASE_URL}/rest/v1/submissions'
        insert_res = requests.post(insert_url, headers=HEADERS, json=submission_payload)
        if not insert_res.ok:
            print(f"  ❌ Error inserting: {insert_res.status_code} - {insert_res.text}")
            continue
        else:
            print(f"  ✅ Inserted as verified!")

    # Step 2: Create certificate record
    print(f"  📜 Creating certificate record...")
    cert_payload = {
        'submission_id': submission_payload['submission_id'],
        'certificate_url': f'https://pivalue.iths.online/certificate.html?id={submission_payload["submission_id"]}',
        'certificate_data': submission_payload
    }
    
    # Check if certificate already exists
    cert_check_url = f"{SUPABASE_URL}/rest/v1/certificates?certificate_data->>submission_id=eq.{submission_payload['submission_id']}"
    cert_check_res = requests.get(cert_check_url, headers=HEADERS)
    
    if not cert_check_res.ok or len(cert_check_res.json()) == 0:
        cert_url = f'{SUPABASE_URL}/rest/v1/certificates'
        cert_res = requests.post(cert_url, headers=HEADERS, json=cert_payload)
        if cert_res.ok or cert_res.status_code == 201:
            print(f"  ✅ Certificate created successfully")
        elif cert_res.status_code == 409:
            print(f"  ℹ️  Certificate already exists")
        else:
            print(f"  ⚠️  Certificate creation skipped: {cert_res.status_code}")
    else:
        print(f"  ℹ️  Certificate already exists")

    verified_count += 1
    print(f"  ✅ Successfully processed!")

# Increase counter
if verified_count > 0:
    increment_url = f'{SUPABASE_URL}/rest/v1/counter?id=eq.1'
    current = requests.get(increment_url, headers=HEADERS).json()
    if isinstance(current, list) and len(current) == 0:
        # create a counter row
        response = requests.post(f'{SUPABASE_URL}/rest/v1/counter', headers=HEADERS, json={'id': 1, 'value': 3.14 + 0.01 * verified_count})
        if not response.ok:
            print('Failed to create counter row', response.status_code, response.text)
            raise SystemExit(1)
    else:
        old_value = float(current[0].get('value', 3.14))
        new_value = round(old_value + 0.01 * verified_count, 2)
        response = requests.patch(f'{SUPABASE_URL}/rest/v1/counter?id=eq.1', headers={**HEADERS, 'Prefer': 'return=minimal'}, json={'value': new_value})
        if not response.ok:
            print('Failed to update counter', response.status_code, response.text)
            raise SystemExit(1)

print(f'Successfully verified {verified_count} entries and updated counter.')
