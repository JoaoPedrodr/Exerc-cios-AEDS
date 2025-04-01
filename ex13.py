mercadoria= float(input("Qual o preço da mercadoria?"))
percentual_desconto= float(input("Digite o percentual de desconto:"))

desconto= (percentual_desconto / 100) * mercadoria

preço_pagar= mercadoria - desconto

print(f"O valor do desconto foi: R$ {desconto:.2f}")
print(f"Preço a pagar: R$ {preço_pagar:.2f}")
