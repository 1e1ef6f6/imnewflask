from flask import Flask, render_template

app = Flask(__name__)

@app.route("/admin")
def index():
    name = "Suwannaphum Intalorbao"
    age = "24"
    return render_template("admin.html", myname = name, myage = age) 

if __name__ == "__main__":
    app.run(debug=True)