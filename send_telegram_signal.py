import requests

BOT_TOKEN = "7970786658:AAEsc2pTqZBnVvxjMh3oAWarEhdOFIfDPW4"
CHAT_ID = "-1002813054305"  # Group Chat ID

entry_price = 117800
stop_loss = 116000
take_profit = 120500

message = f"""
🚨 *Crypto Signal Alert!*

*Pair:* BTC/USD  
*Direction:* BUY 🟢  
*Entry:* ${entry_price}  
*Stop Loss:* ${stop_loss} ❌  
*Take Profit:* ${take_profit} 🎯  
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": message,
    "parse_mode": "Markdown"
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print("✅ Signal sent with SL and TP!")
else:
    print("❌ Failed to send signal.")
    print(response.text)
