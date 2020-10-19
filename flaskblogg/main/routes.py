from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from flaskblogg import db
from flaskblogg.modules import Post
from flaskblogg.posts.forms import PostForm


main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5, page=page)
    return render_template("home.html", posts=posts)


@main.route("/about")
def about():
    return render_template("about.html", title="About")
