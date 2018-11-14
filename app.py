
#########################################################

## new flask instance
from flask import Flask
app = Flask(__name__)

## intergate config.py file 
from config import Config
app.config.from_object(Config)

## db binding 
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

## db migrate config
from flask_migrate import Migrate
migrate = Migrate(app, db)

## intergate models.py file
from models import Todo

## flask-admin instance 
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
admin = Admin(app, name='Admin', template_mode='bootstrap3')
### adding views for db tables
admin.add_view(ModelView(Todo, db.session))

## flask-bootstrap
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

## flask shell config
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Todo': Todo}

#########################################################
# view content

from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello_world():
    print(app.url_map)
    return 'Hello, World!'

#########################################################
