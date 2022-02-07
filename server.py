from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index_1():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '''
            <b>Человечество вырастает из детства.</b>
            <br>
            <b>Человечеству мала одна планета.</b>
            <br>
            <b>Мы сделаем обитаемыми безжизненные пока планеты.</b>
            <br>
            <b>И начнем с Марса!</b>
            <br>
            <b>Присоединяйся!</b>
            '''


@app.route('/image_mars')
def image_mars():
    return f'''
            <h1>Жди нас, Марс!</h1>
            <br>
            <img src="{url_for('static', filename="img/image_mars.png")}" alt="марс уничтожен">
            <br>
            Вот она, красная планета.
            '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
