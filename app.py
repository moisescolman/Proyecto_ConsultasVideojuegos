from src.webserver import app 
from src.dbmethods import init_db
#de src\webserver.py importa app

#app.run(debug=True);
#ejecuta app, con debugger

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
