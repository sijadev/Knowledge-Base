from glob import escape
from pathlib import Path
from flask import Flask, render_template

path = str(Path(__file__).parent.absolute())
app = Flask(__name__)


@app.route('/')
def index():
    return '<p>Hello ! ...</p>'


@app.route('/blog')
def blog():
    return '<p>Hier ist der Blog </p>'


@app.route('/<username>/<int:post_id>')
def user(username=None, post_id=None):
    return render_template('./user.html', name=username, post_id=post_id)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<username>')
def username(username):
    return 'User %s' % escape(username)


if __name__ == '__main__':
    app.run()
