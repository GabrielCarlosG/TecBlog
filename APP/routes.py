# app/routes.py
from flask import render_template, request, redirect, url_for
from flask_mail import Message
from app import app, mail

@app.route('/', endpoint='index')
def index():
    return render_template('index.html')

@app.route('/fale-conosco', methods=['GET', 'POST'])
def fale_conosco():
    if request.method == 'POST':
        nome = request.form['nome']
        assunto = request.form['assunto']
        email = request.form['email']
        mensagem = request.form['mensagem']

        # Cria a mensagem de e-mail
        msg = Message(
            'Nova mensagem de Fale Conosco',
            recipients=['adm@cgtech.tec.br'],  # E-mail para onde será enviado
            body=f'Nome: {nome}\nEmail: {email}\nMensagem:\n{mensagem}'
        )

        # Envia o e-mail
        try:
            mail.send(msg)
            return render_template('fale-conosco.html', mensagem_enviada=True)
        except Exception as e:
            print(f'Erro ao enviar e-mail: {e}')
            return render_template('fale-conosco.html', error_message="Ocorreu um erro ao enviar sua mensagem. Tente novamente.")

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
@app.route('/noticia', endpoint='noticia')
def noticia():
    return render_template('noticia.html')
