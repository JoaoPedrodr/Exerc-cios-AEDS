dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

if divisor == 0:
    print("Divisão por zero não existe.")
else:
    resto = dividendo

    while resto >= divisor:
        resto = resto - divisor  
    print(f"O resto da divisão de {dividendo} por {divisor} é: {resto}")