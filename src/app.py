from flask import Flask, render_template, request, session

from src.common.database import Database
from src.models.user import User

app = Flask(__name__)
app.secret_key = "123"


@app.route('/')
def home_template():
    return render_template('home.html')


@app.route('/login')    # www.mysite.com/api/login
def login_template():
    return render_template('login.html')


@app.route('/register')    # www.mysite.com/api/register
def register_template():
    return render_template('register.html')


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email=email, password=password):
        User.login(user_email=email)
    else:
        session['email'] = None

    return render_template("profile.html", email=session['email'])


@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(email=email, password=password)

    return render_template('profile.html', email=session['email'])


@app.route('blogs/<string:user_id>')
def user_blogs(user_id):
    user = User.get_by_id(user_id)
    user.get_blogs()

    render_template("user_blogs.html", blogs=user_blogs)


if __name__ == '__main__':
    app.run()
