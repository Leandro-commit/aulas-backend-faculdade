alunos = []


def mostrar_menu():

    print("\n===== MENU =====")
    print("1. Cadastrar alunos")
    print("2. Listar alunos")
    print("3. Buscar aluno")
    print("4. Editar aluno")
    print("5. Remover aluno")
    print("6. SAIR\n")


def cadastrar_aluno():
    try:
        nome = input("Nome do aluno: ")
        for aluno in alunos:
            if aluno["nome"].lower() == nome.lower():
                print("Já existe um aluno com esse nome!")
                return
        if nome.strip() == "":
            print("Digite o nome do aluno!")
            return cadastrar_aluno()

        idade = int(input("Idade: "))

        curso = input("Curso: ")
        if curso.strip() == "":
            print("Digite o curso do aluno!")
            return cadastrar_aluno()

        cadastro = {"nome": nome, "idade": idade, "curso": curso}
        alunos.append(cadastro)
        print("Aluno cadastrado com sucesso!")

        return nome, idade, curso

    except ValueError:
        print("\n[Erro] Idade inválida! Digite apenas números. Recomeçando...\n")
        return cadastrar_aluno()  # Tenta novamente do início


def listar_aluno():
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return
    else:
        for i, aluno in enumerate(alunos, start=1):
            print("-" * 40)
            print(
                f"{i} - Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}"
            )


def buscar_aluno():
    nome = input("Digite o nome do aluno: ").strip().lower()

    encontrado = False

    for aluno in alunos:
        if aluno["nome"].lower() == nome:
            encontrado = True
            print("Aluno encontrado:")
            print(
                f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}"
            )
            break

    if not encontrado:
        print("Aluno não encontrado!")
        return


def editar_aluno():
    nome = input("Digite o nome do aluno que deseja editar: ").strip()

    encontrado = False

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print(
                f"\nAluno encontrado: {aluno['nome']} | {aluno['idade']} | {aluno['curso']}"
            )

            novo_nome = input("Digite o novo nome (Enter para manter): ")
            nova_idade = input("Digite a nova idade (Enter para manter): ")
            novo_curso = input("Digite o novo curso (Enter para manter): ")

            if not novo_nome and not nova_idade and not novo_curso != "":
                print("Nenhuma alteração realizada!")
                encontrado = True
                break

            if novo_nome:
                aluno["nome"] = novo_nome

            if nova_idade:
                aluno["idade"] = int(nova_idade)

            if novo_curso:
                aluno["curso"] = novo_curso

            print("Aluno editado com sucesso!")
            print(f"\n{aluno['nome']} | {aluno['idade']} | {aluno['curso']}")

            encontrado = True
            break

    if not encontrado:
        print("Aluno não encontrado!")


def remover_aluno():
    nome = input("Nome do aluno que deseja remover: ").strip()

    encontrado = False

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            encontrado = True
            confirmacao = input("Deseja realmente remover? (s/n): ")
            if confirmacao == "s":
                alunos.remove(aluno)
                print("Aluno removido com sucesso!")
            else:
                return

    if not encontrado:
        print("Aluno não encontrado")
        return mostrar_menu


while True:
    mostrar_menu()
    try:
        opcao = int(input("Escolha uma opção: "))

    except ValueError:
        print("Digite uma opção entre 1 e 6!")
        continue

    if opcao not in (1, 2, 3, 4, 5, 6):
        print("Opção inválida")
        continue

    if opcao == 1:
        cadastrar_aluno()

    elif opcao == 2:
        listar_aluno()

    elif opcao == 3:
        buscar_aluno()

    elif opcao == 4:
        editar_aluno()

    elif opcao == 5:
        remover_aluno()

    elif opcao == 6:
        print("Encerrando...")
        break
