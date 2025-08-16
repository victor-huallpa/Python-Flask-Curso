#reutilizacion de plantillas con la keyword include jinja
from flask import Flask, render_template

app = Flask(__name__, template_folder='plantillas')

@app.route('/')
def inicio():

    return render_template('home.html', title='Mi sitio web')
items = [
    {"nombre": "Mouse", "cantidad": 5},
    {"nombre": "Monitor", "cantidad": 3},
    {"nombre": "Teclaso", "cantidad": 8}
]

@app.route('/tienda')
def tienda():

    return render_template(
        "tienda.html", nombre = 'Pedrito',
        direccion = 'La victoria',
        empleados = ['Juan', "Sofia", "Marta"],
        items = items
        )

@app.route('/store/item')
def items_show():

    return render_template('items.html', items=items)
if __name__ == "__main__":
    app.run()

