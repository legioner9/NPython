# https://proproprogs.ru/flask/ispolzovanie-shablonov
#{anc_head}

from flask import Flask

app = Flask(__name__)

 
@app.route("/")
def index():
    return '''<!DOCTYPE html>
<html>
<head>
<title></title>
</head>
<body>
</body>
</html>'''
#{file_return}
 
 
@app.route("/about")
def about():
    return "<h1>Про Flask</h1>"
#{file_return}
 
#{insert_decfn}

if __name__ == "__main__":
    app.run(debug=True)