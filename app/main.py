import os
from flask import Flask, request #, send_file("file", as_attachment=True)
from flask_cors import CORS
# from dotenv import load_dotenv

from db import PGDB

app = Flask(__name__) #static_folder='web/static'

PUBLIC_DIR = f'{app.root_path}/../public'

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
	return {'site': 'index'}, 200


# As Standalone
if __name__ == "__main__":
	app.run(port='5002', debug=True)
