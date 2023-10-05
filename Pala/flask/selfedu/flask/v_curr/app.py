# https://proproprogs.ru/flask/flask-chto-eto-takoe-wsgi-prilozhenie 
# https://proproprogs.ru/flask/flask-chto-eto-takoe-wsgi-prilozhenie 
# https://proproprogs.ru/flask/flask-chto-eto-takoe-wsgi-prilozhenie 
#{anc_head}

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "index page"
#{file_return}
@app.route("/index")
def index():
    return "index page"
#{file_return}
@app.route("/about")
def about():
    return "<h1>About site</h1>"
#{file_return}
#{insert_decfn}

if __name__ == "__main__":
    app.run(debug=True)