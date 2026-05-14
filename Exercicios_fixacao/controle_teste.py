saldo = 0
movimentacoes = []

print("PLANILHA PESSOAL DE CONTROLE FINANCEIRO.")

while True:
    print("\n1 - Adicionar entrada (ganho)")
    print("2 - Adicionar saída (gasto)")
    print("3 - Ver saldo atual")
    print("4 - Listar movimentações")
    print("5 - Sair\n")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("*Digite apenas números (entre 1 e 5)*")
        continue

    if opcao not in (1, 2, 3, 4, 5):
        print("*Opção inválida (escolha entre 1 e 5)*")
        continue

    elif opcao == 1:
        entrada = float(input("Valor da entrada: R$ ").replace(",", "."))
        descricao = input("Adicione uma descrição: ")
        movimentacao = {"tipo": "entrada", "valor": entrada, "descricao": descricao}

        movimentacoes.append(movimentacao)
        saldo += entrada

        print("Entrada adicionada!")

    elif opcao == 2:
        saida = float(input("Valor da saída: R$ ").replace(",", "."))
        if saida > saldo:
            print("Sua retirada é maior que o saldo atual!")
            continue
        descricao = input("Adicione uma descrição: ")
        movimentacao = {"tipo": "saída", "valor": saida, "descricao": descricao}

        movimentacoes.append(movimentacao)
        saldo -= saida
        print(f"Retirada com sucesso! Saldo atualizado: {saldo:.2f}".replace(".", ","))

    elif opcao == 3:
        print(f"Saldo atual: {saldo:.2f}".replace(".", ","))

    else:
        if not movimentacoes:
            print("Nenhuma movimentação registrada.")
        else:
            print("\n--- HISTÓRICO DE MOVIMENTAÇÕES ---\n")

        for i, mov in enumerate(movimentacoes, start=1):
            print(
                f"{i}. {mov['tipo'].capitalize()} - R$ {mov['valor']:.2f} - {mov['descricao']}"
            )
