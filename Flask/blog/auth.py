from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from . import db
from .models import User

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash('Login successful!', 'success')
            return redirect(url_for("views.home"))
        else:
            flash('Login unsuccessful. Please check your email and password.', 'danger')

    return render_template("login.html")

@auth.route("/register", methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")

        # Check if the email already exists
        existing_email = User.query.filter_by(email=email).first()
        # Check if the username already exists
        existing_username = User.query.filter_by(username=username).first()
        
        if existing_email:
            flash('Email address is already registered. Please use a different email.', 'danger')
        elif existing_username:
            flash('Username is already registered. Please use a different username.', 'danger')
        elif password != confirmPassword:
            flash('Passwords do not match. Please try again.', 'danger')
        elif len(username) < 2:
            flash('Username is too short. Please use a different username.', 'danger')
        elif len(password) < 6:
            flash('Username is too short. Please use a different password.', 'danger')
        else:
            # Create a new user
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for("auth.login"))
        
    return render_template("register.html")

@auth.route("/signOut")
@login_required
def signOut():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for("views.home"))