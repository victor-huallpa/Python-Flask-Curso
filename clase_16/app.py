# incrustacion de html desde python o inyeccion html
from flask import Flask, render_template

app = Flask(__name__)

html = """
    <ul>
        <li class="list">inicio</li>
        <li class="list">categorias</li>
        <li class="list">nosotros</li>
    </ul>

"""
vews = ['index.html', 'plantilla.jinja2']
@app.route('/')
def home():

    return render_template(vews[0], inyection = html)
if __name__ == "__main__":
    app.run()