#conexion a mongodb 
import os
from flask import render_template, request, Flask
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")

app = Flask(__name__)
#conectar a mongo
cliente = MongoClient(mongo_uri)

app.db = cliente.ejemplo

# usuarios = [] #se usa en caso se quiera guradar en una lista
#lista para resivir los usuarios de mongo
usuarios = [usuario for usuario in app.db.usuarios.find({})]#extraemos los datos de mongodb
print(usuarios)

#decorador
@app.route("/", methods = ['GET', "POST"])
def home():
    #verificamos si existe un meto post enviado
    if request.method == "POST":
        infor_nombre = request.form.get("nombre")#se trae el dato ingresad oen l formular
        parametros = {"nombre":infor_nombre}#se alamcena la informaicon en un diccionario
        usuarios.append(parametros)#se guarda en la lista los diccionartios creados
        app.db.usuarios.insert_one(parametros)#insertamos los datos a mongo d
        print(usuarios)
        # print (infor_nombre)
    return render_template("formulario.html", usuarios = usuarios)

if __name__ == '__main__':
    app.run()