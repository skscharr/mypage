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
    print type(bbi)
    return render(request, template, {'blog_basic_info':bbi})

    blog_posts = requests.get('http://api.tumblr.com/v2/blog/skscharr.tumblr.com/posts', params=api_key)
    blog_posts.json()

def linkedin_api(request, template='web_api_calls'):
