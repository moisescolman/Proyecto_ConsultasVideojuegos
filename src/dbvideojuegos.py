from flask import jsonify
import sqlite3
DB_PATH = f"gamesdb.db"


# Get juego INDIVIDUAL
def get_juego_one(name, console):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM videojuegos WHERE titulo = ? AND id_consola = ?', (name, console))
    juego = cursor.fetchone()
    conn.close()
    if juego is None:
        return jsonify({"error": "Videojuego no encontrado"}), 404
    result = {
        "id": juego[0],
        "titulo": juego[1],
        "genero": juego[2],
        "id_consola": juego[3],
        "id_desarrollador": juego[4]
    }
    return jsonify(result)


def get_all_juegos():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    sql = 'SELECT * FROM videojuegos'
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    keys = ['id', 'titulo', 'genero', 'id_consola', 'id_desarrollador']
    juegos = [dict(zip(keys, row)) for row in rows]
    print(juegos)
    return juegos


# AÑADIR consola a la db
def insert_consolas(name, company, year):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO consolas (nombre, fabricante, anio) VALUES (?, ?, ?)', (name, company, year))
    conn.commit()
    conn.close()
    
# ACTUALIZAR consola a la db
def update_consolas(id, name, company, year):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('UPDATE consolas SET nombre = ?, fabricante = ?, anio = ? WHERE id = ?', (name, company, year, id))
    conn.commit()
    conn.close()
    
# BORRAR consolas db
def delete_consolas(consola):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM consolas WHERE nombre = ?', (consola,))
    conn.commit()
    conn.close()

    
    
# # Get todos las consolas desde db
# def get_consolas():
#     conn=sqlite3.connect(DB_PATH)
#     cursor=conn.cursor()
#     cursor.execute('SELECT * FROM consolas')
#     consolas = cursor.fetchall()
#     conn.close()
#     print(consolas)
#     return consolas   
    
# # Get todos los desarrolladores desde db
# def get_desarrolladores():
#     conn=sqlite3.connect(DB_PATH)
#     cursor=conn.cursor()
#     cursor.execute('SELECT * FROM desarrolladores')
#     desarrolladores = cursor.fetchall()
#     conn.close()
#     print(desarrolladores)
#     return desarrolladores

# # Get todos los videojuegos desde db
# def get_videojuegos():
#     conn=sqlite3.connect(DB_PATH)
#     cursor=conn.cursor()
#     cursor.execute('SELECT * FROM videojuegos')
#     videojuegos = cursor.fetchall()
#     conn.close()
#     print(videojuegos)
#     return videojuegos



# # Añadir desarrolladores a la db
# def add_user(name, country):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute('INSERT INTO desarrolladores (nombre, pais) VALUES (?, ?)', (name, country))
#     conn.commit()
#     conn.close()

# # Añadir videojuegos a la db
# def add_user(title, gender, console_id, dev_id):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute('INSERT INTO desarrolladores (titulo, genero, id_consola, id_desarrollador) VALUES (?, ?)', (title, gender, console_id, dev_id))
#     conn.commit()
#     conn.close()

# # ACTUALIZAR consola a la db
# def add_consolas(id, name, company, year):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute('UPDATE consolas SET nombre = ?, fabricante = ?, anio = ? WHERE id = ?', (name, company, year, id))
#     conn.commit()
#     conn.close()

# # ACTUALIZAR desarrolladores a la db
# def add_desarrolladores(id, name, country):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute('UPDATE desarrolladores SET nombre = ?, pais = ? WHERE id = ?', (name, country, id))
#     conn.commit()
#     conn.close()

# # ACTUALIZAR videojuegos a la db
# def add_videojuegos(id, title, gender, console_id, dev_id):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute('UPDATE videojuegos SET titulo = ?, genero = ? , id_consola = ?, id_desarrollador = ? WHERE id = ?', (title, gender, console_id, dev_id, id))
#     conn.commit()
#     conn.close()


    
# # borrar consolas db
# def delete_consolas(id):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute('DELETE FROM consolas WHERE id = ?', (id,))
#     conn.commit()
#     conn.close()

    
# # borrar desarrolladores db
# def delete_desarrolladores(id):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute('DELETE FROM desarrolladores WHERE id = ?', (id,))
#     conn.commit()
#     conn.close()
    
# # borrar videojuegos db
# def delete_videojuegos(id):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute('DELETE FROM videojuegos WHERE id = ?', (id,))
#     conn.commit()
#     conn.close()