#filtro

from flask import Flask, render_template

app = Flask(__name__)

usuarios = ["Ivan", "Pamela", "Rodrigo"]

#decorador que carga la pagina principal
@app.route("/")
def lista_usuarios():
    return render_template("index.html", users = usuarios)

if __name__ == "__main__":
    app.run()