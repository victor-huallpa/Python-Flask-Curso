#

from flask import Flask, render_template

app = Flask(__name__)

cards = [
    {"title": "Biografia", "content": " <p>esta es una breve biografia del usuario...</p> "},
    {"title": "Proyectos", "content": " <ul><li>Proyecto 1</li><li>Proyecto 2</li><li>Proyecto 3</li></ul> "},
    {"title": "Contacto", "content": " <p>Email: user@gmail.com</p><p>Address: Jr Abancay n 123</p> "},
]
@app.route('/')
def home():

    return render_template('index.html', cards = cards)
if __name__ == "__main__":
    app.run()