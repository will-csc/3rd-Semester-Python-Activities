"""3)
Faça um script que solicite um login
“admin” e a senha “admin” e dê três
tentativas para o usuário, caso ele
acerte aparece “Usuário logado”
caso erre as três tentativas deve
aparecer “Usuário bloqueado”."""

# William C S de Carvalho
# RA 105637
# ADS3NC

guesses = 3

while True:
    user = input("Digite o nome do usuário: ")
    password = input("Digite a senha do usuário: ")
    
    if user == "admin" and password == "admin":
        print("\nUsuário logado!!")
        break
    elif guesses == 0:
        print("\nTentativas esgotadas!")
        break
    
    print(f"\nSenha errada! Restam {guesses} tentativas")
    guesses -= 1