#aprender a mejorar las rutas con flask unado las funciones
from flask import Flask, render_template

#indicamos donde esta la carpeta static
app = Flask(__name__, static_folder='estaticos')

@app.route('/')
def home ():

    return render_template("auth/home.html")

@app.route('/store/login')
def login():


    return render_template('auth/login.html')

@app.route('/store/signup')
def signup():

    return render_template('auth/signup.html')


if __name__ == '__main__':
    app.run()