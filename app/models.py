from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_admin(admin_id):
    return Admin.query.get(int(admin_id))

class Admin (UserMixin, db.Model):

    __tablename__ = 'admins'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    posts = db.relationship("Post", backref = "admin", lazy = "dynamic")
    comments = db.relationship('Comment', backref="admin", lazy = "dynamic")

    def save_admin(self):

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

    def get_admin_posts(self):
        admin = Admin.query.filter_by(id = self.id).first()
        return admin.posts
    
    def get_admin_comments(self):
        admin   = Admin.query.filter_by(id = self.id).first()
        return admin.comments


class Post (db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    category = db.Column(db.String())
    admin_id = db.Column(db.Integer, db.ForeignKey('admins.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    
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
    comment=db.Column(db.String(255))
    admin_id = db.Column(db.Integer,db.ForeignKey('admins.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)

    
    def save_comment(self):

        db.session.add(self)
        db.session.commit()

class Subscriber(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(), unique = True)

    
