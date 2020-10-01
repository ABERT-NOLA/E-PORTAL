from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime



#  login class instances

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))   

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    post = db.relationship('Book',backref = 'user',lazy="dynamic")
    comment = db.relationship('Comment',backref = 'user',lazy="dynamic")
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure  = db.Column(db.String(255)) 

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    def __repr__(self):
        return f'User {self.username}'

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer,primary_key = True)
    book = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comment = db.relationship('Comment',backref = 'books',lazy="dynamic")
    
    def save_books(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_books(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_books(id):
        books = Book.query.filter_by(id=user_id).all()
        return books

    def __repr__(self):
        return f'User {self.name}' 

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    description= db.Column(db.String(255))
    books_id = db.Column(db.Integer,db.ForeignKey('books.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
    def save_comments(self):
       db.session.add(self)
       db.session.commit()
     
    def delete_comments(self):
       db.session.add(self)
       db.session.commit()

    @classmethod
    def get_comments(id):
       comments = Comment.query.all()
       return comments


# --------      

