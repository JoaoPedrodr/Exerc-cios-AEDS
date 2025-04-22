n = float(input("Digite o número para calcular a raiz quadrada: "))

b = 2.0
p = (b + n / b) / 2

while abs(n - p**2) >= 0.0001:
    b = p
    p = (b + n / b) / 2

print(f"Raiz quadrada aproximada de {n} é: {p:.5f}")