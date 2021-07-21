import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_treks")
def get_treks():
    treks = list(mongo.db.treks.find())
    return render_template("treks.html", treks=treks)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    treks = list(mongo.db.treks.find({"$text": {"$search": query}}))
    return render_template("treks.html", treks=treks)


@app.route("/home")
def home():
    treks = list(mongo.db.treks.find())
    categories = list(mongo.db.categories.find().sort("category_id", 1))
    return render_template(
        "home.html", treks=treks, categories=categories)


# @app.route("/favourite_trek/<trek_id>", methods=["GET", "POST"])
# def favourite_trek(trek_id):
#     treks = mongo.db.treks.find_one({"_id": ObjectId(trek_id)})
#     user = mongo.db.users.find_one(
#         {"username": session["user"]})["username"]


@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("This Username is Taken")
            return redirect(url_for("join"))
        elif existing_email:
            flash("This Email is Taken")
            return redirect(url_for("join"))

        join = {
            "fname": request.form.get("fname").lower(),
            "lname": request.form.get("lname").lower(),
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(join)

        # put new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("join.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password message
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Get the session users username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_trek", methods=["GET", "POST"])
def add_trek():
    if request.method == "POST":
        trek = {
            "trek_name": request.form.get("trek_name"),
            "county_name": request.form.get("county_name"),
            "category_name": request.form.get("category_name"),
            "trek_distance": request.form.get("trek_distance"),
            "trek_elevation": request.form.get("trek_elevation"),
            "trek_route_type": request.form.get("trek_route_type"),
            "trek_description": request.form.get("trek_description"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        mongo.db.treks.insert_one(trek)
        flash("Trek Successfully Added")
        return redirect(url_for("get_treks"))

    counties = mongo.db.counties.find().sort("county_name", 1)
    # Sort by _id to keep categories in order
    categories = mongo.db.categories.find().sort("category_id", 1)
    return render_template(
        "add_trek.html", counties=counties, categories=categories)


@app.route("/edit_trek/<trek_id>", methods=["GET", "POST"])
def edit_trek(trek_id):
    if request.method == "POST":
        submit = {
            "trek_name": request.form.get("trek_name"),
            "county_name": request.form.get("county_name"),
            "category_name": request.form.get("category_name"),
            "trek_distance": request.form.get("trek_distance"),
            "trek_elevation": request.form.get("trek_elevation"),
            "trek_route_type": request.form.get("trek_route_type"),
            "trek_description": request.form.get("trek_description"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        mongo.db.treks.update({"_id": ObjectId(trek_id)}, submit)
        flash("Trek Successfully Updated")

    trek = mongo.db.treks.find_one({"_id": ObjectId(trek_id)})
    counties = mongo.db.counties.find().sort("county_name", 1)
    categories = mongo.db.categories.find().sort("category_id", 1)
    return render_template(
        "edit_trek.html", trek=trek, counties=counties, categories=categories)


# view individual trek page
@app.route("/view_trek/<trek_id>")
def view_trek(trek_id):
    trek = mongo.db.treks.find_one({"_id": ObjectId(trek_id)})
    return render_template("view_trek.html", trek=trek)


@app.route("/delete_trek/<trek_id>")
def delete_trek(trek_id):
    mongo.db.treks.remove({"_id": ObjectId(trek_id)})
    flash("Trek Successfully Deleted")
    return redirect(url_for("get_treks"))


@app.route("/get_categories")
def get_categories():
    category_easy = list(mongo.db.treks.find(
        {"category_name": "Easy"}).sort("category_name", 1))
    category_moderate = list(mongo.db.treks.find(
        {"category_name": "Moderate"}).sort("category_name", 1))
    category_hard = list(mongo.db.treks.find(
        {"category_name": "Hard"}).sort("category_name", 1))
    categories = list(mongo.db.categories.find().sort("category_id", 1))
    return render_template(
        "categories.html", categories=categories, category_easy=category_easy, category_moderate=category_moderate, category_hard=category_hard)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
