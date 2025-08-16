#apreniendo a usar estructura de datos y clases 
from flask import Flask, render_template
from markupsafe import escape

#indicamos la iniciacion de flask
app = Flask(__name__)
#clase 
class Pelicula:
    def __init__(self, nombre, anio, protagonista):
        self.nombre = nombre
        self.anio = anio
        self.protagonista = protagonista

@app.route("/estructura")#decorador
def estructura_datos():
    # lsita
    peliculas = [
        "El lobo de wall Street",
        "Harry Potter",
        "Volver al Futuro"
    ]
    # diccionario kwargs
    lobo = {
        "Nombre": "El lobo de Wall Street",
        "Anio": 2013,
        "Protagonista":"Leonardo DiCaprio"
    }
    #clase/objetos
    volver = Pelicula("Volver al Futuro", "1985", "Michael J. Fox")

    return render_template("estructuras.html", movies=peliculas, **lobo, destacada=lobo, favorita=volver)

#realizar la conecion automatica al ejecutar el archivo
if __name__ == "__main__":
    app.run()