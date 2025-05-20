from app import db
from datetime import datetime

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    assunto = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow)
    snRespondido = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Mensagem {self.nome} - {self.assunto}>'