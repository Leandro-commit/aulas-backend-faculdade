filmes = []


def mostrar_menu():
    print("\n===== MENU =====")
    print("1. Cadastrar filme")
    print("2. Listar filmes")
    print("3. Buscar")
    print("4. Remover")
    print("5. Editar")
    print("6. SAIR\n")


def cadastrar_filme():
    nome = input("Nome do filme: ").strip()
    genero = input("Gênero: ").strip()

    cadastro = {"nome": nome, "genero": genero}

    filmes.append(cadastro)

    print("Filme cadastrado com sucesso!")


def listar_filme():
    if not filmes:
        print("Nenhum filme cadastrado!")
        return

    for filme in filmes:
        print("-" * 20)
        print(f"Nome: {filme['nome']}\nGênero: {filme['genero']}")


def buscar_filme():
    nome = input("Digite o nome do filme: ")

    encontrado = False

    for filme in filmes:
        if filme["nome"].lower() == nome:
            encontrado = True
            print("Filme encontrado!")
            print(f"Nome: {filme['nome']} | Gênero: {filme['genero']}")
            break

    if not encontrado:
        print("Filme não encontrado!")


def remover_filme():
    nome = input("Digite o nome do filme que deseja remover: ").strip()

    encontrado = False
    for filme in filmes:
        if filme["nome"].lower() == nome.lower():
            confirmacao = input("Tem certeza que deseja removê-lo (s/n): ")
            if confirmacao != "s" and "n":
                print("teste")
            filmes.remove(filme)
            encontrado = True
            print("Filme removido!")
            break

    if not encontrado:
        print("Filme não encontrado!")


def editar_filme():
    nome = input("Digite o filme que deseja editar: ")

    encontrado = False

    for filme in filmes:
        if filme["nome"].lower() == nome.lower():

            print(f"\nFilme encontrado: {filme['nome']} | Gênero {filme['genero']}")

            novo_nome = input("Novo nome (Enter para manter): ")
            novo_genero = input("Novo gênero (Enter para manter): ")

            if not novo_nome and not novo_genero != "":
                print("Nenhuma alteração realizada!")
                encontrado = True
                break

            if novo_nome:
                filme["nome"] = novo_nome

            if novo_genero:
                filme["genero"] = novo_genero

            print("Filme editado com sucesso!")
            print(f"Nome: {filme['nome']} | Gênero {filme['genero']}")

            encontrado = True
            break

        if not encontrado:
            print("Filme não encontrado!")


while True:
    mostrar_menu()

    try:
        opcao = int(input("Digite uma opção: "))
    except ValueError:
        print("Digite uma opção númerica do menu!")
        continue

    if opcao not in (1, 2, 3, 4, 5, 6):
        print("Opção inválida!")
        continue

    if opcao == 1:
        cadastrar_filme()

    elif opcao == 2:
        listar_filme()

    elif opcao == 3:
        buscar_filme()

    elif opcao == 4:
        remover_filme()

    elif opcao == 5:
        editar_filme()

    elif opcao == 6:
        print("Encerrando...")
        break
