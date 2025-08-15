#Manejo de macros
from flask import Flask, render_template

app = Flask(__name__)

usuarios = [
    ("Ivan", "admin"), ("Pamela", "user"),
    ("Rodrigo", "user"), ("Rocio", "admin")
]
usuarios2 = [
    ("Victor", "admin"), ("Hugo", "user"),
    ("Diana", "user"), ("Nathaly", "admin")
]

@app.route("/")
def lista_usuarios():
    return render_template("index.html", users = usuarios)

@app.route("/user")
def lista_usuarios2():
    return render_template("index2.html", users2 = usuarios2)

if __name__ == "__main__":
    app.run()