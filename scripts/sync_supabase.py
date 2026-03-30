#!/usr/bin/env python3
import glob
import json
import os
import requests

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_SERVICE_ROLE_KEY = os.getenv('SUPABASE_SERVICE_ROLE_KEY')

if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
    raise SystemExit('SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY environment variables are required')

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

for filepath in verification_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not data.get('submission_id') or not data.get('verification_code'):
        print(f'Skipping {filepath} (missing submission_id or verification_code)')
        continue

    # Upsert submission
    payload = {
        'github_username': data.get('github_username'),
        'time_limit': data.get('time_limit'),
        'calculations_performed': data.get('calculations_performed'),
        'precision_digits': data.get('precision_digits'),
        'verification_code': data.get('verification_code'),
        'submission_id': data.get('submission_id'),
        'result': data.get('result'),
        'elapsed_seconds': data.get('elapsed_seconds'),
        'submitted_at': data.get('timestamp'),
        'status': 'verified',
        'verified_at': data.get('timestamp')
    }

    upsert_url = f'{SUPABASE_URL}/rest/v1/submissions'
    res = requests.post(upsert_url, headers={**HEADERS, 'Prefer': 'resolution=merge-duplicates'}, json=payload)
    if not res.ok:
        print(f'Error upserting {filepath}:', res.status_code, res.text)
        continue

    # Create certificate record
    cert_payload = {
        'submission_id': data.get('submission_id'),
        'certificate_url': f'https://pivalue.iths.online/certificate.html?id={data.get("submission_id")}',
        'certificate_data': payload
    }
    cert_url = f'{SUPABASE_URL}/rest/v1/certificates'
    res_cert = requests.post(cert_url, headers=HEADERS, json=cert_payload)
    if not res_cert.ok and res_cert.status_code != 409:
        print(f'Error creating certificate for {filepath}:', res_cert.status_code, res_cert.text)
        continue

    verified_count += 1

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