from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def home():
    # The template name should be "home.html" without the "templates/" prefix
    return render_template("home.html")
