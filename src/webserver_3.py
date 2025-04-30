from flask import Flask, jsonify, request, render_template, redirect, url_for
from src.dbvideojuegos import *
from src.dbconsolas import *
from src.dbgeneros import *


app = Flask(__name__, template_folder='../templates')

#############################################
# RUTAS PARA JUEGOS
############################################

@app.route('/juego', methods=['GET', 'POST', 'DELETE', 'PUT'])
def juegos_gp():
    # http://127.0.0.1:5000/juego?name=FIFA 23&console=5
    if request.method == 'GET':
        name = request.args['name']
        consola = request.args['console']
        result = get_juego_one(name, consola)
        return result, 200
    
    # http://127.0.0.1:5000/juego?name=GTA V&console=5&genre=5
    elif request.method == 'POST':
        name = request.args['name']
        console = request.args['console']
        genre = request.args['genre']
        insert_videojuego(name, genre, console)
        return jsonify({"mensaje":"Videojuego añadido correctamente"}) , 201
    
    # http://127.0.0.1:5000/juego?id=32&name=GTA V&console=5&genre=1
    elif request.method == 'PUT':
        id = request.args['id']
        name = request.args['name']
        console = request.args['console']
        genre = request.args['genre']
        update_videojuego(id, name, console, genre)
        return jsonify({"mensaje":"Videojuego modificado correctamente"}), 200
    
    # http://127.0.0.1:5000/juego?id=31 
    elif request.method == 'DELETE':
        id = request.args['id']
        delete_videojuego(id)
        return jsonify({"mensaje":"Videojugo eliminado correctamente"}), 200

# http://127.0.0.1:5000/juegos
@app.route('/juegos', methods=['GET'])
def juegos_all():
    result = get_all_juegos()
    return jsonify(result), 200


@app.route('/juego', methods=['PATCH'])
def patch_juego():
    data = request.get_json()
    if not data or 'id' not in data:
        return jsonify({"error": "Se requiere el campo 'id'"}), 400
    juego_id = data['id']
    if get_juego_by_id(juego_id) is None:
        return jsonify({"error": "Videojuego no encontrado"}), 404
    name = data.get('name')
    console = data.get('console')
    genre = data.get('genre')
    return partial_update_videojuego(juego_id, name=name, console=console, genre=genre)


#############################################
# RUTAS PARA JUEGOS FRONT
############################################

@app.route('/')
def index():
    sort_by = request.args.get('sort_by', 'id')
    order   = request.args.get('order',   'asc')
    juegos = get_all_juegos_completo()
    if sort_by in ('id','titulo','consola','genero'):
        juegos.sort(key=lambda x: x[sort_by], reverse=(order=='desc'))
    return render_template('index.html',
                           juegos=juegos,
                           sort_by=sort_by,
                           order=order)

# agregar videojuego
@app.route('/add_videojuego', methods=['GET','POST'])
def add_videojuego():
    generos  = get_generos_all()
    consolas = get_consola_all()
    if request.method == 'POST':
        insert_videojuego(
            request.form['titulo'],
            request.form['genero'],
            request.form['consola_id']
        )
        mensaje = "✅ Videojuego añadido correctamente"
        return render_template('videojuego_form.html',
                               generos=generos,
                               consolas=consolas,
                               mensaje=mensaje)
    return render_template('videojuego_form.html',
                           generos=generos,
                           consolas=consolas)

#  editar videojuego 
@app.route('/edit_videojuego/<int:juego_id>', methods=['GET','POST'])
def edit_videojuego(juego_id):
    generos  = get_generos_all()
    consolas = get_consola_all()
    juego = get_juego_by_id(juego_id)
    if juego is None:
        return redirect(url_for('index'))
    if request.method == 'POST':
        update_videojuego(
            juego_id,
            request.form['titulo'],
            request.form['consola_id'],
            request.form['genero']
        )
        return redirect(url_for('index'))
    
    return render_template('videojuego_edit_form.html',
                           generos=generos,
                           consolas=consolas,
                           juego=juego)

#  borrar videojuego 
@app.route('/delete_videojuego/<int:juego_id>', methods=['POST'])
def delete_videojuego_route(juego_id):
    delete_videojuego(juego_id)
    return redirect(url_for('index'))

#############################################
# RUTAS PARA CONSOLAS
############################################

# http://127.0.0.1:5000/consola?name=Xbox One
@app.route('/consola', methods=['GET', 'POST', 'DELETE', 'PUT'])
def consoles_gp():
    if request.method == 'GET':
        console = request.args['name']
        result = get_consola_one(console)
        return result, 200
    
    # http://127.0.0.1:5000/consola?name=Atari 2600&company=Atari&year=1977
    elif request.method == 'POST':
        name = request.args['name']
        company = request.args['company']
        year = request.args['year']
        insert_consolas(name, company, year)
        return jsonify({"mensaje":"Consola añadida correctamente"}), 201
    
    # http://127.0.0.1:5000/consola?id=14&name=Atari 2600&company=Atari&year=1978
    elif request.method == 'PUT':
        id = request.args['id']
        name = request.args['name']
        company = request.args['company']
        year = request.args['year']
        update_consolas(id,name, company, year)
        return jsonify({"mensaje":"Consola modificada correctamente"}), 200
    
    # http://127.0.0.1:5000/consola?name=Atari 2600
    elif request.method == 'DELETE':
        name = request.args['name']
        delete_consolas(name)
        return jsonify({"mensaje":"Consola eliminada correctamente"}), 200

# http://127.0.0.1:5000/consolas
@app.route('/consolas', methods=['GET'])
def consolas_all():
    result = get_consola_all()
    return result, 200


#############################################
# RUTAS PARA GENEROS
############################################

# http://127.0.0.1:5000/generos
@app.route('/generos', methods=['GET'])
def generos_all():
    result = get_generos_all()
    return jsonify(result),200

@app.route('/genero', methods=['GET', 'POST', 'DELETE', 'PUT'])
def generos_crud():
    # http://127.0.0.1:5000/genero?id=4
    if request.method == 'GET':
        id = request.args['id']
        result = get_genero(id)
        return result, 200
    
    # http://127.0.0.1:5000/genero?genre=nombregenero
    elif request.method == 'POST':
        genero = request.args['genre']
        insert_genero(genero)
        return jsonify({"mensaje":"Género añadido correctamente"}), 201
    
    # http://127.0.0.1:5000/genero?id=32&genre=ejemplo
    elif request.method == 'PUT':
        id = request.args['id']
        genero = request.args['genre']
        update_genero(id, genero)
        return jsonify({"mensaje":"Género modificado correctamente"}), 200
    
    # http://127.0.0.1:5000/genero?id=32
    elif request.method == 'DELETE':
        id = request.args['id']
        delete_genero(id)
        return jsonify({"mensaje":"Género eliminado correctamente"}), 200
