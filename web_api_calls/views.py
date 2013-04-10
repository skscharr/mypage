from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
import os

def tumblr_api(request, template='web_api_calls.html'):
    env_api = os.environ.get('TUMBLR_PUBLIC_KEY', None)
    api_key = {'api_key' : env_api}

    blog_basic_info = requests.get('http://api.tumblr.com/v2/blog/skscharr.tumblr.com/info', params=api_key)
    bbi = blog_basic_info.json()

    blog_posts = requests.get('http://api.tumblr.com/v2/blog/skscharr.tumblr.com/posts', params=api_key)
    bp = blog_posts.json()

    return render(request, template, {'blog_posts':bp, 'blog_basic_info':bbi})

'''def linkedin_api(request, template='web_api_calls.html'):
    env_api = os.environ.get('LINKEDIN_API_KEY', None)
    env_sec = os.environ.get('LINKEDIN_SECRET_KEY', None)

def twitter_api(request, template='web_api_calls.html'):
    my_tweets = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=16sks')
    mt = my_tweets.json()
    return render(request, template, {'my_tweets':mt})'''

def github_api(request, template='web_api_calls.html'):
  events_performed = requests.get('https://api.github.com/users/skscharr/events')
  ep = events_performed.json()

  events_received = requests.get('https://api.github.com/users/skscharr/received_events')
  er = events_received.json()
  
  return render(request, template, {'events_received':er, 'events_performed':ep})