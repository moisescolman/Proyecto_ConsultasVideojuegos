from flask import jsonify
import sqlite3
DB_PATH = f"gamesdb.db"


# Configuracion db
def init_db():
    conn =sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS consolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            fabricante TEXT,
            anio INTEGER
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS desarrolladores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            pais TEXT
        );
    ''')

    cursor.execute('''
       CREATE TABLE IF NOT EXISTS videojuegos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    genero TEXT,
    id_consola INTEGER,
    id_desarrollador INTEGER,
    FOREIGN KEY (id_consola) REFERENCES consolas(id),
    FOREIGN KEY (id_desarrollador) REFERENCES desarrolladores(id)
);

    ''')
    conn.commit()
    conn.close()


# Get consola INDIVIDUAL

def insert_videojuego(titulo, genero, consola_id, desarrollador_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    sql = """
        INSERT INTO videojuegos (titulo, genero, id_consola, id_desarrollador)
        VALUES (?, ?, ?, ?)
    """
    cursor.execute(sql, (titulo, genero, consola_id, desarrollador_id))
    conn.commit()
    conn.close()




def get_consola_one(consola):
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    print(consola)
    sql = f'SELECT * FROM consolas WHERE nombre = "{consola}"'
    cursor.execute(sql)
    consolas = cursor.fetchall()
    conn.close()
    print(consolas)
    print(consolas[0][1])
    result = {
        "id":consolas[0][0],
        "nombre":consolas[0][1],
        "fabricante":consolas[0][2],
        "año":consolas[0][3]
    }
    return jsonify(result)   

def get_consola_all():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    sql = 'SELECT * FROM consolas'
    cursor.execute(sql)
    consolas = cursor.fetchall()
    conn.close()

    # Convertimos la lista de tuplas a lista de diccionarios
    result = [
        {
            "id": fila[0],
            "nombre": fila[1],
            "fabricante": fila[2],
            "año": fila[3]
        }
        for fila in consolas
    ]
    return result

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