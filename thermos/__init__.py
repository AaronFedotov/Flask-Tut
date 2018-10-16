import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

#Configure database
app.config['SECRET_KEY'] = 't\x12\xd0\xb7\xab-^g\xc1\xeb\xbc\x0b\xc4\x8e\x1d\xc1G\xffM>\xcd^}\x9f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config['DEBUG'] = False
db = SQLAlchemy(app)

#Configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(app)

#enable debug toolbar
toolbar = DebugToolbarExtension(app)

#For displaying timestamps
moment = Moment(app)


from thermos import models
from thermos import views


if __name__ == '__main__':
	app.run()
