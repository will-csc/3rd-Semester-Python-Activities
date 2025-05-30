"""4)
Faça uma aplicação que peça o valor total da compra e se
o usuário necessita parcelar. Caso ele parcele imprima no
final o valor da parcela agora se for pagar a vista dê 5%
de desconto."""

# William C S de Carvalho
# RA 105637
# ADS3NC

def buy():
    valor_total = float(input("Digite o valor total da compra: R$ "))

    parcelar = input("Deseja parcelar a compra? (s/n): ").strip().lower()

    if parcelar == 's':
        parcelas = int(input("Em quantas vezes deseja parcelar? "))
        valor_parcela = valor_total / parcelas
        print(f"A compra será parcelada em {parcelas}x de R$ {valor_parcela:.2f}")
    else:
        valor_desconto = valor_total * 0.05
        valor_final = valor_total - valor_desconto
        print(f"Pagamento à vista. Valor com 5% de desconto: R$ {valor_final:.2f}")

buy()
