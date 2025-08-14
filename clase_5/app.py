from flask import render_template, request, Flask

app = Flask(__name__)

#decorador
@app.route("/", methods = ['GET', "POST"])
def home():
    infor_nombre = ""
    #verificamos si existe un meto post enviado
    if request.method == "POST":
        infor_nombre = request.form.get("nombre")
        # print (infor_nombre)
    return render_template("formulario.html", nombre = infor_nombre)

if __name__ == '__main__':
    app.run()