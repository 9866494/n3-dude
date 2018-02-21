#! /usr/bin/env python
# coding=utf-8

from flask import Flask
from flask import request
app = Flask(__name__)
import os

@app.route("/")
def index():
    textToSay = "АЛАРМ АЛАРМ ТЕСТАМ ПИЗДЕЦ"
    os.system("echo " + textToSay + " | festival --tts")
    return textToSay
