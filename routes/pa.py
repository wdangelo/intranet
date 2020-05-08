from flask import Blueprint, render_template, redirect, request, session

from controllers.check_user import check_login
from controllers.users import User, Agencies

pa = Blueprint('agencies', __name__, template_folder='templates')


@pa.route('/agencias')
@check_login
def cadastro_pa() -> 'html':
    return render_template('agencias.html')


@pa.route('/register-pa', methods=['POST'])
@check_login
def register_pa():
    agencies = Agencies.create(
        pa_num=request.form['pa_num'],
         pa_name=request.form['pa_name'],
         pa_city=request.form['pa_city'],
         pa_address=request.form['pa_address'],
         pa_phone=request.form['pa_phone'],)
    print(agencies)
    return redirect('viewagencies')


@pa.route('/del_pa/<int:id>')
@check_login
def del_agencies(id):
    query = Agencies.get(Agencies.id==id)
    query.delete_instance()
    return render_template('viewagencies.html', the_success='Agência excluída com sucesso!')


@pa.route('/viewagencies')
@check_login
def viewagencies():
    agencies = Agencies.select()
    titles = ('Nº', 'Nome', 'Cidade', 'Endereço', 'Telefone', 'Editar / Excluir ')
    return render_template('viewagencies.html', the_agencies=agencies, the_row_titles=titles, the_title='Agências')


@pa.route('/agenda')
@check_login
def agenda() -> 'html':
    agencies = Agencies.select()
    users = User.select()
    return render_template('agenda/pa00.html', the_users=users, the_agencies=agencies)


@pa.route('/pa00')
@check_login
def pa00() -> 'html':
    agencies = Agencies.select()
    users = User.select()
    return render_template('agenda/pa00.html', the_users=users, the_agencies=agencies)


@pa.route('/pa01')
@check_login
def pa01() -> 'html':
    agencies = Agencies.select()
    users = User.select()
    return render_template('agenda/pa01.html', the_users=users, the_agencies=agencies)


@pa.route('/pa02')
@check_login
def pa02() -> 'html':
    agencies = Agencies.select()
    users = User.select()
    return render_template('agenda/pa02.html', the_users=users, the_agencies=agencies)


@pa.route('/pa03')
@check_login
def pa03() -> 'html':
    agencies = Agencies.select()
    users = User.select()
    return render_template('agenda/pa03.html', the_users=users, the_agencies=agencies)


@pa.route('/pa04')
@check_login
def pa04() -> 'html':
    agencies = Agencies.select()
    users = User.select()
    return render_template('agenda/pa04.html', the_users=users, the_agencies=agencies)


@pa.route('/pa05')
@check_login
def pa05() -> 'html':
    agencies = Agencies.select()
    users = User.select()
    return render_template('agenda/pa05.html', the_users=users, the_agencies=agencies)


@pa.route('/pa99')
@check_login
def pa99() -> 'html':
    agencies = Agencies.select()
    users = User.select()
    return render_template('agenda/pa99.html', the_users=users, the_agencies=agencies)