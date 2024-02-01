from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())    

    # Define a one-to-many relationship with the Post model.
    # 'posts' attribute will be available on instances of User.
    # 'backref' creates a corresponding attribute on the Post model.
    # 'passive_deletes=True' ensures that when a user is deleted,
    # associated posts are also deleted (passive cascade).
    posts = db.relationship('Post', backref='user', passive_deletes=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())    

    # Define a foreign key relationship with the User model.
    # 'nullable=False' ensures every post has an associated author.
    # 'ondelete="CASCADE"' ensures that if a user is deleted,
    # all associated posts are also deleted automatically.
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
