import os
from flask import Flask, request #, send_file("file", as_attachment=True) # only if no user input
from flask import send_from_directory, render_template
from flask import jsonify
from flask_cors import CORS
# from dotenv import load_dotenv

from db import PGDB

app = Flask(__name__, template_folder="pages",
	static_folder="../static", static_url_path='/')

STATIC_DIR = f'{app.root_path}/../static'

CORS(app)
# CORS(app, resource={ r"/*": {"origins": os.getenv("FRONTEND_URL")} })

db = PGDB (
	database = os.getenv("POSTGRES_DBNAME"),
	host	 = os.getenv("POSTGRES_HOST"),
	user	 = os.getenv("POSTGRES_USER"),
	password = os.getenv("POSTGRES_PASS")
)

def cleanup(ss):
	""" """
	return ss.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')

def logg(ss, *args, **kwargs):
	""" """
	print(ss, *args, **kwargs)


@app.route("/")
def index():
	""" """
	return render_template('index.html', name='index')

@app.route("/route")
def route():
	return {'site': '/route'}, 200


# As Standalone
if __name__ == "__main__":
	app.run(port='5002', debug=True)


