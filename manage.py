from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return "HELLO WORLD"


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('/404/spaceman.svg'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)



