import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_csv('miami_transit_tweets.csv', names=["Tweet_ID", "Author_ID", "Created_At", "Text"])

def clean_text(text):
    text = str(text)
    text = text.replace('\n', ' ').replace('\r', ' ')
    return text

df['Cleaned_Text'] = df['Text'].apply(clean_text)

analyzer = SentimentIntensityAnalyzer()

def get_vader_sentiment(text):
    scores = analyzer.polarity_scores(text)
    return scores['compound']

df['VADER_Score'] = df['Cleaned_Text'].apply(get_vader_sentiment)

def label_vader_sentiment(score):
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

df['VADER_Label'] = df['VADER_Score'].apply(label_vader_sentiment)

df.to_csv('miami_transit_tweets_with_vader.csv', index=False)

print(df[['Cleaned_Text', 'VADER_Score', 'VADER_Label']].head())
