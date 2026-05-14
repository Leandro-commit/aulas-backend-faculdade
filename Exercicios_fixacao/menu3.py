while True:

    print("1 - Somar dois números")
    print("2 - Sair")
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

        soma = num1 + num2
        print(f"Resultado: {soma}")

    elif escolha == 2:
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
