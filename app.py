# import flask
from flask import Flask, render_template, request, jsonify, redirect
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
  return render_template('cats.html')


# GET /cats/onecat
@app.route('/cats/<name>')
def cat_name(name):
  return render_template('cats_name.html', name=name)

fake_database = [
  'fritz the cat',
  'snowball II',
  'cheshire cat',
  'sylvester?'
]

# GET /api/cats -- show cats from our fake db
# POST /api/cats -- create a new cat in our fake db
@app.route('/api/cats', methods=['GET', 'POST'])
def cats_api():
  # get the global var
  global fake_database
  # use an if check to handle http methods
  if request.method == 'GET':
    return jsonify({ 'cats': fake_database })
  if request.method == 'POST':
    # get the request body
    # this is for html form
    # cat = request.form['name']
    # fake_database.append(cat)
    # this is for raw json request bodies
    request_body = request.get_json()
    # add it to our fake database
    fake_database.append(request_body['name'])
    # redirect to /api/cats
    return redirect('/api/cats')