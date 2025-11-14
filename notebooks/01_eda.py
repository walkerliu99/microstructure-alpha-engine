import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/82427/OneDrive/Desktop/microstructure-alpha-engine/data/btc_1min_coinbase.csv")

df.head()

df['close'].plot(figsize=(15,5), title="BTC-USD (1m Closing Price)")
plt.show()
