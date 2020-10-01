from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import BookForm,UpdateProfile,CommentForm
from ..models import  User,Book,Comment
from flask_login import login_required,current_user
from .. import db
# from ..email import mail_message


@main.route('/')
def index():
    """ View root page function that returns index page
    """
    
    title = 'Home- Welcome'
    all_books = Book.query.all()
    return render_template('index.html', title = title,all_books=all_books)

def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

    
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)

@main.route('/new_book', methods=['GET', 'POST'])
@login_required
def new_blog():
    book_form = BookForm()
    
    if book_form.validate_on_submit():
        
        book = book_form.book.data
        # user_id = blog_form.user_id.data
        new_book = Book(book=book,user_id=current_user.id)
        new_book.save_books() 
        # subscriber=Subscribe.query.all()
        # for subscribe in subscriber:
        #     mail_message("New Blog Post","email/welcome_user",subscribe.email, new_book = new_book )
        # return redirect(url_for('main.index'))

    return render_template('new_book.html', book_form=book_form)

@main.route('/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def comment(id):
    comment_form = CommentForm()
    
    book= Book.query.filter_by(id=id).first()
    if comment_form.validate_on_submit():
        description = comment_form.description.data
        # user_id = comment_form.user_id.data
        new_comment = Comment(description=description, books_id  = id, user_id=current_user.id)
        new_comment.save_comments()
        new_comment.delete_comments()
        return redirect(url_for('main.index'))

    return render_template('comment.html',comment_form=comment_form, book= book)

# @main.route('/subscribe',methods=["GET","POST"])
# def subscribe():
#     form=SubscribeForm()

#     if form.validate_on_submit():
#         email = form.email.data
#         subscribe = Subscribe(email=form.email.data)
#         db.session.add(subscribe)
#         db.session.commit()

        
#         mail_message("New Blog Post","email/welcome_user",subscribe.email)
#         return redirect(url_for('main.index'))

#         title = 'Subscribe'
#     return render_template('subscribe.html',form=form)

@main.route('/delete/comment/<int:id>', methods = ['GET', 'POST'])
@login_required
def delete_comment(id):
  form=CommentForm()
  comment=Comment.query.filter_by(id=id).first()
 
  if comment is not None:
     comment.delete_comments()
     return redirect(url_for('main.index'))
     return render_template('comment.html', form=form)

@main.route('/delete/post/<int:id>', methods = ['GET', 'POST'])
@login_required
def delete_books(id):
    book=Book.query.filter_by(id=id).first()
 

    if book is not None:
       book.delete_books()
       return redirect(url_for('main.index'))