#!/usr/bin/env python3
"""
Pi Value World - Certificate Generator
Generates beautiful certificates with user details and Pi Value World logo
"""

from PIL import Image, ImageDraw, ImageFont
import json
import os
from datetime import datetime

def create_certificate(username, time_limit, calculations, precision, 
                      verification_code, submission_id, verified_date=None):
    """
    Generate a certificate image with all user details and Pi Value World logo
    
    Parameters:
    - username: GitHub username
    - time_limit: Time limit chosen (2, 5, or 10 minutes)
    - calculations: Number of calculations performed
    - precision: Precision digits achieved
    - verification_code: 16-character verification code
    - submission_id: 12-character submission ID
    - verified_date: Date of verification
    """
    
    print("🎨 Generating your Pi Value World Certificate...")
    
    # Create certificate base (A4 size at 300 DPI: 2480x3508)
    width, height = 2480, 3508
    cert = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(cert)
    
    # Load logo if available
    logo_path = "website/assets/pi.png"
    if not os.path.exists(logo_path):
        logo_path = "pi.png"
    
    try:
        logo = Image.open(logo_path)
        logo = logo.resize((300, 300), Image.Resampling.LANCZOS)
        logo_position = ((width - logo.width) // 2, 150)
        cert.paste(logo, logo_position, logo if logo.mode == 'RGBA' else None)
        print(f"✅ Logo added from {logo_path}")
    except Exception as e:
        print(f"⚠️  Could not load logo: {e}")
        # Draw placeholder circle instead
        draw.ellipse([(width-300)//2, 150, (width+300)//2, 450], 
                    fill='#FFD700', outline='#000000', width=10)
        draw.text((width//2, 300), "π", fill='black', 
                 font=ImageFont.truetype("arial.ttf", 200), anchor="mm")
    
    # Draw decorative border
    border_margin = 60
    draw.rectangle([border_margin, border_margin, width-border_margin, height-border_margin], 
                  outline='#FFD700', width=15)
    draw.rectangle([border_margin+20, border_margin+20, width-border_margin-20, height-border_margin-20], 
                  outline='#000000', width=3)
    
    # Title
    title_text = "Certificate of Achievement"
    title_font = ImageFont.truetype("arial.ttf", 80)
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font, anchor="mt")
    title_width = title_bbox[2] - title_bbox[0]
    draw.text((width//2, 550), title_text, fill='black', font=title_font, anchor="mt")
    
    # Subtitle
    subtitle_text = "Pi Value World Challenge"
    subtitle_font = ImageFont.truetype("arial.ttf", 40)
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font, anchor="mt")
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    draw.text((width//2, 660), subtitle_text, fill='#666666', font=subtitle_font, anchor="mt")
    
    # Presented to text
    presented_text = "This is to certify that"
    presented_font = ImageFont.truetype("arial.ttf", 35)
    draw.text((width//2, 800), presented_text, fill='black', font=presented_font, anchor="mt")
    
    # Username (prominent)
    username_text = f"@{username}"
    username_font = ImageFont.truetype("arial.ttf", 90)
    username_bbox = draw.textbbox((0, 0), username_text, font=username_font, anchor="mt")
    username_width = username_bbox[2] - username_bbox[0]
    draw.text((width//2, 900), username_text, fill='#FFD700', font=username_font, anchor="mt", stroke_fill='black', stroke_width=2)
    
    # Achievement text
    achieve_text = "has successfully completed the Pi Value World Challenge"
    achieve_font = ImageFont.truetype("arial.ttf", 35)
    draw.text((width//2, 1050), achieve_text, fill='black', font=achieve_font, anchor="mt")
    
    # Statistics boxes
    box_y = 1200
    box_height = 350
    box_width = 600
    spacing = 80
    
    # Box 1: Time Limit
    box1_x = (width - (3 * box_width + 2 * spacing)) // 2
    draw_rectangle_rounded(draw, [box1_x, box_y, box1_x + box_width, box_y + box_height], 
                          radius=30, fill='#FFFACD', outline='#FFD700', width=5)
    
    time_label = "Time Limit"
    time_value = f"{time_limit} minute(s)"
    draw.text((box1_x + box_width//2, box_y + 100), time_label, fill='black', 
             font=ImageFont.truetype("arial.ttf", 30), anchor="mm")
    draw.text((box1_x + box_width//2, box_y + 200), time_value, fill='black', 
             font=ImageFont.truetype("arial.ttf", 50, bold=True), anchor="mm")
    
    # Box 2: Calculations
    box2_x = box1_x + box_width + spacing
    draw_rectangle_rounded(draw, [box2_x, box_y, box2_x + box_width, box_y + box_height], 
                          radius=30, fill='#FFFACD', outline='#FFD700', width=5)
    
    calc_label = "Calculations"
    calc_value = f"{calculations:,}"
    draw.text((box2_x + box_width//2, box_y + 100), calc_label, fill='black', 
             font=ImageFont.truetype("arial.ttf", 30), anchor="mm")
    draw.text((box2_x + box_width//2, box_y + 200), calc_value, fill='black', 
             font=ImageFont.truetype("arial.ttf", 50, bold=True), anchor="mm")
    
    # Box 3: Precision
    box3_x = box2_x + box_width + spacing
    draw_rectangle_rounded(draw, [box3_x, box_y, box3_x + box_width, box_y + box_height], 
                          radius=30, fill='#FFFACD', outline='#FFD700', width=5)
    
    prec_label = "Precision"
    prec_value = f"{precision} digits"
    draw.text((box3_x + box_width//2, box_y + 100), prec_label, fill='black', 
             font=ImageFont.truetype("arial.ttf", 30), anchor="mm")
    draw.text((box3_x + box_width//2, box_y + 200), prec_value, fill='black', 
             font=ImageFont.truetype("arial.ttf", 50, bold=True), anchor="mm")
    
    # Verification details
    details_y = box_y + box_height + 150
    
    verify_text = "Verification Details"
    verify_font = ImageFont.truetype("arial.ttf", 40)
    draw.text((width//2, details_y), verify_text, fill='black', font=verify_font, anchor="mt")
    
    # Verification Code
    code_text = f"Verification Code: {verification_code}"
    code_font = ImageFont.truetype("courbd.ttf", 35)
    draw.text((width//2, details_y + 100), code_text, fill='black', font=code_font, anchor="mt")
    
    # Submission ID
    id_text = f"Submission ID: {submission_id}"
    id_font = ImageFont.truetype("courbd.ttf", 35)
    draw.text((width//2, details_y + 180), id_text, fill='black', font=id_font, anchor="mt")
    
    # Date
    if verified_date:
        date_str = verified_date.strftime("%B %d, %Y")
    else:
        date_str = datetime.now().strftime("%B %d, %Y")
    
    date_text = f"Verified on: {date_str}"
    date_font = ImageFont.truetype("arial.ttf", 35)
    draw.text((width//2, details_y + 280), date_text, fill='black', font=date_font, anchor="mt")
    
    # Footer with Pi Value World branding
    footer_y = height - 200
    footer_text = "Pi Value World | https://pivalue.iths.online"
    footer_font = ImageFont.truetype("arial.ttf", 30)
    draw.text((width//2, footer_y), footer_text, fill='#666666', font=footer_font, anchor="mm")
    
    # Signature line
    sig_line_y = footer_y - 100
    draw.line([(width//2 - 300, sig_line_y), (width//2 + 300, sig_line_y)], fill='black', width=3)
    sig_text = "Authorized by Pi Value World Team"
    sig_font = ImageFont.truetype("ariali.ttf", 28)
    draw.text((width//2, sig_line_y - 20), sig_text, fill='black', font=sig_font, anchor="mb")
    
    # Save certificate
    filename = f"certificate_{username}_{submission_id}.png"
    cert.save(filename, "PNG", quality=95)
    
    print(f"\n{'='*60}")
    print(f"🎉 Certificate Generated Successfully!")
    print(f"{'='*60}")
    print(f"👤 Username: @{username}")
    print(f"⏱️  Time Limit: {time_limit} minute(s)")
    print(f"🔢 Calculations: {calculations:,}")
    print(f"📊 Precision: {precision} digits")
    print(f"🎫 Verification Code: {verification_code}")
    print(f"🆔 Submission ID: {submission_id}")
    print(f"💾 Saved to: {filename}")
    print(f"{'='*60}\n")
    
    return filename

def draw_rectangle_rounded(draw, coords, radius=0, **kwargs):
    """Draw a rounded rectangle"""
    x1, y1, x2, y2 = coords
    draw.rectangle(coords, **kwargs)
    # For simplicity, just draw regular rectangle
    # Can be enhanced with proper rounded corners

def load_from_json(json_file):
    """Load calculation results from JSON file"""
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    return create_certificate(
        username=data['github_username'],
        time_limit=data['time_limit'],
        calculations=data['calculations_performed'],
        precision=data['precision_digits'],
        verification_code=data['verification_code'],
        submission_id=data['submission_id'],
        verified_date=datetime.now()
    )

def main():
    print("="*60)
    print("🥧 Pi Value World - Certificate Generator 🥧")
    print("="*60)
    print("\nThis tool generates certificates from your calculation results.\n")
    
    # Look for result files
    result_files = [f for f in os.listdir('.') if f.startswith('pi_result_') and f.endswith('.json')]
    
    if not result_files:
        print("❌ No result files found!")
        print("Please run piclalculation.py first to generate results.\n")
        
        # Manual entry option
        print("Or enter details manually:\n")
        username = input("Enter GitHub username: ").strip()
        time_limit = int(input("Enter time limit (2/5/10): ").strip())
        calculations = int(input("Enter calculations performed: ").strip())
        precision = int(input("Enter precision digits: ").strip())
        verification_code = input("Enter verification code: ").strip()
        submission_id = input("Enter submission ID: ").strip()
        
        create_certificate(
            username=username,
            time_limit=time_limit,
            calculations=calculations,
            precision=precision,
            verification_code=verification_code,
            submission_id=submission_id
        )
    else:
        print(f"✅ Found {len(result_files)} result file(s):\n")
        for i, file in enumerate(result_files, 1):
            print(f"{i}. {file}")
        
        choice = int(input(f"\nSelect file number (1-{len(result_files)}): ").strip())
        selected_file = result_files[choice - 1]
        
        # Generate certificate
        load_from_json(selected_file)
    
    print("\n✨ Your certificate is ready! You can now download and share it.")
    print("🌐 Upload it to the website or share on your GitHub profile!\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Certificate generation cancelled.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure you have Pillow installed:")
        print("pip install Pillow\n")
