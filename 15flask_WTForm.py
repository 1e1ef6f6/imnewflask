from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class MyForm(FlaskForm):
    name = StringField("ป้อนชื่อ: ")
    submit = SubmitField("บันทึก")



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


@app.route('/wtf', methods=["get", "post"])
def wtForm():
    name = False
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
    return render_template('index_WTF.html', form = form, name = name)


if __name__ == "__main__":
    app.run(debug=True)
