from flask import Flask
from my_API_app.routes import tasks_bp
from my_API_app.errors import errors_bp

app = Flask(__name__)

app.register_blueprint(tasks_bp)
app.register_blueprint(errors_bp)

if __name__ == "__main__":
    app.run(debug=True)