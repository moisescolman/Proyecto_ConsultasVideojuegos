# from src.webserver import app
from src.webserver_3 import app
from src.createdb import init_db

if __name__ == "__main__":
    init_db()  
    app.run(host='0.0.0.0', port=5000, debug=True)  
