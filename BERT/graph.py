import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/abhayshastry/Desktop/Miami Dade Sentiment Analysis/miami_transit_tweets_with_bert.csv')

def plot_bert_bar_chart(dataframe):
    sentiment_counts = dataframe['BERT_Label'].value_counts()
    plt.figure(figsize=(8, 6))
    sentiment_counts.plot(kind='bar', color=['orange', 'purple'])
    plt.title('BERT Sentiment Analysis of Miami Transit Tweets')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Tweets')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('bert_sentiment_bar_chart.png', dpi=300)
    # plt.show()

def plot_bert_pie_chart(dataframe):
    sentiment_counts = dataframe['BERT_Label'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('BERT Sentiment Distribution of Miami Transit Tweets')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('bert_sentiment_pie_chart.png', dpi=300)
    # plt.show()

plot_bert_bar_chart(df)
plot_bert_pie_chart(df)
