from flask import Flask, render_template, request,jsonify
from flask import json
from flask.wrappers import Response

import util
app = Flask(__name__)


@app.route('/getLoc')
def getLocation():
    response = jsonify({
        'locations' : util.getLocation()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
        
    return response

@app.route('/')
def home():
    return 'Hello Flask'

if __name__ == "__main__":
    app.run(debug = True)
