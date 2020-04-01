# -*- coding:utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def formulaire():
    prenom = request.form['prenom'].capitalize()
    nom = request.form['nom'].capitalize()
    sexe = request.form['sexe'].lower()
    nick = request.form['nick']

    if sexe == 'homme':
        resultat = 'Bonjour M '
    elif sexe == 'femme':
        resultat = 'Bonjour Mme '
    else:
        resultat = 'Bonjour '

    resultat += f'{prenom} {nom}, votre nom d\'utilisateur est : {nick}'
    print(resultat)

    return render_template('resultats.html', reponse=resultat)

if __name__ == '__main__':
    app.run()