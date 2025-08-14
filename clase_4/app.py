#
from flask import Flask,render_template

#instancia de la libreia flask
app = Flask(__name__)

#decorador para el for loop
@app.route('/for-loop')
def forLoop():
    equipos = [
        "REAL MADRID",
        "FC BARCELONA",
        "MILAN AC",
        "LIVERPOOL",
        "BAYER MUNICH",
        "AJAX AMSTERD",
        "INTER MILAN",
        "JUVENTUS",
        "MANCHESTER UNITED",
        "OPORTO"
    ]
    equipos_cham = {
        "REAL MADRID": 14,
        "MILAN AC": 7,
        "BATER MUNICH": 6,
        "BARCELONA": 5,
        "AJAX AMSTERD": 4,
        "INTER MILAN": 3,
        "MANCHESTER UNITED": 3
    }
    return render_template('for.html', teams = equipos, teams_cham = equipos_cham)

if __name__ == '__main__':
    app.run()