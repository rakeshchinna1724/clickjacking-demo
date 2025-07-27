from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def bank():
    return render_template('bank.html')

@app.after_request
def add_header(response):
    # ❌ Remove this line to demonstrate vulnerability
    # response.headers['X-Frame-Options'] = 'DENY'  # ✅ Prevent Clickjacking
    return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Required for Render
    app.run(host='0.0.0.0', port=port)
