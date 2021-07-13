import sys
sys.executable

# from flask import Flask
# import pickle

from gensim.models.doc2vec import Doc2Vec, TaggedDocument
# from nltk.tokenize import word_tokenize
from gensim.models import doc2vec
sys.path.append('/home/nikhil/.local/lib/python2.7')
sys.path.append('/home/nikhil/.local/lib/python2.7/site-packages')

# print(sys.path)
# import os
# os.getcwd()

x = (sys.argv[1])
dd= (sys.argv[2])
z = (sys.argv[3])
try:
	filename = 'test_doc2vec_5deppt.model'
	model= Doc2Vec.load(filename)
except:
	# dd='hello'
	print(dd)


# from flask import Flask
# app = Flask(__name__)

# @app.route("/")

# def hello():
# 	filename = 'test_doc2vec_5deppt.model'
# 	model= Doc2Vec.load(filename)
# 	return "<h1>hello world</h1>"

# if __name__ == '__main__':
# 	app.run(debug=True)
