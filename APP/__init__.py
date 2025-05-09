# app/__init__.py
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

# Carregar configurações (se houver um arquivo config.py)
app.config.from_object('config.Config')  # Caso tenha uma classe Config em config.py

# Inicializa o Flask-Mail
mail = Mail(app)

# Importar as rotas
from app import routes
