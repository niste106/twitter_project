import csv
import json
import tweepy
import src.locations as locations


class Hashtag(tweepy.API):

    def __init__(self, credentials, save_path='output\\search_results.csv'):
        self.save_path = save_path
        super().__init__(credentials)
    
    def _check_validility(self):
        return self.verify_credentials()
    
    def set_location(self, location):
        self.location = location
        self.coordinates = locations.longitude_latitude_dict[location]
        self.woeid = locations.woeid_dict[location]
    
    def set_hashtags(self):
        trends = self.trends_place(self.woeid)
        self.hashtags = [trend["name"] for trend in trends[0]["trends"] if trend["name"].startswith('#')]
    
    def get_hashtags(self):
        for hashtag in self.hashtags:
            print(hashtag)
    
    def get_hashtag_tweeds(self, hashtag):
        hashtag_tweets = []
        search_results = self.search(
            q=hashtag,
            geocode=self.coordinates,
            result_type='current'
        )
        for search_result in search_results:
            search_result_dict = {
                'id': search_result.id,
                'hashtag' : hashtag,
                'text' : search_result.text,
                'created_at' : search_result.created_at,
                'retweeted' : search_result.retweeted,
                'retweet_count' : search_result.retweet_count,
                'favorite_count' : search_result.favorite_count,
                'location': self.location,
                'user': search_result.user.name
            }
            hashtag_tweets.append(search_result_dict)

        return hashtag_tweets

    def hashtag_tweets_json(self):

        hashtag_tweets_json = []
        for hashtag in self.hashtags:
            hashtag_tweets_json += self.get_hashtag_tweeds(hashtag)
        return hashtag_tweets_json
    
    def update(self):

        hashtag_tweets = self.hashtag_tweets_json()
        hashtag_tweets.sort(key=lambda x: x['id'])
        fnames = ['id','hashtag','text','created_at','retweeted','retweet_count','favorite_count','location','user']

        with open(self.save_path, mode='a', encoding='utf-8') as output_csv:
            writer = csv.DictWriter(output_csv, fieldnames=fnames)
            for hashtag_tweet in hashtag_tweets:
                writer.writerow(hashtag_tweet)
        

    

