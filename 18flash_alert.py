from flask import Flask, render_template, request, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
Bootstrap(app)

class MyForm(FlaskForm):
    name = StringField("ป้อนชื่อ: ", validators=[DataRequired()])
    select = SelectField("ความสามารถพิเศษ", choices=[("vcode", "VibeCoding"), ("eng", "พูดอังกฤษดีมาก"), ("imgay","ผมเป็นเกย์")])
    gender = RadioField("เพศ",choices=[("male", "ชาย"), ("female", "หญิง"), ("other", "อื่นๆ")]) #choice=["ค่าจริง", "ค่าที่แสดงผล"]
    isAccept = BooleanField("ยอมรับเงื่อนไข")
    address = TextAreaField("ป้อนที่อยู่ของคุณ: ")
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
    form = MyForm()
    if form.validate_on_submit():
        flash("Saved DATA!")
        session["address"] = form.address.data
        session["select"] = form.select.data
        session["name"] = form.name.data
        session["isAccept"] = form.isAccept.data
        session["gender"] = form.gender.data  
         
        # Clear Data
        form.address.data = ""
        form.name.data = ""
        form.select.data = ""
        form.isAccept.data = ""
        form.gender.data = ""
    return render_template('index_WTF.html', form = form)


if __name__ == "__main__":
    app.run(debug=True)
