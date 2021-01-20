import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String(10), unique=True, nullable=False) #esto significa que debebn ser 10 o que es hasta 10?
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password = Column(String(8), nullable=False)
    posts = relationship("Post", backref="user")
    comment = relationship("Comment", backref="user")
    post_like = relationship("PostLike", backref="user")
    comment_like = relationship("CommentLike", backref="user")

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    image_url = Column(String, unique=True, nullable=False)
    date_published = Column(DateTime, nullable=False)
    content = Column(String(300), nullable=True) 
    latitude = Column(String, nullable=True)
    longitude = Column(String, nullable=True)
    likes = relationship("PostLike", backref="post")
    comments = relationship("Comment", backref="post")

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(String, nullable=False)
    likes = relationship("CommentLike", backref="comment")
    datetime = Column(DateTime, nullable=False)

class CommentLike(Base):
    __tablename__ = 'comment_like'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class PostLike(Base):
    __tablename__ = 'post_like'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')