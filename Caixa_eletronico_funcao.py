saldo = 1000


def mostrar_menu():
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")


def ver_saldo():
    global saldo
    print(f"Saldo atual: R$ {saldo:.2f}")


def depositar():
    global saldo
    valor = float(input("Valor do depósito: R$ "))

    if valor > 0:
        saldo += valor
        print("Depósito realizado!")
    else:
        print("Valor inválido!")


def sacar():
    global saldo
    valor = float(input("Valor do saque: R$ "))

    if valor <= saldo:
        saldo -= valor
        print("Saque realizado!")
    else:
        print("Saldo insuficiente!")


while True:
    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        ver_saldo()

    elif opcao == "2":
        depositar()

    elif opcao == "3":
        sacar()

    elif opcao == "4":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
