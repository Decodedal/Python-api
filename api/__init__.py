
from flask import Flask 
from dotenv import load_dotenv
import os
from flask_migrate import Migrate

load_dotenv()

def create_app(): 
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("PG_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello(): 
        return 'Hello, snake api!'

    #register blueprint
    from . import snake
    app.register_blueprint(snake.bp)
   

    return app
