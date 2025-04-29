import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('miami_transit_tweets_with_sentiment.csv')

def plot_sentiment_bar_chart(dataframe):
    sentiment_counts = dataframe['Sentiment_Label'].value_counts()
    plt.figure(figsize=(8, 6))
    sentiment_counts.plot(kind='bar', color=['green', 'blue', 'red'])
    plt.title('Sentiment Analysis of Miami Transit Tweets')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Tweets')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('sentiment_bar_chart.png')  
    # plt.show()

def plot_sentiment_pie_chart(dataframe):
    sentiment_counts = dataframe['Sentiment_Label'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Sentiment Distribution of Miami Transit Tweets')
    plt.axis('equal')  
    plt.tight_layout()
    plt.savefig('sentiment_pie_chart.png') 
    # plt.show()

if __name__ == "__main__":
    plot_sentiment_bar_chart(df)
    plot_sentiment_pie_chart(df)
