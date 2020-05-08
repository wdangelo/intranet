from flask import Blueprint, render_template, request
from controllers.check_user import check_login
from controllers.users import User, Agencies

acc = Blueprint('acc', __name__, template_folder='templates')


@acc.route('/user')
@check_login
def user():
    data_agencies = Agencies.select()
    return render_template('user.html', the_title='Cadastro de usuários', the_agencies=data_agencies)


@acc.route('/viewusers')
def view_users() -> 'html':
    titles = ('ID', 'Nome', 'Usuário', 'Cargo', 'E-mail', 'Ramal', 'PA', ' Editar  /  Excluir ', ' ')
    users = User.select()
    return render_template('viewusers.html',
                        the_title='Usuários',
                        the_row_titles=titles,
                        the_users=users)


@acc.route('/register', methods=['POST'])
def register() -> 'html':
    users = User.create(
        name=request.form['name'],
        user=request.form['user'],
        cargo=request.form['cargo'],
        email=request.form['email'],
        ramal=request.form['ramal'],
        pa=request.form['pa'],
        senha=request.form['pass'])
    return render_template('viewusers.html', the_success='Usuário cadastrado com sucesso', the_user=users)


@acc.route('/user_upgrade')
def user_upgrade() -> 'html':
    users = User.select()
    return render_template('user_upgrade.html', the_users=users)




@acc.route('/del_user/<int:id>')
@check_login
def del_user(id):
    query = User.get(User.id == id)
    query.delete_instance()
    return render_template('viewusers.html',
                            the_success='Usuário excluido com sucesso!')