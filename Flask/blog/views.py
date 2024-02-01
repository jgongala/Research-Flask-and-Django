from flask import Blueprint, render_template, flash, redirect, url_for, request, abort
from flask_login import login_required, current_user
from . import db
from .models import Post, User

views = Blueprint("views", __name__)

@views.route("/")
@login_required
def home():
    # Retrieve all posts from the database
    posts = Post.query.all()

    # Check if the user is authenticated
    if not current_user.is_authenticated:
        flash("Please log in to access this page.", "danger")
        return redirect(url_for("login"))  # Redirect to login page or wherever you want

    # Render the home template with the user's username and posts
    return render_template("home.html", name=current_user.username, posts=posts)

@views.route("/createPost", methods=['GET', 'POST'])
@login_required
def createPost():
    if request.method == 'POST':
        # Handle form submission
        title = request.form.get('title')
        text = request.form.get('text')

        # Check for empty fields
        if not text:
            flash("Post is empty. Please insert text.", "danger")
        elif not title:
            flash("Title is empty. Please insert title.", "danger")
        else:
            # Process the data and save it to the database
            new_post = Post(title=title, text=text, author=current_user.id)
            db.session.add(new_post)
            db.session.commit()

            flash('Post created successfully!', 'success')
            return redirect(url_for('views.home'))

    return render_template("createPost.html")

@views.route("/editPost/<int:post_id>", methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    # Retrieve the post from the database or return a 404 error
    post = Post.query.get_or_404(post_id)

    # Check if the current user has permission to edit the post
    if current_user != post.user:
        abort(403)  # Forbidden

    if request.method == 'POST':
        # Handle form submission
        post.title = request.form.get('title')
        post.text = request.form.get('text')

        # Check for empty fields
        if not post.text:
            flash("Post is empty. Please insert text.", "danger")
        elif not post.title:
            flash("Title is empty. Please insert title.", "danger")
        else:
            # Save the changes to the database
            db.session.commit()

            flash('Post updated successfully!', 'success')
            return redirect(url_for('views.home'))

    return render_template("editPost.html", post=post)

@views.route("/deletePost/<int:id>", methods=['GET', 'POST'])
@login_required
def delete_post(id):
    # Retrieve the post from the database based on the provided id
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash("Post does not exist!", 'danger')
    elif current_user.id != post.author:
        flash("No permission to delete post!")
        print(current_user.id)
        print(post.id)
    else:
        # Delete the post from the database
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted!", 'success')
        
    return redirect(url_for('views.home'))
