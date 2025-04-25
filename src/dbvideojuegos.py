from flask import jsonify
import sqlite3
DB_PATH = f"videojuegos.db"


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
        "id_consola": juego[2],
        "id_genero": juego[3]
    }
    return jsonify(result)

# 
def get_all_juegos():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    sql = 'SELECT * FROM videojuegos'
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    keys = ['id', 'titulo', 'genero', 'id_consola', 'id_genero']
    juegos = [dict(zip(keys, row)) for row in rows]
    return juegos


# AÑADIR VIDEOJUEGO A LA BASE DE DATOS
def insert_videojuego(title, genre_id, console_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO videojuegos (titulo, id_consola, id_genero) VALUES (?, ?, ?)',
            (title, console_id, genre_id)
        )
        conn.commit()
    except sqlite3.IntegrityError as e:
        conn.rollback()
        return jsonify({"error": "Error de integridad: clave foránea no válida.", "details": str(e)}), 400
    finally:
        conn.close()
    return jsonify({"mensaje": "Videojuego insertado correctamente"}), 201
    
# ACTUALIZAR videojuego en db
def update_videojuego(id, name, console, genre):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('UPDATE videojuegos SET titulo = ?, id_genero = ?, id_consola = ? WHERE id = ?', (name, genre, console, id))
    conn.commit()
    conn.close()
    
# BORRAR consolas db
def delete_videojuego(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM videojuegos WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    
    
######################################
# MÉTODOS PARA TEMPLATES


def get_all_juegos_completo():
    """
    Devuelve una lista de dicts con:
      id, titulo, genero, consola, anio (año de la consola)
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT
            v.id,
            v.titulo,
            g.nombre   AS genero,
            c.nombre   AS consola,
            c.anio     AS anio
        FROM videojuegos v
        LEFT JOIN generos    g ON v.id_genero  = g.id
        LEFT JOIN consolas   c ON v.id_consola = c.id
        ORDER BY v.titulo
    ''')
    rows = cursor.fetchall()
    conn.close()

    keys = ['id', 'titulo', 'genero', 'consola', 'anio']
    return [dict(zip(keys, row)) for row in rows]

def get_juego_by_id(juego_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        'SELECT id, titulo, id_genero, id_consola FROM videojuegos WHERE id = ?',
        (juego_id,)
    )
    row = cursor.fetchone()
    conn.close()
    if row is None:
        return None
    return {
        "id":           row[0],
        "titulo":       row[1],
        "genero_id":    row[2],
        "consola_id":   row[3]
    }
