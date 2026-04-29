# import external libraries
from flask import Blueprint, render_template

# set views as blueprint 
views = Blueprint("views", "__name__")


# default/home rout
@views.route("/")
@views.route("/home")

# home route function
# returns homepage
def home():
    return render_template("home.html")