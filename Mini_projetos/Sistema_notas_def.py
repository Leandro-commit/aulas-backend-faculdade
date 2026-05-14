# **UM SISTEMA SIMPLES PARA TREINO DA FUNÇÃO DEF**

notas = []


def mostrar_menu():
    print("=== SISTEMA DE NOTAS ===\n")
    print("1. Adicionar nota")
    print("2. Ver média")
    print("3. Ver maior nota")
    print("4. Sair\n")


def adicionar_nota():
    try:
        nota = int(input("Adicione a nota: "))
    except ValueError:
        print("É aceito apenas números!")
        return

    if nota < 0 or nota > 10:
        print("Nota inválida!")
        return
    print("Nota adicionada com sucesso!")

    notas.append(nota)


def calcular_media():
    if len(notas) == 0:
        print("Nenhuma nota cadastrada!")
        return

    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media}")


def maior_nota():
    if len(notas) == 0:
        return

    maior = max(notas)
    print(f"A maior nota é: {maior}")


while True:
    mostrar_menu()

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números!")
        continue
    if opcao not in (1, 2, 3, 4):
        print("Opção inválida!")
        continue

    elif opcao == 1:
        adicionar_nota()

    elif opcao == 2:
        calcular_media()

    elif opcao == 3:
        maior_nota()

    else:
        print("Encerrando o programa...")
        break
