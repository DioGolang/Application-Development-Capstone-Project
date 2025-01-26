import requests
from flask import Flask, escape

app = Flask(__name__)

# @app.route('/')
# def hello_world():
# 	course = request.args['course']
# 	rating = request.args.get('rating')
# 	return {"message": f"{course} with rating {rating} has been added"}

# @app.route('/')
# def get_author():
# 	res = requests.get('https://openlibrary.org/search/authors.json?q=Michael Crichton')
# 	if res.status_code == 200:
# 		return { "message": res.json()}
# 	elif res.status_code == 404:
# 		return {"message": "Author not found"}, 404
# 	else:
# 		return {"message": "Something went wrong"}, 500

# python3 -m pip install pymongo
# python3 mongo_connect.py


@app.route('/')
def get_author(isbn):
	res = requests.get(f'https://openlibrary.org/isbn/{escape(isbn)}.json')
	if res.status_code == 200:
		return { "message": res.json()}
	elif res.status_code == 404:
		return {"message": "Author not found"}, 404
	else:
		return {"message": "Something went wrong"}, 500

