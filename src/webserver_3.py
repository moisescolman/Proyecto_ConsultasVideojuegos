from flask import Flask, jsonify, request
from src.dbvideojuegos import *


app = Flask(__name__)



@app.route('/juego', methods=['GET', 'POST', 'DELETE', 'PUT'])
def juegos_gp():
    # http://127.0.0.1:5000/juego?name=Grand Theft Auto V&console=5
    if request.method == 'GET':
        juego = request.args['name']
        consola = request.args['console']
        result = get_juego_one(juego, consola)
        return result
    # http://127.0.0.1:5000/juego?name=Need For Speed Porshe Unleashed&console=1&gender=Carreras&dev=25
    elif request.method == 'POST':
        name = request.args['name']
        console = request.args['console']
        gender = request.args['gender']
        developer = request.args['dev']
        insert_videojuego(name, gender, console, developer)
        return jsonify({"mensaje":"Videojuego añadido correctamente"})
    # http://127.0.0.1:5000/juego?name=Need For Speed Porshe Unleashed&console=1&gender=Carreras&dev=25
    elif request.method == 'PUT':
        id = request.args['id']
        name = request.args['name']
        console = request.args['console']
        gender = request.args['gender']
        developer = request.args['dev']
        update_videojuego(id, name, console, gender, developer)
        return jsonify({"mensaje":"Videojuego modificado correctamente"})
    # http://127.0.0.1:5000/juego?id=63
    elif request.method == 'DELETE':
        id = request.args['id']
        delete_consolas(name)
        return jsonify({"mensaje":"Consola eliminada correctamente"})

# http://127.0.0.1:5000/juegos
@app.route('/juegos', methods=['GET'])
def juegos_all():
    result = get_all_juegos()
    return jsonify(result)




