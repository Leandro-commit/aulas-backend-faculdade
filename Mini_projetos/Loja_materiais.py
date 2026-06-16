produtos = {
    "telha": 8.50,
    "furadeira": 108,
    "martelo": 15,
    "trena": 8.80,
    "tijolo": 2.00,
    "cimento": 38.90,
    "cal": 25.50,
    "bloco": 4.80,
    "argamassa": 29.90,
    "vergalhao": 65.00,
    "tinta": 189.90,
}


def mostrar_menu():
    print("\nSANTA CRUZ ACABAMENTOS")
    print("-" * 20)
    print("1 - Ver catálogo")
    print("2 - Comprar produto")
    print("3 - Sair\n")


def catalogo():
    for nome, preco in produtos.items():
        print(f"{nome.capitalize()} - R$ {preco:.2f}")


def comprar(produtos):
    while True:
        item = input("Qual produto deseja comprar? ").lower()

        if item in produtos:
            break

        print("Produto não encontrado!")

    qtd = int(input("Quantidade: "))

    total = produtos[item] * qtd

    print("\n===== COMPRA =====")
    print(f"Produto: {item.capitalize()}")
    print(f"Preço unitário: R$ {produtos[item]:.2f}")
    print(f"Quantidade: {qtd}")
    print(f"Total: R$ {total:.2f}")


# Outra forma de fazer:
#     if item in produtos:
#         total = produtos[item] * qtd
#         print(f"\nProduto: {item.capitalize()}")
#         print(f"Preço unitário R$ {produtos[item]:.2f}")
#         print(f"Quantidade: {qtd}")
#         print(f"Total: R$ {total:2f}")

#     else:
#         print("Produto não encontrado!")


while True:
    mostrar_menu()

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números!")
        continue

    if opcao not in (1, 2, 3):
        print("Escolha inválida!")

    if opcao == 1:
        catalogo()

    elif opcao == 2:
        comprar(produtos)

    elif opcao == 3:
        print("Encerrando...")
        break
