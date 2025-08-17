#Regsitr ode usuarios

from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

users = {}
print(users)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        print(users)
        return redirect(url_for('index'))
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True, port=4000)