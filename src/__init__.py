from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name": "Microblog",
        "thumb": "img/microblog.jpg",
        "hero": "img/microblog-2.jpg",
        "categories": ["python", "MongoDB", "HTML", "CSS"],
        "slug": "microblog",
        "prod": "https://rad-it-cons-microblog.herokuapp.com/",
    },
]

slug_to_project = { project["slug"]: project for project in projects }

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template(("contact.html"))

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])