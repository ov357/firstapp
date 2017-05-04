# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 07:58:45 2017

@author: milal
"""

from flask import Flask
import redis


app = Flask(__name__)


def storedb():
    # store somethin into redis DB and persist the data
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set('foo', 'bar')


@app.route("/")
def index():
    # storedb()
    return "Hello World!"


if __name__ == '__main__':
    app.run(port=8000, debug=True)


