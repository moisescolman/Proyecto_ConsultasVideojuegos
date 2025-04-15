import sqlite3
DB_PATH = f"videojuegos.db"


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
        CREATE TABLE IF NOT EXISTS generos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videojuegos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        id_consola INTEGER,
        id_genero INTEGER,
        FOREIGN KEY (id_consola) REFERENCES consolas(id),
        FOREIGN KEY (id_genero) REFERENCES generos(id)
        );
    ''')
    conn.commit()
    conn.close()