from flask import Flask #libreria para levantar servidor
from flask import render_template, request

app = Flask(__name__)

@app.before_request
def before_request():
    print('antes de la peticion before_request')

@app.after_request
def after_request(response):
    print('despues de la peticion after_request')
    return response

#es el index principal
@app.route('/')
def index():
    print("estamos en el Index")
    name = 'Codi'
    title = "Index.."
    apellido = 'Morales'
    curso='Python Web'
    is_premium=False
    courses = ['Python' , 'C++' , 'Visual Basic' , 'C#']
    #return "<h1>Hola desde el servidor Python Flask!</h1>"
    return render_template('index.html',name=name,
                            title=title,
                            apellido=apellido,
                            curso=curso,
                            is_premium=is_premium,
                            courses=courses)

@app.route('/about')
def about():
    print("estamos en el About")
    title = "Acerca de.."
    return render_template('about.html', title=title)

#crear ruta con variables en url
#http://localhost:9000/usuario/sergio/morales/38
@app.route('/usuario/<name>/<last_name>/<int:age>')#String
def usuario(last_name, name, age):
   print("estamos en el Usuario")
   return 'Hola ' + last_name + ' ' + name + ' ' + str(age)

#http://localhost:9000/datos?nombre=Codi&curso=python_web
@app.route('/datos')
def datos():
    print("estamos en los Datos")
    nombre = request.args.get('nombre' , '') #Diccionario
    curso = request.args.get('curso' , '')
    return 'listado de Datos:' + nombre + ' curso:' + curso

if __name__ == '__main__':
    app.run(debug=True, port=9000)#Activamos debug y puerto
