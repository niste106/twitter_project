import tweepy

from src.console import APIPrompt



if __name__=='__main__':
    print('Insert your API key:')
    api_key = input()
    print('Insert your API secret key:')
    api_secret_key = input()
    print('Insert your acces token:')
    access_token = input()
    print('Insert your secret access token:')
    access_secret_token = input()

    

    #auth = tweepy.OAuthHandler(api_key, api_secret_key)
    #auth.set_access_token(access_token, access_token_key)

    prompt = APIPrompt(auth)

    prompt.cmdloop()




