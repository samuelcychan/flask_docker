from flask import Flask
from flask import render_template
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

""" @app.route("/hello/<name>")
def hello(name):
    now = datetime.now()
    fnow = now.strftime('%A $d %B %Y at %X')
    match_obj = re.match('[a-zA-Z]+', name)
    if match_obj:
        cname = match_obj.group(0)
    else:
        cname = 'friend'
    content = "hi, " + cname + '! it\'s' + fnow
    return content """

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello.html",
        name=name,
        date=datetime.now()
    )

@app.route('/api/data')
def get_data():
    return app.send_static_file('data.json')