import datetime
import schedule
import time
import tweepy
import os
from exchanges import Exchanges
from assets import Assets
from elon import MyStreamListener

API_KEY_CONSUMER = os.environ.get("API_KEY_CONSUMER")
API_SECRET_KEY_CONSUMER = os.environ.get("API_SECRET_KEY_CONSUMER")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")


auth = tweepy.OAuthHandler(API_KEY_CONSUMER, API_SECRET_KEY_CONSUMER)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Update Profile Image
# api.update_profile_image(filename)
#
# Update Profile Header
# api.update_profile(name, url, location, description)


# Follow people who use hashtags of crypto that you track to grow your twitter bot
# for follower in tweepy.Cursor(api.search, q="#BTC").items(50):
#     api.create_friendship(screen_name = follower.author.screen_name)
#
# for follower in tweepy.Cursor(api.search, q="#DOGE").items(50):
#     api.create_friendship(screen_name = follower.author.screen_name)
#
# for follower in tweepy.Cursor(api.search, q="#ETH").items(50):
#     api.create_friendship(screen_name = follower.author.screen_name)
#
# for follower in tweepy.Cursor(api.search, q="#XLM").items(50):
#     api.create_friendship(screen_name = follower.author.screen_name)



myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
myStream.filter(follow = ['44196397'], is_async= True)

def check_time():
    current_time = datetime.datetime.now()
    time_string = current_time.strftime("%H")
    return time_string

exchanges = Exchanges()
assets = Assets()

schedule.every().day.at("00:00").do(assets.beginning_prices)
schedule.every().hour.at(":00").do(check_time)
schedule.every().day.at("00:00").do(assets.print_beginning_prices, api)
schedule.every().day.at("23:55").do(assets.closing_prices, api)
if check_time() != "00":
    schedule.every().hour.at(":00").do(assets.curr_prices, api)
schedule.every().hour.at(":15").do(assets.curr_prices, api)
schedule.every().hour.at(":30").do(assets.curr_prices, api)
schedule.every().hour.at(":45").do(assets.curr_prices, api)
schedule.every().hour.at(":00").do(exchanges.exc_prices, api)

while 1:
    schedule.run_pending()
    time.sleep(1)

