from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    greet_with_link = """<h1>Привет, Мир!</h1>
    <p><a href="user/Путр/Ларин">Нажми на меня</a></p>"""
    return greet_with_link


@app.route('/user/<surname>/<name>')
def get_user(name, surname):
    personal_instruc = f"""<h1>Привет, {surname} {name}!</h1>
    <p>Измени имя пользователя в адресной строке и перезагрузи страницу</p>"""
    return personal_instruc


if __name__ == '__main__':
    app.run(debug=True)
