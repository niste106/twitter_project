from cmd import Cmd
from src.hashtag import Hashtag

class APIPrompt(Cmd, Hashtag):

    prompt = '>>>'

    def do_exit(self, inp):
        print("Exit")
        return True


if __name__=='__main__':
    
    APIPrompt().cmdloop()