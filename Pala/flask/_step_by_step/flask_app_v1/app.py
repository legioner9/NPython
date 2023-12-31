from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def get_page_about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
