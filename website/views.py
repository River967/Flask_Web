from flask import Blueprint, render_template, url_for


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

@views.route("/contact")
def contact():
    return render_template("contact.html")