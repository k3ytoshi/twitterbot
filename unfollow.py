#! /usr/bin/python

import tweepy
from config import SLEEP_TIME
from credentials import credentials
from time import sleep

SCREEN_NAME = credentials['screen_name']
CONSUMER_KEY = credentials['consumer_key']
CONSUMER_SECRET = credentials['consumer_secret']
ACCESS_TOKEN = credentials['access_token']
ACCESS_TOKEN_SECRET = credentials['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

followers = api.followers_ids(SCREEN_NAME)
friends = api.friends_ids(SCREEN_NAME)

for f in friends:
    if f not in followers:
        print('Unfollowed the user ' + api.get_user(f).screen_name)
        format(api.get_user(f).screen_name)
        api.destroy_friendship(f)

    sleep(SLEEP_TIME)