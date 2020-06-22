import tweepy
import locations


class Hashtag(tweepy.API):

    def __init__(self, credentials):
        super().__init__(credentials)
    
    def _check_validility(self):
        return self.verify_credentials()
    
    def set_location(self, location):
        self.coordinates = locations.longitude_latitude_dict[location]
        self.woeid = locations.woeid[location]
    
    def set_hashtags(self):
        self.trends = self.trends_place(self.woeid)
        self.hashtags = [trend["name"] for trend in trends[0]["trend"] if '#' in trend["name"]]
    
    def get_hashtags(self):
        for hashtag in self.hashtags:
            print(hashtag)
    
    
