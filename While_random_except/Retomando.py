livros_cadastrados = []


def mostrar_menu():

    print("\n===== MENU =====")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Buscar filme pelo nome")
    print("4. Remover filme")
    print("5. SAIR\n")


def cadastrar_livros():
    nome_livro = input("Nome do livro: ")
    editora = input("Editora: ")

    cadastro_livros = {"nome": nome_livro, "editora": editora}

    livros_cadastrados.append(cadastro_livros)

    print("Livro cadastrado com sucesso!")


def listar_livros():
    if not livros_cadastrados:
        print("Nenhum livro cadastrado!")

    for livros in livros_cadastrados:
        print("-" * 20)
        print(f"Nome: {livros['nome']}\nEditora: {livros['editora']}")


def buscar_livros():
    buscar = input("Digite o nome do filme que deseja buscar: ")

    encontrado = False

    for livros in livros_cadastrados:
        if livros["nome"] == buscar:
            encontrado = True
            print("Livro encontrado:\n")
            print(f"Nome: {livros['nome']} | Editora: {livros['editora']}")
            break

        else:
            if not encontrado:
                print("Livro não encontrado!")
                return 


def remover_livro():
    remover = input("Nome do filme que deseja remover: ")

    encontrado = False

    for livros in livros_cadastrados:
        if livros["nome"] == remover:
            encontrado = True
            confirmacao = input("Tem certeza que deseja removê-lo (s/n): ")
            if confirmacao == "s":
                livros_cadastrados.remove(livros)
                print("Livro removido com sucesso!")
                break

            else:
                cadastrar_livros()


while True:
    mostrar_menu()

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números!")

    if opcao not in (1, 2, 3, 4, 5):
        print("Opção inválida!")

    if opcao == 1:
        cadastrar_livros()

    elif opcao == 2:
        listar_livros()

    elif opcao == 3:
        buscar_livros()

    elif opcao == 4:
        remover_livro()

    elif opcao == 5:
        print("Encerrando...")
        break
