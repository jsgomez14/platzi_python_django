from flask import Flask,request,make_response,redirect,render_template,url_for,flash,session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'HIPER SECRET'

todos = ['TODO 1', 'TODO 2', 'TODO 3']

class LoginFrom(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginFrom()
    username = session.get('username')
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form':login_form,
        'username': username,
    }

    if login_form.validate_on_submit():
        session['username'] = login_form.username.data
        flash('Nombre de usuario registrado con éxito!')
        return redirect(url_for('index'))

    return render_template('hello.html', **context)