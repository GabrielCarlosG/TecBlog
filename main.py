# app.py
from myapp import  create_app  # Importa a instância Flask do app/__init__.py

app = create_app()

if __name__ == '__main__':
    app.run(debug=False)