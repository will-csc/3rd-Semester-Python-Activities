import mysql.connector

#------------ Função Para Criar Conexão ---------------
def connection():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="toor",
        database="agenda"
    )
    return conexao, conexao.cursor()

#------------ Classe do usuário ---------------
class User():
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = int(telefone)
        self.id = None  # só será atribuído depois do sign_up
        self.contatos = {}
        sign_up(self)


    def add_contact(self, nome, user):
        self.contatos[nome] = user
        conexao, cursor = connection()
        query = "INSERT INTO contacts (id_owner, id_contact) VALUES (%s, %s)"
        cursor.execute(query, (self.id, user.id))
        conexao.commit()
        conexao.close()

    def delete_contact(self, nome):
        if nome in self.contatos:
            contato = self.contatos[nome]
            conexao, cursor = connection()
            query = "DELETE FROM contacts WHERE id_owner = %s AND id_contact = %s"
            cursor.execute(query, (self.id, contato.id))
            conexao.commit()
            conexao.close()
            del self.contatos[nome]  

    def menu(self):
        while True:
            print("\n====== MENU ======")
            print("1. Atualizar dados do usuário")
            print("2. Adicionar contato")
            print("3. Remover contato")
            print("4. Deletar o seu usuário")
            print("5. Mostrar todos contato")
            print("6. Pesquisar contato")
            print("7. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("Obs: Caso não queira um dos campos, deixe vazio")
                nome = input("Novo nome: ")
                email = input("Novo email: ")
                telefone = input("Novo telefone: ")
                self.nome = nome
                self.email = email
                self.telefone = telefone
                update_information(self)

            elif opcao == "2":
                if self:
                    nome = input("Nome do contato: ")
                    email = input("Email do contato: ")
                    telefone = input("Telefone do contato: ")
                    contato = User(nome, email, telefone)
                    self.add_contact(nome, contato)
                    print("\nContato adicionado com sucesso.")
                else:
                    print("\nCadastre um usuário primeiro.")

            elif opcao == "3":
                if self:
                    nome = input("Nome do contato para remover: ")
                    if self.contatos[nome]:
                        self.delete_contact(nome)
                        print("\nContato removido com sucesso.")
                    else:
                        print("\nEsse contato não existe")
                else:
                    print("\nCadastre um usuário primeiro.")

            elif opcao == "4":
                delete_user(self.id)
                self = None
                break
            
            elif opcao == "7":
                print("\nEncerrando o programa.")
                break
            
            elif opcao == "5":
                self.show_all_contacts()
            
            elif opcao == "6":
                nome = input("Digite o nome do contato: ")
                self.search_user(nome)
            
            else:
                print("\nOpção inválida, tente novamente.")

    def show_all_contacts(self):
        print("\nSeus contatos:")
        for i, (key, user) in enumerate(self.contatos.items(), 1):
            print(f"{i} | Nome: {key} ---> Email: {user.email}, Telefone {user.telefone}")
    
    def search_user(self,nome):
        new_nome = self.contatos[nome].nome
        email = self.contatos[nome].email
        telefone = self.contatos[nome].telefone

        print(f"Nome: {new_nome} ---> Email: {email}, Telefone {telefone}\n")

"""
users -> id, nome, email, telefone
"""

def turn_off(cursor,conexao):
    cursor.close()
    conexao.close()

def sign_up(user):
    conexao, cursor = connection()

    # Verifica se o usuário já existe
    query = "SELECT id FROM users WHERE email = %s"
    cursor.execute(query, (user.email,))
    existing_user = cursor.fetchone()

    if existing_user:
        user.id = existing_user[0]  # Atribui o id do usuário existente
        print("Usuário já existe!")
    else:
        # Cria novo usuário
        insert_query = "INSERT INTO users (nome, email, telefone) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (user.nome, user.email, user.telefone))
        conexao.commit()
        user.id = cursor.lastrowid  # Pega o ID gerado pelo banco
        print("Usuario cadastrado com sucesso!")

    turn_off(cursor, conexao)

def update_information(user):
    conexao, cursor = connection()

    campos = []
    valores = []

    # Validação do e-mail
    if user.email.strip():
        if "@" not in user.email or len(user.email) < 6:
            print("\nErro: O e-mail informado é inválido.")
            return
        campos.append("email = %s")
        valores.append(user.email)

    # Validação do nome
    if user.nome.strip():
        if len(user.nome) < 3:
            print("\nErro: Digite um nome com pelo menos 3 caracteres.")
            return

        campos.append("nome = %s")
        valores.append(user.nome)
    
    # Validação do telefone
    if user.telefone.strip():
        if not user.telefone.isdigit() or len(user.telefone) != 11:
            print("Erro: Digite um telefone válido com exatamente 11 dígitos numéricos.")
            return
        campos.append("phone = %s")
        valores.append(user.telefone)

    # Nenhum campo preenchido
    if not campos:
        print("Aviso: Nenhum campo foi preenchido para atualizar.")
        return

    # Montar e executar query
    query = f"UPDATE users SET {', '.join(campos)} WHERE id = %s"
    valores.append(user.id)

    cursor.execute(query, tuple(valores))
    conexao.commit()
    print("Sucesso: Dados alterados com sucesso!")

def delete_user(id):
    conexao, cursor = connection()

    # Preparar e executar o DELETE
    query = (
        "DELETE FROM users "
        "WHERE id = %s"
    )

    cursor.execute(query, (id,))
    conexao.commit()
    print("\nO seu usuario foi deletado com sucesso")

def delete_all():
    conexao, cursor = connection()

    try:
        # Deleta todos os contatos primeiro (porque há foreign key referenciando users)
        cursor.execute("DELETE FROM contacts WHERE id > 0")

        # Deleta todos os usuários
        cursor.execute("DELETE FROM users ")

        conexao.commit()
        print("Todos os dados de 'contacts' e 'users' foram deletados com sucesso.")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao deletar os dados: {e}")
    finally:
        turn_off(cursor, conexao)
