from flask import Flask, render_template, request



app = Flask(__name__)


@app.route("/")
def index():
    data = {"name":"Suwannaphum Intalorbao", "age":"24", }
    return render_template("index.html", mydata = data)


@app.route("/about")
def mhai():
    product = ["Mhai", "lele", "fefe"]
    return render_template("about.html", myproduct = product)


@app.route("/admin")
def admin():
    username = "Suwannaphum"
    return render_template("admin.html", username = username)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/dataForm")
def signupForm():
    fname = request.args.get('fname')
    description = request.args.get('description')
    return render_template('thankyou.html', data = {"name":fname, "description":description})

if __name__ == "__main__":
    app.run(debug=True)
