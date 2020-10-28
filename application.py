from flask import Flask, render_template, request
import json
import os
import psycopg2

application = Flask(__name__)
STATIC_PATH = os.path.dirname(os.path.abspath(__file__)) + "/static"

@application.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    application.run()