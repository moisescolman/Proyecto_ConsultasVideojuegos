from flask import Flask, jsonify, request
from src.dbmethods import *


app = Flask(__name__)


# http://127.0.0.1:5000/api?console=PS4
@app.route('/api', methods=['GET'])
def get_games():
    console = request.args['console']
    result = get_consola_one(console)
    # for game in result:
    #     if game['console'] == console:
    #         result.append(game)
    return result

# http://127.0.0.1:5000/save?console=PS4&name=Grand%20Turismo%203
@app.route('/save', methods=['POST'])
def save_game():
    console= request.args['console']
    name= request.args['name']
    
    dicc = {
        "name": name,
        "console": console
    }
    return jsonify(dicc)

# Post con json
@app.route('/saveJSON', methods=['POST'])
def save_json():
    data = request.get_json()
    console= data['console']
    name= data['name']
    
    dicc = {
        "name": name,
        "console": console
    }
    return jsonify(dicc)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)