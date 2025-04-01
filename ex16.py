km_percorridos= float(input("Qual foi a quantidade de km percorridos pelo carro?"))
dias_alugado= float(input("Quantos dias o carro ficou alugado?"))

preço_pagar= (60 * dias_alugado) + (0.15 * km_percorridos)

print(f"O preço a pagar pelo carro alugado foi R${preço_pagar:.2f}")
