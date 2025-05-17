import database as db

def create_user():
    print("Bem vindo ao melhor app de agenda!\n")
    print("Crie o seu usuario:")

    nome = input("Nome --> ")
    email = input("Email --> ")
    telefone = input("Telefone --> ")
    return db.User(nome,email,telefone)

usuario = create_user()
usuario.menu()
db.delete_all()
