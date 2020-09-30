from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,login_manager
from flask_admin import Admin,AdminIndexView
from flask_admin .contrib.sqla import ModelView

class schools(db.Model):
    __