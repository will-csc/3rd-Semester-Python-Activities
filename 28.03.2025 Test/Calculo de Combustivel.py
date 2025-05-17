def melhor_opcao(preco_gas,preco_alcool):
    perc_70_gasolina = preco_gas * 0.7
    if preco_alcool <= perc_70_gasolina:
        print("Está mais vantajoso abastecer com alcool")
    else:
        print("Está mais vantajoso abastecer com gasolina")
    
    print(f"\n70% do Preço da Gasolina -> {perc_70_gasolina}\nPreço do Alcool -> {preco_alcool}")

while True:
    preco_gas = float(input("Digite o preço da gasolina: "))
    preco_alcool = float(input("Digite o preço do alcool: "))

    #Corrija possíveis erros
    if preco_alcool < 1 or preco_gas < 1:
        print("\nOs preços foram digitados de maneira errônea, corrija\n")
        continue
    
    melhor_opcao(preco_gas,preco_alcool)
    cond = input("Desejar continuar? (Digite Y para Sim): ").upper()
    if cond != 'Y':
        break

