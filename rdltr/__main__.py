# source: http://docs.gunicorn.org/en/stable/custom.html
import multiprocessing
import os

from flask_migrate import upgrade
from waitress import serve

from rdltr import create_app

if not os.getenv('RDLTR_SETTINGS'):
    os.environ['RDLTR_SETTINGS'] = 'rdltr.config.ProductionConfig'
HOST = os.getenv('RDLTR_HOST', '0.0.0.0')
PORT = os.getenv('RDLTR_PORT', '5000')
BASEDIR = os.path.abspath(os.path.dirname(__file__))
app = create_app()


def upgrade_db():
    with app.app_context():
        upgrade(directory=BASEDIR + '/migrations')


def main():
    serve(app, host=HOST, port=PORT)


if __name__ == '__main__':
    main()
