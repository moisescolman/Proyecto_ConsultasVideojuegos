from flask import Flask, jsonify, request, render_template, redirect  # Add redirect here
from src.dbconsolas import get_consola_all, get_consola_one, insert_consolas, update_consolas, delete_consolas
from src.dbvideojuegos import get_videojuegos, insert_videojuego, get_desarrolladores

app = Flask(__name__)

@app.route('/')
def index():
    # Render the index page (make sure index.html exists in the templates folder)
    return render_template('index.html')

@app.route('/consola', methods=['GET', 'POST', 'PUT', 'DELETE'])
def consoles_gp():
    if request.method == 'GET':
        # Getting a specific console by name
        console = request.args.get('name')
        result = get_consola_one(console)
        return result
    
    elif request.method == 'POST':
        # Adding a new console
        name = request.form['name']  # Using form data for POST
        company = request.form['company']
        year = request.form['year']
        insert_consolas(name, company, year)
        return jsonify({"mensaje": "Consola añadida correctamente"})
    
    elif request.method == 'PUT':
        # Updating an existing console
        id = request.form['id']
        name = request.form['name']
        company = request.form['company']
        year = request.form['year']
        update_consolas(id, name, company, year)
        return jsonify({"mensaje": "Consola modificada correctamente"})
    
    elif request.method == 'DELETE':
        # Deleting a console
        name = request.args.get('name')
        delete_consolas(name)
        return jsonify({"mensaje": "Consola eliminada correctamente"})

@app.route('/consolas', methods=['GET'])
def consolas_all():
    # Get all consoles
    result = get_consola_all()
    return jsonify(result)

@app.route('/nuevo_videojuego', methods=['GET', 'POST'])
def nuevo_videojuego():
    if request.method == 'POST':
        # Adding a new video game
        titulo = request.form['titulo']
        genero = request.form['genero']
        id_consola = request.form['id_consola']
        id_desarrollador = request.form['id_desarrollador']
        insert_videojuego(titulo, genero, id_consola, id_desarrollador)
        return redirect('/videojuegos')  # Redirect to the list of video games after POST
    
    # Get list of consoles and developers to show in the form
    consolas = get_consola_all()
    desarrolladores = get_desarrolladores()
    return render_template('videojuego_form.html', consolas=consolas, desarrolladores=desarrolladores)

@app.route('/videojuegos')
def videojuegos():
    # Get all video games
    lista = get_videojuegos()
    return render_template('lista_videojuegos.html', videojuegos=lista)

if __name__ == "__main__":
    app.run(debug=True)
