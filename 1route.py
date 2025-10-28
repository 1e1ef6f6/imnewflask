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


if __name__ == "__main__":
    app.run()
