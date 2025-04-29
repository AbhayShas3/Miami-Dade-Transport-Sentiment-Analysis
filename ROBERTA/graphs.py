
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('miami_transit_tweets_with_roberta.csv')

label_mapping = {
    "LABEL_0": "Negative",
    "LABEL_1": "Neutral",
    "LABEL_2": "Positive"
}

df['Roberta_Label_Mapped'] = df['Roberta_Label'].map(label_mapping)

def plot_roberta_bar_chart(dataframe):
    sentiment_counts = dataframe['Roberta_Label_Mapped'].value_counts()
    plt.figure(figsize=(8, 6))
    sentiment_counts.plot(kind='bar', color=['red', 'blue', 'green'])
    plt.title('Roberta Sentiment Analysis of Miami Transit Tweets')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Tweets')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('roberta_sentiment_bar_chart_fixed.png', dpi=300)
    # plt.show()

def plot_roberta_pie_chart(dataframe):
    sentiment_counts = dataframe['Roberta_Label_Mapped'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Roberta Sentiment Distribution of Miami Transit Tweets')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('roberta_sentiment_pie_chart_fixed.png', dpi=300)
    # plt.show()

if __name__ == "__main__":
    plot_roberta_bar_chart(df)
    plot_roberta_pie_chart(df)
