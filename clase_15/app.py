# Eliminar espacios en flask y jinja
from flask import Flask , render_template

app = Flask(__name__)
lista = [
    'Victor', 'Hugo', 'Huallpa', 'Huahuacondori'
]
word = 'Bienvenido!'
@app.route('/')
def home():

    return render_template('index.html', lista = lista, word = word)