from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import app as my_app


app = my_app.create_app()
manager = Manager(app)
Migrate(app, my_app.mysqldb)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()