from flask import Flask, render_template
from markupsafe import escape

#nombre del codigo determina la ubicacion de la carpeta raiz
app = Flask(__name__)

#usar plantillas html y redireccionar
@app.route("/")# ers una plantilla
def web_index():
    #tempale nos ayuda a identificar la caroeta templates donde se encuetra los html o plantillas html
    return render_template('index.html')

@app.route("/nosotros")
def web_nostros():
    return render_template("nosotros.html")

#url
# @app.route("/")#decorador que ejecuta en la carpeta raiz y puedes manejar las rutas
# def hello_world():
#     return "Hello World!!!"

@app.route("/inicio")
def inicio():
    return"""
        <html>
            <body>
                <h1>Saludo bienvenido a inicio</h1>
                <p>Esta vista pertenece a la pagiana inicio</p>
            </body>
        </html>
    """

#resive pararmetros dinamicos y los usa para su veneficio
ruta = "/saludo/<nombre>/"
@app.route(ruta)
def saludo(nombre):
    return f"Saludos {escape(nombre)}"

#usando la misma plantilla para diferentes datos mandamos en la variable y ruta
@app.route("/python")
def curso_1():
    #retornamos el archivo html y las varaibles que su usarasn en la pagina
    return render_template(template_name_or_list="modificable.html",nombre="victor",curso="Flask")

@app.route("/php")
def curso_2():
    #retornamos el archivo html y las varaibles que su usarasn en la pagina
    return render_template(template_name_or_list="modificable.html",nombre="victor",curso="PHP")

#envio de variables para realizar operaciones
@app.route("/expresiones")
def expresiones():
    return render_template("expresiones.html", nombre='victor', apellido='huallpa', color='verde', altura=45, base=14)

@app.route("/expresiones2")
def expresiones2():
    #entraga de datos con un diccionario 'kwargs
    kwargs = {
        "nombre":"victor",
        "apellido":"huallpa",
        "color":'naranja',
        "base":2,
        "altura":5
    }
    return render_template("expresiones.html", **kwargs)

#ejecuta flask 
if __name__ == "__main__":
    # DEBUG = True
    app.run()

