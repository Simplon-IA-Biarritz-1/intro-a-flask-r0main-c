# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, Markup
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client['test_formulaire']

@app.route('/')
def accueil():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def formulaire():
    prenom = request.form['prenom'].capitalize()
    nom = request.form['nom'].capitalize()
    sexe = request.form['sexe'].lower()
    nick = request.form['nick'].lower()

    data = {'_id':nick, 'prenom':prenom, 'nom':nom, 'sexe':sexe}

    try:
        db['users'].insert(data)
    except DuplicateKeyError:
        return render_template('resultats.html', reponse='Votre pseudo est déjà utilisé!')

    else:
        if sexe == 'homme':
            resultat = 'Bonjour M '
        elif sexe == 'femme':
            resultat = 'Bonjour Mme '
        else:
            resultat = 'Bonjour '

        resultat += f'{prenom} {nom}, votre nom d\'utilisateur est : {nick}'

        return render_template('resultats.html', reponse=resultat)

@app.route('/liste_inscrits')
def liste_inscrits():
    users_bdd = Markup('<br>'.join(db['users'].find().distinct('_id')))
    return render_template('liste_inscrits.html', str=users_bdd)

if __name__ == '__main__':
    app.run()