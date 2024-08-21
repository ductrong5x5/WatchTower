from db import load_db, hello_entry, checkin_entry
from flask import Flask, request, Response, url_for, redirect, render_template
import pandas as pd

app = Flask(__name__)

# Homepage
@app.route('/') 
def home():
  return 'Watchtower'

# Receiving an HTTP payload
@app.route('/hello', methods=['POST'])
def receive_hello():
  json = request.json
  hello_entry(json=json)
  return f'{json}'

# Receiving an HTTP payload
@app.route('/checkin', methods=['POST'])
def receive_checkin():
  json = request.json
  checkin_entry(json=json)
  return f'{json}'

if __name__ == '__main__':
  app.run(host='127.0.0.1', debug=True)