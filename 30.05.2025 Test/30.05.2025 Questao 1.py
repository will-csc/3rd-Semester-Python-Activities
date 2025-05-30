"""1)
Dada a seguinte lista:
minhaLista = [8, -13, 889, -6, -450, 10, 81]
faça um script Python para imprimir apenas os números positivos."""

# William C S de Carvalho
# RA 105637
# ADS3NC

mylist = [8, -13, 889, -6, -450, 10, 81]
mylist.sort(reverse=True)

print("Impressão do maior para o menor:\n")
for i,number in enumerate(mylist):
    if number > 0:
        print(f"{i+1} ---> {number}")
    else:
        break