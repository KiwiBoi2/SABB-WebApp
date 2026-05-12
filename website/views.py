# import external libraries
from flask import Blueprint, render_template, request, flash, url_for
from flask_login import current_user, login_required, logout_user, login_user
# set views as blueprint 
views = Blueprint("views", "__name__")


# default/home rout
@views.route("/")
@views.route("/home")

# home route function
# returns homepage
def home():
    return render_template("home.html", user=current_user)
    

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
            post = User(title=title, content=content, author=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash("Post created!", category="success")
            return redirect(url_for("views.home"))


    return render_template("create_post.html", user=current_user)