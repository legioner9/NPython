# https://proproprogs.ru/flask/ispolzovanie-shablonov
#{anc_head}

from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = ["Установка", "Первое приложение", "Обратная связь"]

 
@app.route("/")
def index():
    print( url_for('index') )
    return render_template('index.html', title="Про Flask", menu = menu)
#{file_return}
 
 
@app.route("/about")
def about():
    print( url_for('about') )
    return render_template('about.html', title="О сайте", menu = menu)
#{file_return}
 
#{insert_decfn}

if __name__ == "__main__":
    app.run(debug=True)