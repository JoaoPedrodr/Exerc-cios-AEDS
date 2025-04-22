T = [-10, -8, 0, 1, 2, 5, -2, -4]

menor = T[0]
maior = T[0]
soma = 0
quantidade = 0

for temp in T:
    if temp < menor:
        menor = temp
    if temp > maior:
        maior = temp
    soma = soma + temp  
    quantidade = quantidade + 1  

media = soma / quantidade

print(f"Menor temperatura: {menor}°C")
print(f"Maior temperatura: {maior}°C")
print(f"Temperatura média: {media:.2f}°C")