import tweepy
import src.locations as locations


class Hashtag(tweepy.API):

    def __init__(self, credentials):
        super().__init__(credentials)
    
    def _check_validility(self):
        return self.verify_credentials()
    
    def set_location(self, location):
        self.coordinates = locations.longitude_latitude_dict[location]
        self.woeid = locations.woeid_dict[location]
    
    def set_hashtags(self):
        trends = self.trends_place(self.woeid)
        self.hashtags = [trend["name"] for trend in trends[0]["trends"] if trend["name"].startswith('#')]
    
    def get_hashtags(self):
        for hashtag in self.hashtags:
            print(hashtag)
    
    def count_hashtag_tweed(self):
        for hashtag in self.hashtags:
            pass

    def save_hashtags_tweeds(self):
        pass
    

