from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["TESTING"] = True  # Enable testing mode
    app.config["SECRET_KEY"] = "your-secret-key"  # Required for session

    # Register routes


    @app.route("/")
    def root():
       return {}