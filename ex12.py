salario_atual= float(input("Digite seu salário atual:"))
porcentagem_aumento= float(input("Digite a porcentagem de aumento:"))

aumento= (porcentagem_aumento / 100) * salario_atual

novo_salario= salario_atual + aumento

print(f"O valor do aumento foi: R$ {aumento:.2f}")
print(f"Novo salário é: R$ {novo_salario:.2f}")
