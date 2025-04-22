tabela_precos = {
    1: 0.50,
    2: 1.00,
    3: 4.00,
    5: 7.00,
    9: 8.00,
    100: 100.00  
}

total = 0.0

while True:
    try:
        codigo = int(input("Digite o código do produto (ou 0 para encerrar): "))
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
        continue

    if codigo == 0:
        break

    if codigo in tabela_precos:
        try:
            quantidade = int(input("Digite a quantidade comprada: "))
        except ValueError:
            print("Quantidade inválida! Digite um número inteiro.")
            continue

        subtotal = tabela_precos[codigo] * quantidade
        total = total + subtotal
    else:
        print("Código inválido")

print(f"Total da compra: R$ {total:.2f}")

# Pagamento e troco
while True:
    try:
        valor_pago = float(input("Digite o valor pago pelo cliente: R$ "))
        if valor_pago < total:
            print("Valor insuficiente. Por favor, insira um valor igual ou maior que o total.")
        else:
            troco = valor_pago - total
            print(f"Troco: R$ {troco:.2f}")
            break
    except ValueError:
        print("Entrada inválida! Digite um valor numérico.")