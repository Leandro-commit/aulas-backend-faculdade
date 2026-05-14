carrinho = []

while True:

    print("\n1 - Registrar produto")
    print("2 - Listar e remover produtos")
    print("3 - Sair\n")

    # ---INVÁLIDAR INSERÇÃO DE LETRAS E CÓDIGOS---
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números!")
        continue

    # ---INSERIR PRODUTO---
    if opcao == 1:
        produto = input("Nome do produto: ")
        preco = float(input("Preço: ").replace(",", "."))
        qtd = int(input("Quantidade: "))

        registro = {"nome": produto, "preco": preco, "quantidade": qtd}
        carrinho.append(registro)
        print("\nProduto adicionado!")

    # ---LISTAGEM E REMOÇÃO---
    elif opcao == 2:
        if not carrinho:
            print("\nNenhum produto registrado.")

        else:
            print("\nProdutos no carrinho:")
            for i, item in enumerate(carrinho, start=1):
                print(
                    f"\n{i} - Nome: {item['nome']} | "
                    f"Preço: R$ {item['preco']:.2f}".replace(".", ",")
                    + f" | Quantidade: {item['quantidade']}"
                )
            print("\nDigite 0 para sair ou...")
            remover = int(input("Digite o número do produto que deseja remover: "))

            if remover >= 1 and remover <= len(carrinho):
                produto_removido = carrinho.pop(remover - 1)
                print(f"\n{produto_removido['nome']} foi removido do carrinho!")
            elif remover == 0:
                print("Voltando ao menu...")
            else:
                print("\nNúmero inválido")

    # ---SAIR E INVALIDAÇÃO---
    elif opcao == 3:
        break
    else:
        print("\nOpção inválida. Tente novamente.")
