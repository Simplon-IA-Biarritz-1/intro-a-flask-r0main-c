# -*- coding:utf-8 -*-

from flask import Flask, request, render_template
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import numpy as np
##from keras.datasets import mnist
import pickle

app = Flask(__name__)

##(X_train, y_train), (X_test, y_test) = mnist.load_data()
##
##X = np.concatenate((X_train, X_test))
##X = X.reshape(len(X), -1)
##y = np.concatenate((y_train, y_test))
##
##rfc = RandomForestClassifier()
##rfc = rfc.fit(X, y)
##
##with open('pickle_rfc', 'wb') as fichier:
##    fichier.write(pickle.dumps(rfc))

with open('pickle_rfc', 'rb') as fichier:
    clf = pickle.loads(fichier.read())

@app.route('/')
def accueil():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def upload():
    if request.method == 'POST':
        uploaded_file = request.files['file_upload']
        picture = Image.open(uploaded_file)
        picture = picture.convert('L')
        picture = picture.convert('1')
        picture = np.array(picture).flatten()
        picture = picture.reshape(1,-1)

        return render_template('index.html', resultat=clf.predict(picture))

if __name__ == '__main__':
    app.run()