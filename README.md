# 💀 Clickjacking Vulnerability Demo

This is a simple Flask-based project to demonstrate **Clickjacking**, a common web security vulnerability.

## 🔍 What is Clickjacking?

Clickjacking tricks users into clicking something they didn't intend to — often by hiding a sensitive page (like a bank button) inside an invisible iframe.

## 🛠 How It Works

- `bank.html`: A fake bank site with a "Transfer Money" button.
- `evil.html`: A malicious page with a visible "Click Me" button, which overlaps the hidden bank button inside an invisible iframe.

## ▶️ Run the App

1. Install Flask:


2. Start the server:


3. Open `evil.html` in your browser.

## 🧪 Test

When you click the fake button, it actually clicks the bank's invisible button — simulating a **clickjacking attack**.

## 🛡️ Protection

Remove or comment out the `X-Frame-Options` header in `app.py` to allow clickjacking. To **prevent** the attack, keep this line:

```python
response.headers['X-Frame-Options'] = 'DENY'

File structure:

clickjacking-demo/
│
├── app.py
├── evil.html
└── templates/
    └── bank.html
