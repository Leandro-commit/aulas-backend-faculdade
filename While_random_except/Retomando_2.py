sacolao = []


def mostrar_menu():

    print("\n===== MENU =====\n")
    print("1. Cadastrar fruta")
    print("2. Listar frutas")
    print("3. Buscar fruta")
    print("4. Remover fruta")
    print("5. Editar fruta")
    print("6. SAIR\n")


def cadastrar_fruta():
    cadastro_fruta = input("Nome da fruta: ")
    preco = float(input("Preço do kg: ").replace(",", "."))

    cadastro = {"nome": cadastro_fruta, "preco": preco}
    sacolao.append(cadastro)

    print("Fruta cadastrada com sucesso!")


def listar_frutas():
    if not sacolao:
        print("Nenhuma fruta encontrada!")
        return

    for frutas in sacolao:
        print(f"Nome: {frutas['nome']}\nPreço: {frutas['preco'].replace(',','.')}")


def buscar_frutas():
    nome_fruta = input("Digite o nome da fruta: ")

    encontrado = False

    for frutas in sacolao:
        if frutas["nome"] == nome_fruta:
            encontrado = True
            print("Fruta encontrada!")
            print(f"Nome: {frutas['nome']} | Preço kg: {frutas['preco']}")
            break


cadastrar_fruta()
listar_frutas()
buscar_frutas()
