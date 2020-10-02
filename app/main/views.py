from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort
from ..model import Course,Exam,Answer
from .forms import CourseForm,ExamForm,AnswerForm
from .. import db
from . import main
import markdown2


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))

@main.route('/course', methods=['GET','POST'])
@login_required
def new_course():
    courses = Course.query.all()
    form = CourseForm()
    if form.validate_on_submit():
        course = form.course.data
        topic = form.topic.data
        module = form.module.data
        new_course=Course(course=course,topic=topic,module = module, user_id=current_user.id)
        
        new_course.save_course()
        
        return redirect(url_for('main.new_course'))
    
    return render_template('course.html', course_form=form,courses=courses)


@main.route('/exam/<int:course_id>', methods=['GET','POST'])
@login_required
def new_exam(course_id):
    form = ExamForm
    courses = Course.query.get(course_id)
    exam = Exam.query.filter_by(course_id=course_id).all()
    form = ExamForm()
    if form.validate_on_submit():
        course = form.course.data
        module = form.module.data
        question = form.question.data
        topic = form.topic.data
        
        course_id = course_id
        user_id = current_user._get_current_object().id
        new_exam= Exam(course=course,module=module,question=question,topic=topic,course_id = course_id, user_id=user_id)
        new_exam.save_exam()      
        # import pdb; pdb.set_trace()
        return redirect(url_for('main.new_exam', course_id=course_id))
    
    return render_template('exam.html',form=form, exam=exam, course_id=course_id,courses=courses)


@main.route('/answer/<int:exam_id>', methods=['GET','POST'])
@login_required
def new_answer(exam_id):
    form = AnswerForm
    exam = Exam.query.get(exam_id)
    answer = Answer.query.filter_by(exam_id=exam_id).all()
    form = AnswerForm()
    if form.validate_on_submit():
        answer = form.answer.data
        
        exam_id = exam_id
        user_id = current_user._get_current_object().id
        new_answer= Answer(exam=exam,answer=answer,exam_id = exam_id, user_id=user_id)
        new_exam.save_exam()      
       
        return redirect(url_for('main.new_exam', exam_id=exam_id))
    
    return render_template('exam.html', form=form, answer=answer, exam_id=exam_id,exam=exam)

    return render_template('index.html')
