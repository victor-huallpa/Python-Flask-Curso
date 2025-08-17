#hasheo de palabras, se usan par alogins codigo etc
from passlib.hash import pbkdf2_sha256

from flask import Flask, render_template, url_for, redirect, request, session

app = Flask(__name__)
app.secret_key = 'supersecreto'

words = {}
@app.route('/', methods = ['GET', 'POST'])
def home():
    messages = 'sin mensaje'   # siempre inicializado
    
    if request.method == 'POST' and request.form.get('word'):
        word = request.form.get('word')
        word_hash = pbkdf2_sha256.hash(word)
        words[word] = word_hash
        return redirect(url_for('home'))
    
    if request.method == 'POST' and request.form.get('word_ve'):
        word = request.form.get('word_ve')
        if word in words and pbkdf2_sha256.verify(word, words[word]):
            messages = f"{word} es verificado al hash {words[word]}"
        else:
            messages = f"La palabra {word} no existe"

    return render_template('index.html', word_hashed=words, word_verify=messages)

if __name__ == "__main__":
    app.run(debug=True)