from flask import Flask, jsonify, request, render_template, redirect, url_for
from src.dbconsolas import *
from flask import Flask, render_template


app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_videojuego', methods=['GET', 'POST'])
def add_videojuego():
    if request.method == 'POST':
        titulo = request.form['titulo']
        genero = request.form['genero']
        consola_id = request.form['consola_id']
        desarrollador_id = request.form['desarrollador_id']
        anio = request.form['anio']

        insert_videojuego(titulo, consola_id, desarrollador_id)

        return render_template('videojuego_form.html', mensaje="¡Videojuego añadido!")
    
    return render_template('videojuego_form.html')


# http://127.0.0.1:5000/consola?name=Xbox One
@app.route('/consola', methods=['GET', 'POST', 'DELETE', 'PUT'])
def consoles_gp():
    if request.method == 'GET':
        console = request.args['name']
        result = get_consola_one(console)
        return result
    # http://127.0.0.1:5000/consola?name=Xbox Series X&company=Microsoft&year=2020
    elif request.method == 'POST':
        name = request.args['name']
        company = request.args['company']
        year = request.args['year']
        insert_consolas(name, company, year)
        return jsonify({"mensaje":"Consola añadida correctamente"})
    # http://127.0.0.1:5000/consola?id=16&name=Sega Dreamcast&company=Sega&year=1999
    elif request.method == 'PUT':
        id = request.args['id']
        name = request.args['name']
        company = request.args['company']
        year = request.args['year']
        update_consolas(id,name, company, year)
        return jsonify({"mensaje":"Consola modificada correctamente"})
    # http://127.0.0.1:5000/consola?name=Sega Dreamcast
    elif request.method == 'DELETE':
        name = request.args['name']
        delete_consolas(name)
        return jsonify({"mensaje":"Consola eliminada correctamente"})

# http://127.0.0.1:5000/consolas
@app.route('/consolas', methods=['GET'])
def consolas_all():
    result = get_consola_all()
    return jsonify(result)



