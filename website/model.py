from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# User model for storing user account information
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Unique user ID
    email = db.Column(db.String(150), unique=True)  # User email (must be unique)
    password = db.Column(db.String(150))  # Hashed password
    username  = db.Column(db.String(150))  # Username
    notes = db.relationship('Note')  # Relationship to user's notes

# Note model for storing user comments/notes
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique note ID
    data = db.Column(db.String(10000))  # Note content
    date = db.Column(db.DateTime(timezone=True), default=func.now())  # Timestamp
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Reference to the user who wrote the note

