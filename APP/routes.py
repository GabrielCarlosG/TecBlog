# app/routes.py
from flask import render_template
from app import app

@app.route('/', endpoint='index')
def index():
    return render_template('index.html')

@app.route('/fale-conosco', endpoint='fale_conosco')
def fale_conosco():
    return render_template('fale-conosco.html')

@app.route('/sobre', endpoint='sobre')
def sobre():
    return render_template('Sobre.html')

@app.route('/servicos', endpoint='servicos')
def servicos():
    return render_template('Services.html')

@app.route('/portifolio', endpoint='portifolio')
def portifolio():
    return render_template('Portifolio.html')
