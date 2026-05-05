from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pas = request.form.get('password')
    # এখানে আপনি ডাটা সেভ করার কোড রাখতে পারেন
    print(f"User: {user}, Pass: {pas}")
    return "Login Successful! Check Console."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
