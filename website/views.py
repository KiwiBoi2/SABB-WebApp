# import external libraries
from flask import Blueprint, render_template
from flask_login import current_user, login_required

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
    return render_template("create_post.html", user=current_user)