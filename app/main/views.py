from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Admin, Post, Comment
import markdown2
from .forms import CommentForm, UpdateProfile, AddPostForm, Subscribe
from .. import db,photos
from datetime import datetime
from flask_login import login_required,current_user


@main.route('/')
def index():

    posts = Post.query.all()
    title = "Home"   
    return render_template("index.html", posts = posts, title = title)



@main.route("/<uname>/add_post", methods = ["GET","POST"])
@login_required
def add_post(uname):
    
    form = AddPostForm()
    Admin = Admin.query.filter_by(username = uname).first()
  
    title = "Add Post"
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        posted = datetime.now()
        new_post = Post(title = title, content = post, admin = admin, posted = posted)
        new_post.save_pitch()  
        posts = Post.query.all()
    return render_template("add_post.html",form = form, title = title)

@main.route("/<user>/post/<post_id>/add-comment", methods = ["GET","POST"])
@login_required
def comment(user,pitch_id):
    user = User.query.filter_by(id = user).first()
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    form = CommentForm()
    title = "Add comment"
    if form.validate_on_submit():
        content = form.comment.data 
        posted = datetime.now()
        new_comment = Comment(comment = form.comment.data, user = user, pitch = pitch, posted = posted )
        new_comment.save_comment()
        return redirect(url_for("main.view_comments", pitch_id=pitch.id))
    return render_template("new_comment.html", title = pitch.title,form = form,pitch = pitch)

@main.route("/<pitch_id>/comments")
@login_required
def view_comments(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    title = "Comments"
    comments = pitch.get_pitch_comments()

    return render_template("comment.html", comments = comments,pitch = pitch,title = title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches = Pitch.query.filter_by(user_id = user.id)

    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user, pitches = pitches)


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

@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname = uname))