from flask import Flask, jsonify, request
from src.dbconsolas import *
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    # Renderiza el archivo index.html desde la carpeta 'templates'
    return render_template('index.html')


@app.route('/add_videojuego', methods=['GET', 'POST'])
def add_videojuego():
    # Your code to handle adding a video game
    return render_template('videojuego_form.html')  # or some other template

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



# @app.route('/save', methods=['POST'])
# def save_game():
#     console= request.args['console']
#     name= request.args['compay']
    
#     dicc = {
#         "name": name,
#         "console": console
#     }
#     return jsonify(dicc)

# Post con json
# @app.route('/saveJSON', methods=['POST'])
# def save_json():
#     data = request.get_json()
#     console= data['console']
#     name= data['name']
    
#     dicc = {
#         "name": name,
#         "console": console
#     }
#     return jsonify(dicc)

