# An example of a flask project
When I wanted to start a flask project, I was quite confused how to organize the code (comparing to Django's out-of-the-box structure). After some tries, I found

 - Put databases to 'databases' module, and initiated a db handler in each file. Registered them ('init_app') in app by importing those db handlers from the module. DB handlers were also imported to models. This structure could prevent an incursive importing.
 - For the same reason, initiated a Marshmallow instance, and registered it in app.
 - Put all routes in the routes file - this was much clearer than writing them directly in app


# project
using python3

## Install dependencies
pip install -r requirements.txt

## Run local dev server
FLASK_ENV=development python -m flask run --host=0.0.0.0

## Run production
gunicorn -w 4 -b 0.0.0.0:5000 -k gevent "wsgi:create_app()"

## Migrate
python manage.py db init

python manage.py db migrate

python manage.py db upgrade

## Run flask shell
FLASK_ENV=development python -m flask shell
