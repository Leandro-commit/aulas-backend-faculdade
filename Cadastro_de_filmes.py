filmes_cadastrados = []


def mostrar_menu():

    print("\n===== MENU =====")
    print("1. Cadastrar filme")
    print("2. Listar filmes")
    print("3. Buscar filme pelo nome")
    print("4. Remover filme")
    print("5. Editar filme")
    print("6. SAIR\n")


def cadastrar_filme():

    nome_filme = input("Nome do filme: ").strip()
    genero = input("Gênero: ").strip()

    cadastro = {"nome": nome_filme, "genero": genero}

    filmes_cadastrados.append(cadastro)

    print("Filme cadastrado com sucesso!")


def editar_filmes():
    nome = input("Digite o nome do filme que deseja editar: ").strip()

    encontrado = False

    for filme in filmes_cadastrados:
        if filme["nome"].lower() == nome.lower():

            print(f"\nFilme encontrado: {filme['nome']} ({filme['genero']})")

            novo_nome = input("Novo nome (Enter para manter): ").strip()
            novo_genero = input("Novo gênero (Enter para manter): ").strip()

            if not novo_nome and not novo_genero != "":
                print("Nenhuma alteração realizada")
                encontrado = True
                break

            if novo_nome:
                filme["nome"] = novo_nome

            if novo_genero:
                filme["genero"] = novo_genero

            print("Filme editado com sucesso!")
            print(f"Nome: {filme['nome']} ({filme['genero']})")

            encontrado = True
            break

    if not encontrado:
        print("Filme não encontrado!")


def listar_filmes():
    if not filmes_cadastrados:
        print("Nenhum filme cadastrado!")
        return
    for cadastro in filmes_cadastrados:
        print("-" * 20)
        print(f"Nome: {cadastro['nome']} ({cadastro['genero']})")


def buscar_filmes():
    nome = input("Digite o nome do filme: ").strip().lower()

    encontrado = False

    for filme in filmes_cadastrados:
        if filme["nome"].lower() == nome:
            encontrado = True
            print("Filme encontrado:")
            print(f"Nome: {filme['nome']} ({filme['genero']})")
            break

    if not encontrado:
        print("Filme não encontrado!")


def remover_filme():
    remover_filme = input("Digite o nome do filme que deseja remover: ").strip()

    encontrado = False

    for filme in filmes_cadastrados:
        if filme["nome"].lower() == remover_filme.lower():
            filmes_cadastrados.remove(filme)
            encontrado = True
            print("Filme removido!")
            break

    if not encontrado:
        print("Filme não encontrado!")


while True:
    mostrar_menu()
    try:
        opcao = int(input("Digite uma opção: "))
    except ValueError:
        print("Digite apenas números!")
        continue

    if opcao not in (1, 2, 3, 4, 5, 6):
        print("Opção inválida!")
        continue

    if opcao == 1:
        cadastrar_filme()

    elif opcao == 2:
        listar_filmes()

    elif opcao == 3:
        buscar_filmes()

    elif opcao == 4:
        remover_filme()

    elif opcao == 5:
        editar_filmes()

    elif opcao == 6:
        print("Encerrando...")
        break
