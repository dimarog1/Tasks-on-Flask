from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/form_sample')
def form_sample():
    pass


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
