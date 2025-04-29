import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

df = pd.read_csv('miami_transit_tweets.csv', names=["Tweet_ID", "Author_ID", "Created_At", "Text"])

def clean_text(text):
    text = str(text)
    text = text.replace('\n', ' ').replace('\r', ' ')
    return text

df['Cleaned_Text'] = df['Text'].apply(clean_text)

def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

df['Sentiment_Score'] = df['Cleaned_Text'].apply(get_sentiment)

def label_sentiment(score):
    if score > 0.1:
        return 'Positive'
    elif score < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

df['Sentiment_Label'] = df['Sentiment_Score'].apply(label_sentiment)

print(df['Sentiment_Label'].value_counts())

df['Sentiment_Label'].value_counts().plot(kind='bar')
plt.title('Sentiment Analysis of Miami Transit Tweets')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

df.to_csv('miami_transit_tweets_with_sentiment.csv', index=False)
