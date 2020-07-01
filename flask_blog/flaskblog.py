import os
os.environ['PORT'] = '5000'
os.environ['IP'] = '0.0.0.0'
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'