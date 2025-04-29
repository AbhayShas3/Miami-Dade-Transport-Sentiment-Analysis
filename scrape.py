import tweepy
import os
import csv
from datetime import datetime

bearer_token = 'REMOVED_SECRET'

client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

query = '("Miami-Dade Transit" OR "Better Bus Network" OR #BetterBusNetwork OR "Miami transit") lang:en -is:retweet'

max_results = 100

output_file = "miami_transit_tweets.csv"

with open(output_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Tweet_ID", "Author_ID", "Created_At", "Text"])  
    tweet_count = 0

    try:
        for response in tweepy.Paginator(
            client.search_recent_tweets,
            query=query,
            max_results=max_results,
            sort_order="recency",  
            tweet_fields=["id", "text", "created_at", "author_id", "lang"],
        ):
            if response.data is None:
                continue
            for tweet in response.data:
                writer.writerow([tweet.id, tweet.author_id, tweet.created_at, tweet.text.replace('\n', ' ')])
                tweet_count += 1
                print(f"Fetched {tweet_count} tweets...", end="\r")

    except tweepy.TooManyRequests:
        print("\nRate limit reached. Sleeping for 15 minutes...")
        time.sleep(15 * 60)

    except Exception as e:
        print(f"\nAn error occurred: {e}")

print(f"\nDone! Total tweets fetched and saved to {output_file}: {tweet_count}")
