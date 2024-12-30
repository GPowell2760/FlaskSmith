from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("home.html.j2")


@main.errorhandler(404)
def page_not_found(e):
    return "Page does not exist", 404
