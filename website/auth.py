from flask import Blueprint, render_template, url_for, request, flash, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .model import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():