from cmd import Cmd
from src.hashtag import Hashtag


class APIPrompt(Hashtag, Cmd):

    def __init__(self, credentials):
        Hashtag.__init__(self, credentials)
        Cmd.__init__(self)

    prompt = '>>'

    def do_set_location(self, location):
        self.set_location(location)
    
    def do_trends(self, *args):
        self.set_hashtags()
        self.get_hashtags()
    
    def do_exit(self):
        return True
