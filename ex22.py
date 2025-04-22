numero = int(input("Digite um número: "))

if numero <= 1:
    print(f"{numero} não é primo.")
elif numero == 2:
    print("2 é primo.")
elif numero % 2 == 0:
    print(f"{numero} não é primo (divisível por 2).")
else:
    primo = True 
    for i in range(3, numero, 2):  
        if numero % i == 0:
            primo = False
            break  
    if primo:
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")
        