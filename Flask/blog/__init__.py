from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize SQLAlchemy instance
db = SQLAlchemy()

# Define the name of the SQLite database file
DB_NAME = "blogDatabase.db"

# Function to create the Flask app
def create_app():
    app = Flask(__name__)

    # Set the secret key for session management
    app.config['SECRET_KEY'] = "meatballMaisie"
    
    # Set the URI for the SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    # Initialize the SQLAlchemy instance with the Flask app
    db.init_app(app)
    
    # Import and register the views blueprint
    from .views import views
    app.register_blueprint(views, url_prefix="/")
    
    # Import and register the auth blueprint
    from .auth import auth
    app.register_blueprint(auth, url_prefix="/")
    
    from .models import User, Post
    
    # Create the database if it doesn't exist
    create_database(app)

    # Set up Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

        
    return app

# Function to create the database
def create_database(app):
    # Check if the database file does not exist
    if not path.exists("blog/" + DB_NAME):
        # Use the application context to create all tables defined in the SQLAlchemy models
        with app.app_context():
            db.create_all()
        print("Database created successfully!")

    

