from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required
from ..model import Course,Exam,Answer
class CourseForm(FlaskForm):
    course = TextAreaField('Write The Course...')
    module = TextAreaField('Module...')
    topic = TextAreaField('Topic...')
    submit = SubmitField('Submit')

class ExamForm(FlaskForm):
    question = TextAreaField('Write The Question...')
    module = TextAreaField('Module...')
    topic = TextAreaField('Topic...')
    course = TextAreaField('Course...')
    submit = SubmitField('Submit')

class AnswerForm(FlaskForm):
    answer = TextAreaField('Write The Answer...')
    submit = SubmitField('Submit')