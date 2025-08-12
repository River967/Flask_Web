from flask import Blueprint, render_template, url_for, request, flash, redirect, jsonify, json
from flask_login import login_user, login_required, logout_user, current_user
from .model import User, Note
from . import db


# Set blueprint
views = Blueprint("views", __name__)


# Default/Home route
@views.route("/")
@views.route("/home")  # Fixed: Added missing /
@views.route("/index")  # Fixed: Added missing /
def home():
    return render_template("home.html", user=current_user)  # Added user


# Gallery route
@views.route("/gallery")
def gallery():
    return render_template("gallery.html", user=current_user)  # Added user

@views.route("/about")
def about():
    return render_template("about.html", user=current_user)  # Added user


# Contact route
@views.route("/contact", methods=['POST', 'GET'])
@login_required
def contact():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Comment cannot be blank!', category='error')  # Added category
        else: 
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Comment Added!', category='success')

    return render_template("contact.html", user=current_user)  # Added user

@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    note = json.loads(request.data)
    note_id = note['noteId']
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

# Astra wiki route
@views.route("/astra")
def astra():
    return render_template("Astra.html", user=current_user)