from flask import Flask
from controllers.solicitud_controller import solicitud_bp

app = Flask(__name__)
app.register_blueprint(solicitud_bp)

if __name__ == "__main__":
    app.run(port=5007, debug=True)
