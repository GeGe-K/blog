from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Post
import markdown2
from .forms import CommentForm, UpdateProfile, AddPostForm, SubscribeForm
from .. import db,photos
from datetime import datetime
from flask_login import login_required,current_user


@main.route('/')
def index():

    posts = Post.query.order_by(Blog.posted.desc()).all()
    title = "Home"   
    return render_template("index.html", posts = posts, title = title)



@main.route("/add/post", methods = ["GET","POST"])
@login_required
def add_post():
    
    form = AddPostForm()  
    title = "Add Post"

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        posted = datetime.now()
        if 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            path = f'photos/{filename}'
        new_post = Post(title = title, content = post, user = user, posted = posted)
        new_post.save_post()  
        posts = Post.query.all()
    return render_template("add_post.html",form = form, title = title)

@main.route("/delete/<id>")
def delete(id):
    post = Post.query.filter_by(id = id).first()
    user_id = post.user_id
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('main.profile', id = user_id))

@main.route("/post/<int:id>/", methods = ["GET","POST"])

def view_posts(post_id):
    post = Post.query.filter_by(id = id).first()
    form = CommentForm()
    title = "Leave a comment"
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data 
        name = form.name.data  
        posted = datetime.now()
        new_comment = Comment(title = title, comment = comment, name = name, post = post, posted = posted )
        new_comment.save_comment()
        return redirect(url_for("main.view_posts", id=post.id))
    return render_template("post.html", title = title, post = post, form = form, comments = comments)

@main.route("/delete/comment/<id>")
def delete_comment(id):
    comment = Comment.query.filter_by(id = id).first()
    post_id = comment.post.id
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("main.view_posts", id = post_id))


@main.route('/user/<user_id>')
def profile(user_id):
    user = User.query.filter_by(id = user_id).first()
    posts = Post.query.filter_by(user_id = user.id)

    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user, posts = posts )


@main.route('/user/<user_id>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', user_id=user.id))

    return render_template('profile/update.html', form=form)

@main.route('/user/<user_id>/update/pic', methods = ['POST'])
@login_required
def update_pic(user_id):
    user = User.query.filter_by(id = user_id).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',user_id = user_id))

@main.route('/subscribe', methods=['GET','POST'])
def subscriber():
    form = SubscribeForm()

    if form.validate_on_submit():
        subscriber= Subscriber(email=form.email.data,name = form.name.data)

        db.session.add(new_subscriber)
        db.session.commit()

        mail_message("Welcome to The Resident","email/welcome_subscriber",subscriber.email,subscriber=subscriber)

        title= "Home"
        return render_template('index.html',title=title, posts=posts)

    subscriber = Post.query.all()
    posts = Post.query.all()
    return render_template('index.html',subscriber=subscriber,form=form,post=posts)
