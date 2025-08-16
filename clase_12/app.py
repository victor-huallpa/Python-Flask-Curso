# Keyword "is", <ruta> es la namera como se puede obtener datos
#despues de ello trabajar con esa informaicon para consultas a base de datos, 
#retornar vistas
from flask import Flask, render_template

app = Flask(__name__)

lista = ['Ivan', 'Maria', "George"]
@app.route("/")
def key_inicio():

    return render_template("index.html", var = lista)
if __name__ == "__main__":
    app.run()