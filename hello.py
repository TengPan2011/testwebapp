# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:57:06 2019

@author: Teng Pan
"""

from flask import Flask
#Flask objects are initialized with name of this file
app = Flask(__name__)

#Call the route function here, passing in hello world as the function
@app.route('/')
def hello_world():
    return 'Hello, World!'