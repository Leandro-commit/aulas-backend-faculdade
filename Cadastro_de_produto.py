produtos = []


def mostrar_menu():
    print("\n===== MENU =====")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Buscar produto pelo nome")
    print("4. SAIR")


def cadastrar_produto():

    nome = input("Digite o nome do produto: ").strip().lower()

    produto = {"nome": nome}

    produtos.append(produto)

    print("Produto adicionado!")


def listar_produtos():
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(f"Nome: {produto['nome']}")


while True:
    mostrar_menu()

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números!")
        continue

    if opcao not in (1, 2, 3, 4):
        print("Opção inválida")
        continue

    elif opcao == 1:
        cadastrar_produto()

    elif opcao == 2:
        listar_produtos()

    elif opcao == 3:
        if not produtos:
            print("\nNenhum produto registrado.")

        else:
            produto = input("Digite o nome do produto: ").strip().lower()

            encontrado = False

            for item in produtos:
                if item["nome"] == produto:
                    print("Produto encontrado")
                    encontrado = True

            if not encontrado:
                print("Produto não encontrado.")

    else:
        print("Encerrando o programa...")
        break
