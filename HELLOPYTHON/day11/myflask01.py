from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/param', methods=['GET', 'POST'])
def param():
    if request.method == "POST":
        name = request.form.get('name', 'POST기본값')
    # name = request.args.get('name', 'user01')
    if request.method == "GET":
        name = request.args.get('name', 'GET기본값')
    return "param = " + name


if __name__ == '__main__':
    app.run()
