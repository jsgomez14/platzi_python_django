from flask import render_template,session,flash,redirect,url_for
from app.forms import LoginForm

from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': LoginForm(),
    }

    if login_form.validate_on_submit():
        session['username'] = login_form.username.data
        flash('Nombre de usuario registrado con éxito!')
        return redirect(url_for('index'))

    return render_template('login.html', **context)