from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, Mhai</h1>"


@app.route("/mhai")
def mhai():
    return "<h1>Welcome Black!, Mhailele</h1>"


@app.route("/admin")
def admin():
    return "Hello ADMIN"


## Dynamic Roting
@app.route("/user/<name>/<age>")
def member(name, age):
    return "<h1>สวัสดีสมาชิก: {}, อายุ: {}</h1>".format(name, age)


if __name__ == "__main__":
    app.run()
