# Nome -> William C S de Carvalho
# RA -> 105637
# Turma -> Ads3nc
# Periodo -> Noturno

def salario_prof(nivel,horas):
    if nivel == 1:
        return horas * 18
    elif nivel == 2:
        return horas * 36
    else:
        return horas * 72
    
while True:
    nivel = 0
    horas = 0

    # Corrige possíveis erros
    while nivel < 1 or nivel > 3:
        print("\n----- Niveis de professores ----- \nNivel 1 -> 18/h \nNivel 2 -> 36/h \nNivel 3 -> 72/h")
        nivel = int(input("Digite o nível do professor conforme mostrado acima: "))
        if nivel not in range(1,4):
            print("\n\nDigite o nivel entre 1 e 3!!!\n\n")
    
    while horas < 1:
        horas = int(input("Digite as horas trabalhadas: "))
        if horas < 1:
            print("\n\n\nDigite uma hora valida!!!\n\n")
    
    # Imprime o Salario
    salario = salario_prof(nivel,horas)
    print(f"\nO salario do seu professor é: {salario}")

    cond = input("Desejar calcular mais algum salário? (Digite Y para Sim): ").upper()
    if cond != 'Y':
        break
    

    