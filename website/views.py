from flask import Blueprint, render_template, url_for, request, flash, redirect, jsonify, json
from flask_login import login_user, login_required, logout_user, current_user
from .model import User, Note
from . import db


# Set up the blueprint for views
views = Blueprint("views", __name__)


# Home page routes
@views.route("/")
@views.route("/home")  
@views.route("/index")  
def home():
    # Render the home page
    return render_template("home.html", user=current_user)  

# About page route
@views.route("/about")
def about():
    # Render the about page
    return render_template("about.html", user=current_user)  

# Contact page route (requires login)
@views.route("/contact", methods=['POST', 'GET'])
@login_required
def contact():
    # Handle comment submission
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Comment cannot be blank!', category='error')  
        else: 
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Comment Added!', category='success')
        # Redirect after POST to prevent duplicate submissions
        return redirect(url_for('views.contact'))
    # Render the contact page
    return render_template("contact.html", user=current_user) 

# Delete note route (AJAX, requires login)
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

# Agent wiki routes

# Astra wiki route
@views.route("/astra")
def astra():
    # Render the Astra agent wiki page
    return render_template("Astra.html", user=current_user)

@views.route("/breach")
def breach():
    # Render the Breach agent wiki page
    return render_template("Breach.html", user=current_user)

@views.route("/cypher")
def cypher():
    # Render the Cypher agent wiki page
    return render_template("Cypher.html", user=current_user)

@views.route("/jett")
def jett():
    # Render the Jett agent wiki page
    return render_template("Jett.html", user=current_user)

@views.route("/killjoy")
def killjoy():
    # Render the Killjoy agent wiki page
    return render_template("Killjoy.html", user=current_user)

@views.route("/neon")
def neon():
    # Render the Neon agent wiki page
    return render_template("Neon.html", user=current_user)

@views.route("/omen")
def omen():
    # Render the Omen agent wiki page
    return render_template("Omen.html", user=current_user)

@views.route("/phoenix")
def phoenix():
    # Render the Phoenix agent wiki page
    return render_template("Phoenix.html", user=current_user)

@views.route("/raze")
def raze():
    # Render the Raze agent wiki page
    return render_template("Raze.html", user=current_user)

@views.route("/reyna")
def reyna():
    # Render the Reyna agent wiki page
    return render_template("Reyna.html", user=current_user)

@views.route("/sage")
def sage():
    # Render the Sage agent wiki page
    return render_template("Sage.html", user=current_user)

@views.route("/skye")
def skye():
    # Render the Skye agent wiki page
    return render_template("Skye.html", user=current_user)