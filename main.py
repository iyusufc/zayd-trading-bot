from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    return requests.post(url, data=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    alert_msg = data.get('message', '🚨 New Trading Alert!')
    send_telegram(f"📈 TradingView Alert: {alert_msg}")
    return {'status': 'ok'}

@app.route('/')
def home():
    return 'Zayd Trading Bot is Live!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
