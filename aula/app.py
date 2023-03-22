from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///produtos.sqlite3'

db = SQLAlchemy(app)


class Produto(db.Model):
    id = db.Column('id', db.Integer, primary_key=True,  autoincrement=True)
    nome = db.Column(db.String(150))
    preco = db.Column(db.Float)
    sinopse = db.Column(db.String(500))
    quantidade = db.Column(db.Integer)
    autor = db.Column(db.String(150))
    editora = db.Column(db.String(150))

    def __init__(self, nome, preco, sinopse, quantidade, autor, editora):
        self.nome = nome
        self.preco = preco
        self.sinopse = sinopse
        self.quantidade = quantidade
        self.autor = autor
        self.editora = editora


@app.route('/')
def exibir_produtos():
    produtos = Produto.query.all()
    return render_template('produtos.html', produtos=produtos)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
