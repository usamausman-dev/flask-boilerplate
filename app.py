# app.py
from flask import Flask
from flask_cors import CORS
from routes.example_routes import example_bp

# Initialize Flask app
app = Flask(__name__)
CORS(app)



# Registering Blueprints (similar to setting up routes in Express)
app.register_blueprint(example_bp, url_prefix='/api')

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
