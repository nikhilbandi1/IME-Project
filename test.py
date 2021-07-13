# to run the file    python3 test.py
# to make new environment 	run python3 -m venv env
# to open exisiting virtual environment run  		source ./env/bin/activate
# run 		(pip freeze > requirements.txt)

# db
# Create Table information (id smallint unsigned not null auto_increment,name text,email text , dd text, primary key(id));

# Configure db
# db = yaml.safe_load(open('db.yaml'))
# app.config['MYSQL_HOST'] = db['localhost']
# app.config['MYSQL_USER'] = db['nikhil']
# app.config['MYSQL_PASSWORD'] = db['nikhil*123']
# app.config['MYSQL_DB'] = db['ime_medical_department']


# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'nikhil'
# app.config['MYSQL_PASSWORD'] = 'Nikhil*123'
# app.config['MYSQL_DB'] = 'ime_medical_department'

from flask import Flask, request, jsonify,render_template
import pickle
import docx

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

filename = ('test_doc2vec_5deppt.model')
model= Doc2Vec.load(filename)

@app.route("/")
def home():
	return render_template('index.html')

@app.route("/predict",methods=['POST'])

def predict():
	dd = [x for x in request.form.values()]
	# print(dd)
	new_vector = model.infer_vector(dd[2].split())
	output = model.docvecs.most_similar([new_vector])
	return render_template('index.html', prediction_text='You should go the Department of {}'.format(output[0][0]))
 

if __name__ == '__main__':
	app.run(debug=True)
