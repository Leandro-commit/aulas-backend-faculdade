while True:
    print("-" * 20)
    print("1 - Somar (+)")
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

    if escolha in (1, 2, 3, 4):
        try:
            num1 = int(input("Escolha um número: "))
            num2 = int(input("Escolha outro número: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if escolha == 1:
            resultado = num1 + num2
            print(f"Resultado: {resultado:,}".replace(",", "."))

        elif escolha == 2:
            resultado = num1 - num2
            print(f"Resultado: {resultado:,}".replace(",", "."))

        elif escolha == 3:
            resultado = num1 * num2
            print(f"Resultado: {resultado:,}".replace(",", "."))

        elif escolha == 4:
            if num2 == 0:
                print("Não é possível dividir por zero!")
                continue

            resultado = num1 / num2
            print(f"Resultado: {resultado:.2f}")

    elif escolha == 5:
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
