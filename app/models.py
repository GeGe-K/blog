from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User (UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    full_name = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    posts = db.relationship("Post", backref = "user", lazy = "dynamic")
    comments = db.relationship('Comment', backref="user", lazy = "dynamic")

    def save_user(self):

        db.session.add(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password) 

    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)  


class Post (db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    pic_path = db.Column(db.String())
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='post', lazy="dynamic")

    
    def save_post(self):

        db.session.add(self)
        db.session.commit()

    def get_post_comments(self):

        post = Post.query.filter_by(id = self.id).first()
        comments = Comment.query.filter_by(post_id = post.id).order_by(Comment.posted.desc())
        return comments
        

class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String)
    title = db.Column(db.String)
    comment=db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)


    
    def save_comment(self):

        db.session.add(self)
        db.session.commit()
    

class Subscriber(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30))
    email = db.Column(db.String, unique = True)


    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    
