jogos = []


def mostrar_menu():

    print("\n===== MENU =====")
    print("1. Cadastrar novo jogo")
    print("2. Listar jogos")
    print("3. SAIR\n")


def cadastrar_jogo():
    nome = input("Nome do jogo: ").strip()
    plataforma = input("Plataforma: ")

    descricao = {"nome": nome, "tipo": plataforma}

    jogos.append(descricao)

    print("Jogo cadastrado!")


def listar_jogos():
    if len(jogos) == 0:
        # Eu poderia colocar ''If not jogos:'' que seria a mesma coisa
        print("Nenhum jogo foi cadastrado.")
        return

    for descricao in jogos:
        print("-" * 20)
        print(f"Nome: {descricao['nome']}")
        print(f"Plataforma: {descricao['tipo']}\n")


while True:
    mostrar_menu()

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números!")
        continue

    if opcao not in (1, 2, 3):
        print("Opção inválida!")
        continue

    elif opcao == 1:
        cadastrar_jogo()

    elif opcao == 2:
        listar_jogos()

    else:
        print("Encerrando...")
        break
