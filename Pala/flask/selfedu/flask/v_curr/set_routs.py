

@app.route("/")
def index():
    return "index page"

@app.route("/about")
def about():
    return "<h1>About site</h1>"