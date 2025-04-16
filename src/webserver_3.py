from flask import Flask, jsonify, request, render_template
from src.dbvideojuegos import *
from src.dbconsolas import *


app = Flask(__name__, template_folder='../templates')



@app.route('/juego', methods=['GET', 'POST', 'DELETE', 'PUT'])
def juegos_gp():
    # http://127.0.0.1:5000/juego?name=Grand Theft Auto V&console=5
    if request.method == 'GET':
        name = request.args['name']
        consola = request.args['console']
        result = get_juego_one(name, consola)
        return result
    # http://127.0.0.1:5000/juego?name=Need For Speed Porshe Unleashed&console=1&genre=7
    elif request.method == 'POST':
        name = request.args['name']
        console = request.args['console']
        genre = request.args['genre']
        insert_videojuego(name, genre, console)
        return jsonify({"mensaje":"Videojuego añadido correctamente"})
    # http://127.0.0.1:5000/juego?id=31&name=Need For Speed Porshe Unleashed&console=2&genre=7
    elif request.method == 'PUT':
        id = request.args['id']
        name = request.args['name']
        console = request.args['console']
        genre = request.args['genre']
        update_videojuego(id, name, console, genre)
        return jsonify({"mensaje":"Videojuego modificado correctamente"})
    # http://127.0.0.1:5000/juego?id=31 
    elif request.method == 'DELETE':
        id = request.args['id']
        delete_videojuego(id)
        return jsonify({"mensaje":"Consola eliminada correctamente"})

# http://127.0.0.1:5000/juegos
@app.route('/juegos', methods=['GET'])
def juegos_all():
    result = get_all_juegos()
    return jsonify(result)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_videojuego', methods=['GET', 'POST'])
def add_videojuego():
    if request.method == 'POST':
        titulo = request.form['titulo']
        genero = request.form['genero_id']
        consola= request.form['consola_id']
        insert_videojuego(titulo, genero, consola)
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



