import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Date': ['2023-03-09', '2023-02-09', '2023-10-01', '2023-04-01'],
    'Mentions': [156, 180, 120, 200],
    'Engagement': [80, 90, 70, 100],
    'Sentiment': [0.7, 0.6, 0.8, 0.5]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plotting trends over time
plt.figure(figsize=(10, 6))

# Mentions over time
plt.subplot(3, 1, 1)
plt.plot(df['Date'], df['Mentions'], marker='o')
plt.title('Mentions Over Time')
plt.xlabel('Date')
plt.ylabel('Mentions')

# Engagement over time
plt.subplot(3, 1, 2)
plt.plot(df['Date'], df['Engagement'], marker='o', color='orange')
plt.title('Engagement Over Time')
plt.xlabel('Date')
plt.ylabel('Engagement')

# Sentiment over time
plt.subplot(3, 1, 3)
plt.plot(df['Date'], df['Sentiment'], marker='o', color='green')
plt.title('Sentiment Over Time')
plt.xlabel('Date')
plt.ylabel('Sentiment')

plt.tight_layout()
plt.show()
