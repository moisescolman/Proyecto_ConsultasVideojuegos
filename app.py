from src.webserver import app
from src.dbconsolas import init_db

if __name__ == "__main__":
    init_db()  # Si tienes que inicializar la base de datos
    app.run(host='0.0.0.0', port=50001, debug=True)  
