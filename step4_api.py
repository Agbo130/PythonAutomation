import requests

# ✅ Working public API (no 403 error, returns JSON)
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

response = requests.get(url)
print("Status Code:", response.status_code)

try:
    data = response.json()
    print("✅ Bitcoin Price in USD:", data["bitcoin"]["usd"])
except Exception as e:
    print("❌ Failed to parse JSON:", e)
