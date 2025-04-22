tabela = {
    1: 0.50,
    2: 1.00,
    3: 4.00,
    5: 7.00,
    9: 8.00
}

total = 0

while True:
    codigo = int(input("Digite o código do produto (ou digite 0 para finalizar): "))
    
    if codigo == 0:
        break
    
    if codigo in tabela:
        quantidade = int(input("Digite qual foi a quantidade comprada: "))
        parcial = tabela[codigo] * quantidade
        total = total + parcial  
    else:
        print("Código inválido")

print(f"Total das compras: R$ {total:.2f}")