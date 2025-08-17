#Regsitr ode usuarios
import random
from flask import Flask, render_template, redirect, request, url_for, session
#metodo apra crear la sesion es session de flask

app = Flask(__name__)
app.secret_key = str(random.uniform(1000,999999))

users = [
    {'username': 'admin', 'password': 'admin'}
]
print(users)
@app.route('/')
def index():
    user = session.get('user')
    if user:
        return render_template('index.html', user = user)
    else:
        
        return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['user'] = username#creas la sesion
        list_user = {
            "username": username,
            "password": password
        }
        users.append(list_user)
        print(users)
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user['username'] == username and user['password'] == password:
                session['user'] = username#creas la sesion
                return redirect(url_for('index'))
        else:
            mensaje = 'error usuario o contrasenia incorrecta'
            return render_template('login.html', message = mensaje)
    return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True, port=4000)