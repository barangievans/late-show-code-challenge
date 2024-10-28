from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Step 1: Initialize Flask app
app = Flask(__name__)

# Step 2: Configure the database URI (Update this to your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database_name.db'  # Change as needed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, but recommended

# Step 3: Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Step 4: Import your models here to avoid circular imports
from .models import Episode, Guest, Appearance # Make sure this import is correct

# Step 5: Import routes or any other necessary modules after initializing the app and db
# from .routes import your_routes_here  # Uncomment and adjust if you have routes
