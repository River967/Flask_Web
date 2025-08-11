from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_user, login_required, logout_user, current_user
from .model import User, Note
from . import db


# Set blueprint
views = Blueprint("views", __name__)


# Deafult/Home route
@views.route("/")
@views.route("home")
@views.route("index")
def home():
    return render_template("home.html")

# Gallery route
@views.route("/gallery")
def gallery():
    return render_template("gallery.html")

@views.route("/contact", methods=['POST', 'GET'])
@login_required
def contact():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Comment cannot be blank!')
        else: 
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Comment Added!', category='success')

    return render_template("contact.html")