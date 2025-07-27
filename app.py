from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def bank():
    return render_template('bank.html')

@app.after_request
def add_header(response):
    # ❌ Remove this line to demonstrate the vulnerability
    #response.headers['X-Frame-Options'] = 'DENY'  # ✅ Prevent Clickjacking
    return response

if __name__ == '__main__':
    app.run(debug=True)
