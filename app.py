# to run the file    python3 test.py
# to make new environment 	run python3 -m venv env
# to open exisiting virtual environment run  		source ./env/bin/activate
# run 		(pip freeze > requirements.txt)

# db
# Create Table information (id smallint unsigned not null auto_increment,name text,email text , dd text, primary key(id));
# mysql -u nikhil -p


from flask import Flask, request, jsonify,render_template
from flask_mysqldb import MySQL
# from flask_sqlalchemy import SQLAlchemy
import yaml
import pickle
import docx
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
from docx import Document
import pandas as pd
import string
import numpy as np
import pickle
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim import models
# from gensim.models import doc2vec

import sklearn
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import random
import seaborn as sns


app = Flask(__name__)


# Configure db
# db = yaml.safe_load(open('db.yaml'))
# app.config['MYSQL_HOST'] = db['mysql_host']
# app.config['MYSQL_USER'] = db['mysql_user']
# app.config['MYSQL_PASSWORD'] = db['mysql_password']
# app.config['MYSQL_DB'] = db['mysql_db']
# app.config['MYSQL_CUSRSORCLASS'] = 'DictCursor'

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'nikhil'
# app.config['MYSQL_PASSWORD'] = 'Nikhil*123'
# app.config['MYSQL_DB'] = 'ime_medical_department'
# app.config['MYSQL_CUSRSORCLASS'] = 'DictCursor'
#mysql = MySQL(app)

filename = ('test_doc2vec_5deppt.model')
model= Doc2Vec.load(filename)



@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route("/predict",methods=['POST'])

def predict():
	dd = [x for x in request.form.values()]
	new_vector = model.infer_vector(dd[2].split())
	output = model.docvecs.most_similar([new_vector])
	if request.method == 'POST':
        # Fetch form data
		userDetails = request.form
		name = userDetails['name']
		email = userDetails['email']
		dd = userDetails['dd']
		#cur = mysql.connection.cursor()
		#cur.execute('''CREATE TABLE IF NOT EXISTS ime_medical_department.test_data(id smallint unsigned not null auto_increment, name text , email text,dd text,primary key(id));''')
		# query = '"INSERT INTO ime_medical_department.tesdt_data(name, email,dd) VALUES (" + name +","  +  email + "," + dd + ");"'
		#cur.execute("INSERT INTO test_data(name, email,dd) VALUES (%s,%s,%s) ",(name, email,dd))
		# cur.execute(query);
		#mysql.connection.commit()
		#cur.close()

	return render_template('index.html', prediction_text='You should go to the department of {}'.format(output[0][0]))
 

if __name__ == '__main__':
	app.run(debug=True)





# from flask import Flask
# from flask_mysqldb import MySQL

# app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'nikhil'
# app.config['MYSQL_PASSWORD'] = 'Nikhil*123'
# app.config['MYSQL_DB'] = 'ime_medical_department'
# app.config['MYSQL_CUSRSORCLASS'] = 'DictCursor'

# mysql = MySQL(app)


# @app.route('/')
# def users():
#     cur = mysql.connection.cursor()
#     cur.execute('''SELECT user, host FROM mysql.user''')
#     cur.execute('''CREATE TABLE IF NOT EXISTS ime_medical_department.test_data(id INTEGER PRIMARY KEY, name text , email text,dd text)''')

#     rv = cur.fetchall()
#     return str(rv)

# if __name__ == '__main__':
#     app.run(debug=True)
