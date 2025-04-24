from flask import jsonify
import sqlite3
DB_PATH = f"videojuegos.db"


# OBTENER GENERO INDIVIDUAL
def get_genero(genero):
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    sql = f'SELECT * FROM generos WHERE id = "{genero}"'
    cursor.execute(sql)
    genre = cursor.fetchone()
    conn.close()
    print(genre)
    result = {
        "id":genre[0],
        "genero":genre[1],
    }
    return jsonify(result)   

# OBTENER TODOS LOS GÉNEROS
def get_generos_all():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    sql = 'SELECT * FROM generos'
    cursor.execute(sql)
    filas = cursor.fetchall()
    conn.close()
    keys = ['id', 'nombre']
    generos = [dict(zip(keys, row)) for row in filas]
    return generos

# AÑADIR genero a la db
def insert_genero(name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO generos (nombre) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    
# ACTUALIZAR genero en la db
def update_genero(id, name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('UPDATE generos SET nombre = ? WHERE id = ?', (name, id))
    conn.commit()
    conn.close()
    
# BORRAR genero
def delete_genero(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM generos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
