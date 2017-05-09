# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 07:58:45 2017

@author: milal
"""

import feedparser
import json, urllib, requests
# urllib2 -> deprecated ?
from flask import Flask
from flask import render_template
from flask import request

#import redis

app = Flask(__name__)

RSS_FEEDS = {'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn':'http://rss.cnn.com/rss/edition.rss',
             'fox':'http://feeds.foxnews.com/foxnews/latest',
             'iol':'http://iol.co.za/cmlink/1.640'}


def storedb():
    # store somethin into redis DB and persist the data
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set('foo', 'bar')


def get_weather(query):
    api_url = 'http://api.openweathermap.org/data/2.5/weather'
    #q={}&units=metric&appid=8a839a08492fc8191c3b9e02ddcf272b'
    #query = urllib.quote(query)
    payload = {'q': query, 'appid': '8a839a08492fc8191c3b9e02ddcf272b'}
    #url = api_url.format(query)
    #print(url)
    # data = urllib2.open(url).read() #urllib2 does not seem to exist for python3 try request instead
    data = requests.get(api_url, params = payload)
    print(data.text)
    try:
        parsed = json.loads(data.text)
        weather = None
        if parsed.get("weather"):
            weather = {"description":parsed["weather"][0]["description"],
            "temperature":parsed["main"]["temp"],
            "city":parsed["name"]
            }
    except:
        weather = None
    return weather


@app.route("/", methods = ['GET', 'POST'])
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()
    feed=feedparser.parse(RSS_FEEDS[publication])
    weather = get_weather("London,UK")
    #first_article = feed['entries'][0]
    return render_template("home.html", articles = feed['entries'], weather = weather)


def index():
    # storedb()
    return "Hello World!"


if __name__ == '__main__':
    app.run(port=8000, debug=True)
