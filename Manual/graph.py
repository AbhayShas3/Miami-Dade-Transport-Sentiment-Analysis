import matplotlib.pyplot as plt

sentiment_counts = {
    'Neutral': 26,
    'Negative': 5,
    'Positive': 0
}

# Step 2: Plotting
plt.figure(figsize=(6, 6))
plt.pie(sentiment_counts.values(), labels=sentiment_counts.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Manual Sentiment Distribution of Miami Transit Tweets')
plt.axis('equal')  
plt.tight_layout()
plt.savefig('manual_sentiment_pie_chart.png', dpi=300)
plt.show()