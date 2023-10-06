# https://proproprogs.ru/flask/ispolzovanie-shablonov
#{anc_head}

from flask import Flask, render_template

app = Flask(__name__)

menu = ["Установка", "Первое приложение", "Обратная связь"]

 
@app.route("/")
def index():
    return render_template('index.html', title="Про Flask", menu = menu)
#{file_return}
 
 
@app.route("/about")
def about():
    return render_template('index.html', title="О сайте", menu = menu)
#{file_return}
 
#{insert_decfn}

if __name__ == "__main__":
    app.run(debug=True)