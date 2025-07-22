import requests

def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return float(data['bitcoin']['usd'])
    else:
        print("❌ Failed to fetch price. Status Code:", response.status_code)
        return None

threshold = 60000

price = get_bitcoin_price()
if price:
    print(f"✅ Current Bitcoin Price: ${price}")
    if price > threshold:
        print(f"🚨 ALERT: Bitcoin is above ${threshold}!")
    else:
        print("ℹ️ Price is below threshold. No alert.")
else:
    print("⚠️ Could not retrieve Bitcoin price.")
