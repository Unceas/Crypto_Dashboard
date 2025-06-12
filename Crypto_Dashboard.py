import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# 1. Fetch Crypto Market Data
# ----------------------------
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 20,  # Increase number of coins
    'page': 1,
    'sparkline': 'false'
}

response = requests.get(url, params=params)
data = response.json()

# ----------------------------
# 2. Create DataFrame
# ----------------------------
df = pd.DataFrame(data)
df = df[['id', 'symbol', 'current_price', 'market_cap', 'price_change_percentage_24h']]

# ----------------------------
# 3. Horizontal Bar Chart (Log Scale)
# ----------------------------
sns.set(style="whitegrid")
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.barplot(y='id', x='current_price', data=df, palette='mako')
plt.xscale('log')  # Apply log scale for visibility
plt.xlabel('Current Price (USD, log scale)')
plt.ylabel('Cryptocurrency')
plt.title('Top Cryptos - Price Comparison')

# ----------------------------
# 4. Pie Chart (Market Cap Share)
# ----------------------------
plt.subplot(1, 2, 2)
top5 = df.head(5)
plt.pie(top5['market_cap'], labels=top5['symbol'], autopct='%1.1f%%', startangle=140)
plt.title('Market Cap Share (Top 5)')

plt.tight_layout()
plt.show()

# ----------------------------
# 5. Print Data Table
# ----------------------------
print("\n📊 Top Crypto Stats:\n")
print(df.to_string(index=False))
