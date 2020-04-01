# -*- coding:utf-8 -*-

# Je sais que ce code n'est pas sécurisé par rapport à l'envoi de fichier. J'ai fait au plus vite.

from flask import Flask, request, render_template, Markup
import pandas as pd

app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def upload():
    if request.method == 'POST':
        data = request.files['file_upload']
        data = pd.read_csv(data)

        data_describe = data.describe().to_html()

        return render_template('index.html', describe=Markup(data_describe))

if __name__ == '__main__':
    app.run()