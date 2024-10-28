from flask import Flask
from app import db
from app.routes import configure_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'  # Use your correct database URI here
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Configure routes
configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
