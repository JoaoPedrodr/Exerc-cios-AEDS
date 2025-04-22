n = int(input("Digite quantos números primos deseja ver: "))

contador = 0      # Conta quantos primos já foram encontrados
numero = 2        # Começa do primeiro primo

while contador < n:
    # Verifica se 'numero' é primo
    e_primo = True
    if numero > 2 and numero % 2 == 0:
        e_primo = False
    else:
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:
                e_primo = False
                break

    if e_primo:
        print(numero)
        contador += 1

    numero += 1