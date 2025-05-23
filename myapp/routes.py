# app/routes.py
from flask import render_template, request, redirect, url_for, flash, Blueprint
from myapp import db
from myapp import models

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

        nova_mensagem = models.Mensagem(
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

@bp.route('/noticia/<slug>', endpoint='noticia_detalhe')
def noticia(slug):
    noticia = models.Noticia.query.filter_by(slug=slug).first_or_404()
    return render_template('noticia.html', noticia=noticia)
    # lógica aqui

@bp.route('/servicos', endpoint='servicos')
def servicos():
    return render_template('Services.html')

@bp.route('/portifolio', endpoint='portifolio')
def portifolio():
    return render_template('Portifolio.html')

@bp.route('/noticia', endpoint='noticia')
def noticia():
    return render_template('noticia.html')

# Tratamento da pagina mensagem

@bp.route('/mensagens')
def listar_mensagens():
    mensagens = models.Mensagem.query.filter_by(snRespondido=False).all()
    return render_template('mensagens.html', mensagens=mensagens)

@bp.route('/responder/<int:id>', methods=['POST'])
def atualizar_resposta(id):
    mensagem = models.Mensagem.query.get_or_404(id)
    mensagem.snRespondido = 'snRespondido' in request.form
    db.session.commit()
    return redirect(url_for('main.listar_mensagens'))

@bp.route('/deletar/<int:id>', methods=['POST'])
def deletar_mensagem(id):
    mensagem = models.Mensagem.query.get_or_404(id)
    db.session.delete(mensagem)
    db.session.commit()
    flash('Mensagem Deletada com sucesso', 'suvess')
    return redirect(url_for('main.listar_mensagens'))