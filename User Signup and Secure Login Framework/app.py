from flask import Flask
from flask_cors import CORS
from models import db  # Import the db instance from models
from routes import init_routes

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Use the db instance from models

# Create database tables within an application context
with app.app_context():
    db.create_all()

# Register routes
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
