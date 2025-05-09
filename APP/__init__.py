# app/__init__.py
from flask import Flask

app = Flask(__name__)

# Carregar configurações (se houver um arquivo config.py)
app.config.from_object('config.Config')  # Caso tenha uma classe Config em config.py

# Importar as rotas
from app import routes
