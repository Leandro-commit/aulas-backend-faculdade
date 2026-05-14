saldo = 1000
vezes_deposito = 0
vezes_saque = 0


while True:

    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    escolha = int(input("Digite a opção desejada: "))

    if escolha not in (1, 2, 3, 4):
        print("Escolha inválida.")
        continue

    elif escolha == 1:
        print(
            f"Saldo atual: R$ {saldo:,.2f}".replace(",", "#")
            .replace(".", ",")
            .replace("#", ".")
        )

    elif escolha == 2:
        try:
            deposito = float(
                input("Qual valor deseja depositar? ")
                .replace(",", "#")
                .replace(".", ",")
                .replace("#", ".")
            )
            if deposito <= 0:
                print("Valor de deposito inválido!")
                continue
        except ValueError:
            print("É aceito apenas números!")
            continue
        saldo += deposito
        vezes_deposito += 1
        print(
            f"Deposito conclúido, Novo saldo total: R$ {saldo:,.2f}".replace(",", "#")
            .replace(".", ",")
            .replace("#", ".")
        )

    elif escolha == 3:
        try:
            saque = float(
                input("Qual valor deseja sacar? R$ ")
                .replace(",", "#")
                .replace(".", ",")
                .replace("#", ".")
            )
            if saque <= 0:
                print("Valor inválido!")
                continue
            elif saque > saldo:
                print("Quantia maior que seu saldo atual!")
                continue

        except ValueError:
            print("É aceito apenas números!")
        saldo -= saque
        vezes_saque += 1
        print(
            f"Saque conclúido, Saldo restante: R$ {saldo:,.2f}".replace(",", "#")
            .replace(".", ",")
            .replace("#", ".")
        )

    else:
        print("\nObrigado por utilizar nossos serviços.\n")
        print(f"Você fez {vezes_deposito} depósitos e {vezes_saque} saques.")
        print(
            f"Seu saldo final é de: R$ {saldo:,.2f}".replace(",", "#")
            .replace(".", ",")
            .replace("#", ".")
        )
        break
