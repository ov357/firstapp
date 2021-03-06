# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 07:58:45 2017

@author: milal
"""

from flask import Flask
from flask import render_template

#import redis
import feedparser

app = Flask(__name__)

RSS_FEEDS = {'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn':'http://rss.cnn.com/rss/edition.rss',
             'fox':'http://feeds.foxnews.com/foxnews/latest',
             'iol':'http://iol.co.za/cmlink/1.640'}


def storedb():
    # store somethin into redis DB and persist the data
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set('foo', 'bar')


@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed=feedparser.parse(RSS_FEEDS[publication])
    #first_article = feed['entries'][0]
    return render_template("home.html", articles = feed['entries'])


def index():
    # storedb()
    return "Hello World!"


if __name__ == '__main__':
    app.run(port=8000, debug=True)

