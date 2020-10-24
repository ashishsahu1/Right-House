import requests
import configparser
from flask import Flask, render_template, request
from requests import api

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Flask'

if __name__ == "__main__":
    app.run(debug = True)
