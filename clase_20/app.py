#hasheo de palabras, se usan par alogins codigo etc
from passlib.hash import pbkdf2_sha256

from flask import Flask, render_template, url_for, redirect, request, session

app = Flask(__name__)
app.secret_key = 'supersecreto'

words = {}
@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        word = request.form['word']
        word_hash = pbkdf2_sha256.hash(word)
        words[word] = word_hash
        return redirect(url_for('home'))
    
    return render_template('index.html', word_hashed=words)

if __name__ == "__main__":
    app.run(debug=True)