from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    if not current_user.is_authenticated:
        flash("Please log in to access this page.", "danger")
        return redirect(url_for("login"))  # Redirect to login page or wherever you want

    return render_template("home.html", name=current_user.username)

@views.route("/createPost", methods=['GET', 'POST'])
@login_required
def createPost():
    # The template name should be "home.html" without the "templates/" prefix
    return render_template("createPost.html")
