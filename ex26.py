numero = int(input("Digite um número: "))
original = numero  
invertido = 0

while numero > 0:
    resto = numero % 10            # Pega o último dígito
    invertido = invertido * 10 + resto  # Constrói o número invertido
    numero = numero // 10          # Remove o último dígito do número

if original == invertido:
    print(f"{original} é um número palíndromo.")
else:
    print(f"{original} não é um número palíndromo.")