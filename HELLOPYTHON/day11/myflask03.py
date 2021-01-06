from flask import Flask
from flask import request
from flask.templating import render_template
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


@app.route('/forward.do')
def forward():
    title = "Good Morning"
    return render_template('myflask03forward.html', title=title)


if __name__ == '__main__':
    app.run()
