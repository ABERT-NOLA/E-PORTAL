from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,login_manager
from flask_admin import Admin,AdminIndexView
from flask_admin .contrib.sqla import ModelView
from flask_security import UserMixin,RoleMixin

class schools(db.Model):
    __tablename__ = 'schools'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    admin_id = db.Column(db.Integer,db.foreignkey('admin.id'))
    def __repr__(self):
        return f'User {self.username}'

class facilitator(db.Model):
    __tablename__ = 'Facilitator'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    schools = db.relationship('schools',backref = 'admin',lazy ='dynamic')
    def __repr__(self):
        return f'User {self.username}'

class User(db,model,UserMixin)
    id = db.Column(db,Interger,primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.column(db,string(255))
    active = db.Column(db.Boolean)