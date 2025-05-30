"""2)
faça uma função que recebe dois valores e mostra 
a diferença que tem entre os valores."""

# William C S de Carvalho
# RA 105637
# ADS3NC

def showDifference(n1: int,n2: int):
    print(f"As diferenças entre os números mostrados são: {abs(n1 - n2)}")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

showDifference(n1,n2)
