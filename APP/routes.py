# app/routes.py
from flask import render_template, request, redirect, url_for, flash, Blueprint
from app import db
from app.models import Mensagem

bp = Blueprint('main', __name__)

@bp.route('/', endpoint='index')
def index():
    return render_template('index.html')

@bp.route('/fale-conosco', methods=['GET', 'POST'])
def fale_conosco():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        assunto = request.form.get('assunto')
        mensagem = request.form.get('mensagem')

        if not nome or not email or not mensagem:
            flash('Por favor, preencha todos os campos.', 'error')
            return redirect(url_for('main.fale_conosco'))

        nova_mensagem = Mensagem(
            nome=nome, 
            email=email, 
            assunto = assunto,
            mensagem=mensagem)
        db.session.add(nova_mensagem)
        db.session.commit()

        flash('Mensagem enviada com sucesso!', 'success')
        return redirect(url_for('main.fale_conosco'))

    return render_template('fale-conosco.html')

@bp.route('/sobre', endpoint='sobre')
def sobre():
    return render_template('Sobre.html')

@bp.route('/servicos', endpoint='servicos')
def servicos():
    return render_template('Services.html')

@bp.route('/portifolio', endpoint='portifolio')
def portifolio():
    return render_template('Portifolio.html')
@bp.route('/noticia', endpoint='noticia')
def noticia():
    return render_template('noticia.html')

@bp.route('/mensagens')
def listar_mensagens():
    mensagens = Mensagem.query.all()
    return render_template('mensagens.html', mensagens=mensagens)
