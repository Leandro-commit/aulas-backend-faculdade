while True:
    print("-" * 20)
    print("1 - resultador (+)")
    print("2 - Subtrair (-)")
    print("3 - Multiplicar (*)")
    print("4 - Dividir (/)")
    print("5 - Sair")
    print("-" * 20)
    try:
        escolha = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite uma opção numérica válida!")
        continue

    if escolha == 1:
        try:
            num1 = int(input("Escolha um número: "))
            num2 = int(input("Escolha outro número: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        resultado = num1 + num2
        print(f"Resultado: {resultado:,}".replace(",", "."))

    elif escolha == 2:
        try:
            num1 = int(input("Escolha um número: "))
            num2 = int(input("Escolha outro número: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        resultado = num1 - num2
        print(f"Resultado: {resultado:,}".replace(",", "."))

    elif escolha == 3:
        try:
            num1 = int(input("Escolha um número: "))
            num2 = int(input("Escolha outro número: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        resultado = num1 * num2
        print(f"Resultado: {resultado:,}".replace(",", "."))

    elif escolha == 4:
        try:
            num1 = int(input("Escolha um número: "))
            num2 = int(input("Escolha outro número: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        resultado = num1 / num2
        print(f"Resultado: {resultado:,.2f}".replace(",", "."))

    elif escolha == 5:
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
