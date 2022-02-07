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


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                    <title>Жди нас, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/image_mars.png')}">
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнём с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
