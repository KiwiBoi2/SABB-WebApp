# import external libraries
from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
# import database
from . import db
# import from .models user
from .models import User

# set auth blueprint
auth = Blueprint("auth", "__name__")


# sign up route
@auth.route("/sign-up", methods=["GET","POST"])
# sign up function
# returns sign_up page
def sign_up():
    # signup function
    # returns signup page
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # check if email or username already exists

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

        # validation of password, username and email

        if email_exists:
            flash("Email is already in use.", category="error")
        elif username_exists:
            flash("Username is already in use.", category="error")
        elif password1 != password2:
            flash("Passwords do not match!", category="error")
        elif len(password1) < 8:
            flash("Password is too short!", category="error")
        elif len(username) < 2:
            flash("Username is too short!", category="error") 
        elif len(email) < 4:
            flash("Email is not valid!", category="error")
        else:

            # create new user and add to database

            new_user = User(email=email, username=username, password=generate_password_hash(password1, method="scrypt:32768:8:1"), date_created=db.func.now())
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Your account has been created!", category="success")
            return redirect(url_for("views.home"))


    return render_template("sign_up.html", user=current_user)

# login route
@auth.route("/login", methods=["GET","POST"])
# login function
# returns login page
def login():
    if request.method == "POST":
        # get email and password from login form
        email = request.form.get("email")
        password = request.form.get("password")

        # queries database for user information using email address
        user = User.query.filter_by(email=email).first()
        # checks email and password
        if user:
            # logs in user if correct login information is provided and redirects to home page
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success") 
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                # if incorrect password, flash error
                flash("Incorrect password!", category="error")
        else:
            # if email does not exist, flash error
            flash("User associated with this email does not exist!", category="error")


    return render_template("login.html", user=current_user)

# logout route
@auth.route("/logout")
@login_required
# logout function
# returns logout page   
def logout():
    logout_user()
    return redirect(url_for("views.home"))
