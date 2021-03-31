# import flask
from flask import Flask
# import dotenv
from dotenv import load_dotenv
# import the operationg system
import os

print(os.environ['MY_BIG_SECRET'])

# config the app
app = Flask(__name__)

# make a route!
@app.route('/')
def hello_flask():
  return 'hello from flask 🎉'

# GET /cats -- landing page for the cat cafe
@app.route('/cats')
def cats():
  return 'cat cafe 🐈'


# GET /cats/onecat
@app.route('/cats/<name>')
def cat_name(name):
  return f'in the cafe, we have {name} 🐱'