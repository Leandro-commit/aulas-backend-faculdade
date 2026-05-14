while True:
    print("1 - Somar dois números")
    print("2 - Sair")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        num1 = int(input("Escolha um número: "))
        num2 = int(input("Escolha outro número: "))
        soma = num1 + num2
        print(f"Resultado: {soma}")
    elif escolha == 2:
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")
