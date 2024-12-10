import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob


class TwitterClient:
    '''
    Generic Twitter Class for sentiment analysis.
    '''

    def __init__(self):
        '''
        Class constructor for authentication and API setup.
        '''
        # Keys and tokens from the Twitter Developer Console
        consumer_key = 'tYo0BJCArBRsKDqfvVPqo6Nhl'
        consumer_secret = 'lBHkOKp9oxFFhsTf8f9fOdXh5fs0QKmadtCcycensxnB4Wmo6E'
        access_token = 'AAAAAAAAAAAAAAAAAAAAAIypxQEAAAAAZgrWDuwCLnAFL5ouu%2FTtbdpBvGs%3DCEkBRi5mIQJxNk5UUnUNGsS8VIOwZm7V96Ib6vUZtut3IwV1om'
        access_token_secret = 'UjA8VPlENbZHI9Lhuu4aFykdE2orruofcAFyt7C3gzoEM'

        # Attempt authentication
        try:
            # Create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # Set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # Create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except Exception as e:
            print(f"Error: Authentication Failed - {e}")

    def clean_tweet(self, tweet):
        """
        Utility function to clean tweet text by removing links, special characters,
        and usernames using regular expressions.
        """
        return ' '.join(re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        """
        Utility function to classify the sentiment of a tweet using TextBlob.
        """
        analysis = TextBlob(self.clean_tweet(tweet))
        # Determine sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count=10):
        """
        Main function to fetch tweets and parse them.
        """
        tweets = []

        try:
            # Fetch tweets using the API
            fetched_tweets = self.api.search_tweets(q=query, count=count)

            # Parse tweets
            for tweet in fetched_tweets:
                parsed_tweet = {
                    'text': tweet.text,
                    'sentiment': self.get_tweet_sentiment(tweet.text)
                }
                # Append tweet if not already present
                if parsed_tweet not in tweets:
                    tweets.append(parsed_tweet)

            return tweets

        except tweepy.TweepError as e:
            print(f"Error: {e}")
            return []


def main():
    # Create a TwitterClient object
    api = TwitterClient()
    # Fetch tweets
    tweets = api.get_tweets(query='Donald Trump', count=200)

    if not tweets:
        print("No tweets retrieved.")
        return

    # Separate tweets by sentiment
    positive_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    negative_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    # Print sentiment analysis summary
    print(f"Positive tweets percentage: {100 * len(positive_tweets) / len(tweets):.2f}%")
    print(f"Negative tweets percentage: {100 * len(negative_tweets) / len(tweets):.2f}%")
    print(
        f"Neutral tweets percentage: {100 * (len(tweets) - len(positive_tweets) - len(negative_tweets)) / len(tweets):.2f}%")

    # Print example positive tweets
    print("\nPositive tweets:")
    for tweet in positive_tweets[:10]:
        print(tweet['text'])

    # Print example negative tweets
    print("\nNegative tweets:")
    for tweet in negative_tweets[:10]:
        print(tweet['text'])


if __name__ == "__main__":
    # Run the main function
    main()
