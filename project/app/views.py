from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for, abort
#from .forms import RegisterForm
from flask_login import login_user, logout_user, login_required , current_user#nos traemos el UserMixin
from .models import User, Task
#mandamos llamar la clase dentro de forms.py
from .forms import LoginForm , RegisterForm, TaskForm #mandamos llamar los forms por su clase
#Importamos las constantes
#from .consts import *
from .email import welcome_mail

#from .models import Task
from . import login_manager #importamos para el UserMixin

page = Blueprint('page', __name__)

#decoramos la funcion para obtner el id de session
@login_manager.user_loader
def load_user(id):
    return User.get_by_id(id)

@page.app_errorhandler(404)
def page_not_found(error):
    title='Error 404'
    print('Estas en Pagina de error 404')
    return render_template('errors/404.html', title=title), 404

@page.route('/logout')
def logout():
    logout_user()
    print('LOGOUT')
    flash('cerraste session exitosamente')
    return redirect(url_for('.login'))

@page.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: #si el usuario es authenticado
        return redirect(url_for('.task'))#redirige ala funcion task
    form = LoginForm(request.form) #Instanciamos la clase en una variable
    if request.method == 'POST' and form.validate():
        user = User.get_by_username(form.username.data)
        passed = user.verify_password(form.password.data)
        if user and passed:#valida el usuario y el password 
            login_user(user)
            print(login_user(user))
            flash('Usuario Authenticado Correctamente')
        else:
            flash('Usuario o Password Invalidos', 'error')
            print(user)
    return render_template('auth/login.html', title='Login', form=form ,active='login')

@page.route('/register' , methods=['GET','POST'])
@login_required
def register():
    #if current_user.is_authenticated: #si el usuario es authenticado
    #    return redirect(url_for('.task'))
    form = RegisterForm(request.form) #manda a allmar la clase registerform dentro de forms.py
    if request.method == 'POST':
        if form.validate():
            user = User.create_element(form.username.data, form.password.data, form.email.data)
            flash('Usuario Registrado Exitosamente')
            login_user(user)
            welcome_mail(user)
            print(user.id)
            print(user.email)
    return render_template('auth/register.html' , title='Registro', form=form, active='register')

@page.route('/tasks')
@login_required
def task(page=1, per_page=2):
    tasks = current_user.tasks #con esto me muestra todas las tareas sin paginacion
    #pagination = current_user.tasks.paginate(page, per_page=per_page)
    #tasks = pagination.items
    #return render_template('task/list.html', title='Tareas', tasks=tasks,
                                            #pagination=pagination,page=page)
    return render_template('task/list.html', title='Tareas', tasks=tasks, active='task')

@page.route('/tasks/new', methods=['GET','POST'])
@login_required
def task_new():
    form = TaskForm(request.form)
    #print(user.id)
    if request.method == 'POST' and form.validate():
        task = Task.create_element(form.title.data, form.description.data, current_user.id)
        if task:
            flash('TASK_CREATED')
            print(task.id)
    return render_template('task/new.html', title='Tareas', form=form, active='task_new')

@page.route('/tasks/edit/<int:task_id>', methods=['GET','POST'])
@login_required
def task_edit(task_id):
    print('estas en task edit')
    task = Task.query.get_or_404(task_id)#busca el id si noexiste manda la pagina 404
    if task.user_id != current_user.id:  #busca el id de usuario que pertenezca al usurio
        abort(404)
    form = TaskForm(request.form , obj=task) #llenamos el form con el obejto task
    if request.method == 'POST' and form.validate():
        print('ya paso el metodo post')
        task = Task.update_element(task.id, form.title.data, form.description.data)
        if task:
            flash('Se ha actualizado Correctamente')
    return render_template('task/edit.html', title='editar tarea', form=form, active='task_edit')

@page.route('/tasks/delete/<int:task_id>',methods=['GET','POST'])
@login_required
def delete_task(task_id):
    print('estas en delete')
    task = Task.query.get_or_404(task_id)#busca el id si noexiste manda la pagina 404
    print(task.id)
    if task.user_id != current_user.id:  #busca el id de usuario que pertenezca al usurio
        abort(404)
        form = TaskForm(request.form)
        if request.method == 'GET':
            task = Task.delete_element(task.id)
            if task:
                flash('TASK_DELETED')
            else:
                flash('Error al eliminar la tarea')
    return redirect(url_for('.task'))

@page.route('/tasks/show/<int:task_id>')
@login_required
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template('task/show.html', title='Tareas', task=task)

@page.route('/')
def index():
    print('Estas en layout')
    return render_template('layout.html',title='Index', active='index')

@page.before_request
def before_request():
   print('antes de la peticion before_request')

@page.after_request
def after_request(response):
    print('despues de la peticion after_request')
    return response

@page.route('/about')
def about():
    print("estamos en el About")
    title = "Acerca de.."
    return render_template('about.html', title=title, active='about')

#crear ruta con variables en url
#http://localhost:9000/usuario/sergio/morales/38
@page.route('/usuario/<name>/<last_name>/<int:age>')#String
def usuario(last_name, name, age):
   print("estamos en el Usuario")
   return 'Hola ' + last_name + ' ' + name + ' ' + str(age)

#Metdodo GET
#http://localhost:9000/datos?nombre=Codi&curso=python_web
@page.route('/datos')
def datos():
    print("estamos en los Datos")
    nombre = request.args.get('nombre' , '') #Diccionario
    curso  = request.args.get('curso' , '')
    return 'listado de Datos:' + nombre + ' curso:' + curso
