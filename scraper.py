import snscrape.modules.twitter as sntwitter


class Scraper:
    """A class to scrape tweets."""

    def __init__(self) -> None:
        self.tweet_list = []

    def get_tweets(self, query, rows):
        """Get tweets based on Advanced search query."""
        tweets = sntwitter.TwitterSearchScraper(query).get_items()

        for tweet in tweets:
            if len(self.tweet_list) == rows:
                break
            self.tweet_list.append([tweet.date, tweet.user.username, tweet.content])

        return self.tweet_list
