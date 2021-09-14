from flask import Flask
from flask_cors import CORS
from pfrf.pfrf_bootstrap import Bootstrap


app = Flask(__name__)
pfrf_bootstrap = Bootstrap()
pfrf_bootstrap.load_app(app)

CORS(app, resources={
    r"/api/*": {"origins": "*", "Access-Control-Allow-Origin": "*"},
    r"/static/*": {"origins": "*", "Access-Control-Allow-Origin": "*"}
})


if __name__ == '__main__':
    app.run()
