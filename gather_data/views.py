from django.shortcuts import render
from django.http import HttpResponse
import tweepy
import json
from tweepy import OAuthHandler

consumer_key = "akkF8ZwlKGjCq5eRIWsnjau4e"
consumer_secret = "e4CQYDdnZf08CZmenaPTWAID5GfAHYHzPqYUKPBHF6Zcs49Ff6"
access_token = "371675359-EFIANnRbEdJtGB4BtSejdFx631BgXbiYtuPAndSh"
access_secret = "b2HLdu8ktdnTlJqRyf6CP3i3KXrUmjCHW6PIUnW9OyoMA"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def display_tweets_json(request):
    for status in tweepy.Cursor(api.home_timeline).items(10):
        dt = json.dumps(status._json)

    return HttpResponse(dt)


def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)