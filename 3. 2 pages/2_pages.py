# -*- coding:utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', msg='Welcome!',
                            msg_link='Cliquez ici pour aller sur la page suivante')

@app.route('/next')
def page1():
    return render_template('page1.html', msg='Voici la page 1',
                            msg_link='Cliquez ici pour aller sur la page d\'accueil')

if __name__ == '__main__':
    app.run()