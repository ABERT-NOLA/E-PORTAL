
from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'



class Schools(db.Model):
    __tablename__ = 'schools'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    
    def __repr__(self):
        return f'User {self.username}'




class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer,primary_key=True)
    course = db.Column(db.String(255))
    module = db.Column(db.String(255))
    topic = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))
    def save_course(self):
        db.session.add(self)
        db.session.commit()
    def delete_course(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_course(cls,id):
        course = Course.query.filter_by(user_id=id).all()
        return course






class Exam(db.Model):
    __tablename__ = 'exams'
    id = db.Column(db.Integer,primary_key=True)
    exam = db.Column(db.String(255))
    topic = db.Column(db.String(255))
    course = db.Column(db.String(255))
    module = db.Column(db.String(255))
    question = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    
    def save_exam(self):
        db.session.add(self)
        db.session.commit()
    def delete_exam(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_exam(cls,id):
        exam = Exam.query.filter_by(user_id=id).all()
        return exam

class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer,primary_key=True)
    answer = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'))
    
    def save_answer(self):
        db.session.add(self)
        db.session.commit()
    def delete_answer(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_answer(cls,id):
        answer = Answer.query.filter_by(user_id=id).all()
        return answer