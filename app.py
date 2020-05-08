from flask import Flask, render_template, request, redirect, session
from controllers.DBcm import UseDatabase
from controllers.check_user import check_login
from controllers.users import User, Agencies
from routes.pa import pa
from routes.acc import acc
from datetime import datetime


current_date_time = datetime.now()
text_date_time = current_date_time.strftime('%H:%M - %d/%m/%Y ')


app = Flask(__name__)

app.config['dbconfig'] = { 
    'host': 'localhost',
    'user': 'vsearch',
    'password': '12345678',
    'database': 'intranet'
}

app.secret_key = 'wlu@2341!df$%'


@app.route('/')
def index():
    return render_template('login.html', the_title='Pagina de Login')


app.register_blueprint(pa)
app.register_blueprint(acc)


@app.route('/home')
@check_login
def home() -> 'html':
    print(text_date_time)
    return render_template('home.html',
                           the_title='Pagina Inicial',
                           date_time=text_date_time
                           )



@app.route('/login', methods=['POST'])
def do_login() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select user, senha
            from users"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
        user_login = request.form['login_user'], request.form['login_psw']
        if user_login in contents:
            
            session['logged_in'] = True

            return redirect('home')
        else:
            session.pop('logged_in')

    return render_template('login.html', the_alert='Usuário ou senha inválido')


@app.route('/logout')
def do_logout() -> 'html':
    session.pop('logged_in')
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='10.110.157.114', debug=True, port=8082)