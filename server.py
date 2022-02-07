from flask import Flask, url_for, request

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
                <html lang="ru">
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
                    <img src="{url_for('static', filename='img/image_mars.png')}" width="400" height="400">
                    <div class="alert alert-dark" role="alert">
                      <b>Человечество вырастает из детства.</b>
                    </div>
                    <div class="alert alert-success" role="alert">
                      <b>Человечеству мала одна планета.</b>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      <b>Мы сделаем обитаемыми безжизненные планеты.</b>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <b>И начнём с Марса!</b>
                    </div>
                    <div class="alert alert-danger" role="alert">
                      <b>Присоединяйся!</b>
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="ru">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <div class="page-title">
                                    <h1>Анкета претендента</h1>
                                    <h3>на участие в миссии</h3>
                                </div>
                                <div>
                                    <form class="login_form" method="post" enctype="multipart/form-data">
                                        <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                        <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                        <br>
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у Вас образование?</label>
                                            <select class="form-control" id="classSelect" name="education">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                              <option>Высшее</option>
                                            </select>
                                        </div>
                                        Какие у вас есть профессии?<br>
                                        <div class="form-group form-check">
                                            
                                            <input type="checkbox" class="form-check-input" id="acceptEngenier" name="engenier"> Инженер <br>
                                            
                                            <input type="checkbox" class="form-check-input" id="accepDoctor" name="doctor"> Врач <br>
                                            
                                            <input type="checkbox" class="form-check-input" id="acceptPilot" name="pilot"> Пилот <br>
                                            
                                            <input type="checkbox" class="form-check-input" id="acceptBuilder" name="builder"> Строитель <br>
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="motivation" rows="3" name="motivation"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form.get('surname'))
        print(request.form.get('name'))
        print(request.form.get('email'))
        print(request.form.get('education'))
        print(request.form.get('engenier'))
        print(request.form.get('doctor'))
        print(request.form.get('pilot'))
        print(request.form.get('builder'))
        print(request.form.get('sex'))
        print(request.form.get('motivation'))
        file = request.files.get('file')
        print(file.read())
        print(request.form.get('accept'))
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
