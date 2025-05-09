# app/routes.py
from flask import render_template, request, redirect, url_for
from app import app

@app.route('/', endpoint='index')
def index():
    return render_template('index.html')

@app.route('/fale-conosco', methods=['GET', 'POST'])
def fale_conosco():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        # Aqui, você pode salvar os dados no banco de dados ou enviar um e-mail, por exemplo.
        # Vou apenas exibir os dados no terminal para teste
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"Assunto: {assunto}")
        print(f"Mensagem: {mensagem}")

        # Após processar, podemos redirecionar para a página ou mostrar uma mensagem de sucesso
        return render_template('fale-conosco.html', mensagem_enviada=True)

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
