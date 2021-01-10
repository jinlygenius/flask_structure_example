# deploy production
# gunicorn -w 4 -b 0.0.0.0:5000 -k gevent "wsgi:create_app()"

from app import create_app

app = create_app()
