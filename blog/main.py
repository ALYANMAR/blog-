from infrastructure import database
from infrastructure.flask_app import app

if __name__ == "__main__":
    database.init_db()
    app.run(debug=True)