from flask import Flask, render_template, request
import json
import os
import psycopg2

application = Flask(__name__)
STATIC_PATH = os.path.dirname(os.path.abspath(__file__)) + "/static"

conn = psycopg2.connect(
        user=os.environ.get("PGUSER"),
        host=os.environ.get("PGHOST"),
        port=os.environ.get("PGPORT"),
        password=os.environ.get("PGPASSWORD"),
        database=os.environ.get("PGDATABASE")
        )

@application.route('/')
def home():
    cur = conn.cursor()
    cur.execute("select * from testing")
    words = cur.fetchall()
    return render_template('index.html', testing=words)

if __name__ == "__main__":
    application.run()
