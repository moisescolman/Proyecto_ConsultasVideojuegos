from flask import jsonify
import sqlite3
DB_PATH = f"videojuegos.db"



def get_consola_one(consola):
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    print(consola)
    sql = f'SELECT * FROM consolas WHERE nombre = "{consola}"'
    cursor.execute(sql)
    consolas = cursor.fetchall()
    conn.close()
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

