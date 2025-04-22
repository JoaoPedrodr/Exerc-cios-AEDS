while True:
    print("\n Menu")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Saindo do programa...")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida.")
        continue

    try:
        numero = int(input("Digite um número para ver a tabuada: "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        continue

    print("\nTabuada:")

    for i in range(1, 11):
        if opcao == "1":
            print(f"{numero} + {i} = {numero + i}")
        elif opcao == "2":
            print(f"{numero} - {i} = {numero - i}")
        elif opcao == "3":
            print(f"{numero} x {i} = {numero * i}")
        elif opcao == "4":
            if i != 0:
                print(f"{numero} / {i} = {numero / i:.2f}")