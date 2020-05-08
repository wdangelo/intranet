from flask import session, render_template

from functools import wraps


def check_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return render_template('login.html', the_alert='Você precisa estar logado para acessar esta pagina!')
    return wrapper