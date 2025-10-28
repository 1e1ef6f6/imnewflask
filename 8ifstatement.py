from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = {"name":"Suwannaphum Intalorbao", "age":"24", }
    return render_template("index.html", mydata = data)


@app.route("/about")
def mhai():
    return render_template("about.html")


@app.route("/admin")
def admin():
    username = "Suwannaphum"
    return render_template("admin.html", username = username)


if __name__ == "__main__":
    app.run(debug=True)
