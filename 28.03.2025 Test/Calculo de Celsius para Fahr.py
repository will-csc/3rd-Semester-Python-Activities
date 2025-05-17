while True:
    cel = float(input("Digite os graus em celsius: "))
    fahr = cel * 9 / 5 + 32
    
    print(f"Celsius {cel} -> Fahrenheit {fahr}")

    cond = input("Desejar continuar? (Digite Y para Sim): ").upper()
    if cond != 'Y':
        break