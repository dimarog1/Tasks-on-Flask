from flask import Flask, render_template, request

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


title = ''
surname = ''
name = ''
education = ''
profession = ''
sex = ''
motivation = ''
ready = ''


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('index.html', **param)


@app.route('/training/<prof>')
def training(prof):
    param = {}
    param['title'] = prof
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        param['phrase'] = 'Инженерные тренажеры'
        param['image'] = '../static/img/ingenier.png'
    else:
        param['phrase'] = 'Научные симуляторы'
        param['image'] = '../static/img/doctor.jpg'
    return render_template('training.html', **param)


@app.route('/list_prof/<kind>')
def list_prof(kind):
    param = {}
    param['title'] = kind
    param['kind'] = kind
    param['jobs'] = [
        'Врач',
        'Строитель',
        'Инженер',
        'Сварщик',
        'Астроном',
        'Физик'
    ]
    return render_template('list_prof.html', **param)


@app.route('/answer')
def answer():
    param = {}
    param['title'] = 'answer'
    param['surname'] = surname
    param['name'] = name
    param['education'] = education
    param['profession'] = profession
    param['sex'] = sex
    param['motivation'] = motivation
    param['ready'] = ready
    return render_template('answer.html', **param)


@app.route('/auto_answer', methods=['POST', 'GET'])
def auto_answer():
    global title, surname, name, education, profession, sex, motivation, ready
    if request.method == 'GET':
        return render_template('auto_answer.html')
    elif request.method == 'POST':
        surname = request.form.get('surname')
        name = request.form.get('name')
        profession = request.form.get('profession')
        education = request.form.get('education')
        sex = request.form.get('sex')
        motivation = request.form.get('motivation')
        ready1 = request.form.get('ready')
        ready = True if ready1 == 'on' else False
        return "Форма отправлена"


# @app.route('/odd_even')
# def odd_even():
#     return render_template('odd_even.html', number=3)
#
#
# @app.route('/news')
# def news():
#     with open("data/news.json", "rt", encoding="utf8") as f:
#         news_list = json.loads(f.read())
#     print(news_list)
#     return render_template('news.html', news=news_list)
#
#
# @app.route('/queue')
# def queue():
#     param = {}
#     param['title'] = 'Кто стоит в очереди?'
#     return render_template('queue.html', **param)
#
#
# @app.route('/success', methods=['GET', 'POST'])
# def success():
#     param = {}
#     param['title'] = 'Успешно'
#     return render_template('login.html', **param)
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         return redirect('/success')
#     return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
