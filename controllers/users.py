from peewee import MySQLDatabase, Model, CharField, OperationalError

database = MySQLDatabase("intranet", host="localhost", port=3306, user="root", password = "root")

class User(Model):
    name = CharField()
    user = CharField( unique=True )
    cargo = CharField()
    email = CharField( index=True )
    ramal = CharField()
    pa = CharField()
    senha = CharField()


    class Meta:
        database = database
        db_table = 'Users'


class Agencies(Model):
    pa_num = CharField()
    pa_name = CharField( unique=True )
    pa_city = CharField()
    pa_address = CharField()
    pa_phone = CharField()


    class Meta:
        database = database
        db_table = 'Agencies'

if __name__ == "__main__":

    try:
        Agencies.create_table()
        print('Tabela Agencies criada com sucesso!')
    except OperationalError:
        print('Tabela Agencies ja existe!')
        
    
    for the_users in User.select():
        print('Base de usuarios selecionada')



