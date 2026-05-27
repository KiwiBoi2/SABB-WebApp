# import external libraries
from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import current_user, login_required

# import database
from . import db
from .models import User, Post, Comment

# set views as blueprint 
views = Blueprint("views", "__name__")


# default/home route
@views.route("/")
@views.route("/home")

# home route function
# returns homepage
def home():
    return render_template("home.html", user=current_user)
    
# blog page route
@views.route("/blog")
# user must be logged in
@login_required 
# blog route function
# returns blog page
def blog():
    posts = Post.query.all()
    return render_template("blog.html", user=current_user, posts=posts)


# create blog post route
@views.route("/create-post", methods=["GET", "POST"])
@login_required
# create post route function
# returns create_post.html
def create_post():
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get("content")
        
        if not title:
            flash("Title cannot be empty", category="error")
        elif not content:
            flash("Blog cannot be empty", category="error")
        else:
            post = Post(title=title, content=content, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash("Post created!", category="success")
            return redirect(url_for("views.blog"))


    return render_template("create_post.html", user=current_user)

# delete blog post route
@views.route("/delete-post/<id>")
# user must be logged in to delete
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash("Post does not exist.", category="error")
    elif current_user.id != post.author:
        flash("You do not have permission to delete this post.", category="error")
    else:
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted.", category="success")
    return redirect(url_for("views.blog"))

# create blog comment route
@views.route("/create-comment/<post_id>", methods=['POST'])
# user must be logged in to post
@login_required
def create_comment(post_id):
    text = request.form.get("text")
    if not text:
        flash("Comment cannot be empty.", category="error")
    else:
        post = Post.query.filter_by(id=post_id)
        if post:
            comment = Comment(text=text, author=current_user.id, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
            flash("Comment added!", category="success")
        else:
            flash("Comment does not exist.", category="error")
    return redirect(url_for("views.blog"))


# delete blog comment route
@views.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()
    if not comment:
            flash("Comment does not exist.", ategory="error")
    elif current_user.id != comment.author and current_user.id != comment.post.author:
        flash("You do not have permission to delete this comment.", category="error")
    else:
        db.session.delete(comment)
        db.session.commit()
        flash("Comment deleted.", category="success")
    return redirect(url_for("views.blog"))