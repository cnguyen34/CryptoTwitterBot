import datetime
import tweepy
import os

API_KEY_CONSUMER = os.environ.get("API_KEY_CONSUMER")
API_SECRET_KEY_CONSUMER = os.environ.get("API_SECRET_KEY_CONSUMER")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")


auth = tweepy.OAuthHandler(API_KEY_CONSUMER, API_SECRET_KEY_CONSUMER)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        current_time = datetime.datetime.now()
        cryptos = ['bitcoin', 'btc', 'ethereum', 'eth', 'xlm', 'stellar', 'doge', 'dogecoin', 'xtz',
                   'tezos', 'cryptocurrency', 'crypto']
        time_string = current_time.strftime("%m/%d/%Y %H:%M:%S")
        if status.user.id_str != '44196397':
            return
        tweet = status.text
        for i in cryptos:
            if i in tweet.lower():
                if i == 'bitcoin' or i == 'btc':
                    elon_string = f"ELON'S TWEET mentioned {i}. At {time_string} CST.\n" \
                                  f"Follow this url to keep track of how it affects the market!\n"
                    elon_string += "https://www.coindesk.com/price/bitcoin\n"
                    elon_string += f"#{i}"
                    api.update_status(status= elon_string)
                elif i == 'ethereum' or i == 'eth':
                    elon_string = f"ELON'S TWEET mentioned {i}. At {time_string} CST.\n" \
                                  f"Follow this url to keep track of how it affects the market!\n"
                    elon_string += "https://www.coindesk.com/price/ethereum\n"
                    elon_string += f"#{i}"
                    api.update_status(status=elon_string)
                elif i == 'xlm' or i == 'stellar':
                    elon_string = f"ELON'S TWEET mentioned {i}. At {time_string} CST.\n" \
                                  f"Follow this url to keep track of how it affects the market!\n"
                    elon_string += "https://www.coindesk.com/price/stellar\n"
                    elon_string += f"#{i}"
                    api.update_status(status=elon_string)
                elif i == 'doge' or i == 'dogecoin':
                    elon_string = f"ELON'S TWEET mentioned {i}. At {time_string} CST.\n" \
                                  f"Follow this url to keep track of how it affects the market!\n"
                    elon_string += "https://www.coindesk.com/price/dogecoin\n"
                    elon_string += f"#{i}"
                    api.update_status(status=elon_string)
                elif i == 'crypto' or i == 'cryptocurrency':
                    elon_string = f"ELON'S TWEET mentioned {i}. At {time_string} CST.\n" \
                                  f"Follow this url to keep track of how it affects the market!\n"
                    elon_string += "https://www.coindesk.com/\n"
                    elon_string += f"#{i}"
                    api.update_status(status=elon_string)
                else:
                    elon_string = f"ELON'S TWEET mentioned {i}. At {time_string} CST.\n" \
                                  f"Follow this url to keep track of how it affects the market!\n"
                    elon_string += "https://www.coindesk.com/price/tezos\n"
                    elon_string += f"#{i}"
                    api.update_status(status=elon_string)
