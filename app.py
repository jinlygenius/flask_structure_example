# FLASK_ENV=development python -m flask run
from databases import influxdb, mongodb, mysqldb
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from logging.config import dictConfig
from routes import initialize_routes
from serializers import ma
import logging
import os
import settings


try:
    from log_settings import LOGGING
    dictConfig(LOGGING)
except Exception as e:
    pass
logger = logging.getLogger('app')


# ============= factory ================
def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    api = Api(app)
    api.init_app(app)
    # init influxdb client
    influxdb.init_app(app)
    # init mongodb
    # mongodb.init_app(app)
    # init mysqldb
    mysqldb.init_app(app)
    # init Marshmallow
    ma.init_app(app)
    # register resources
    initialize_routes(api)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)


# ============= singleton ================
# app = Flask(__name__)
# api = Api(app)

# api.add_resource(TodoList, '/todos')
# api.add_resource(Todo, '/todos/<todo_id>')

# if __name__ == '__main__':
#     app.run(debug=True)
