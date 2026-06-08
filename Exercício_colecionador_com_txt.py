def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x


def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, "wt+")  # wt para escrita e o + de atualização
        a.close()
    except:
        print("Erro na criação do arquivo.")
    else:
        print(f"Arquivo {nomeArquivo} criado com sucesso!\n")


def cadastrarJogo(nomeArquivo, Nomejogo, plataforma):
    try:
        a = open(nomeArquivo, "at")  # at eu abre pra escrita mantendo o conteúdo
    except:
        print("Erro ao abrir o arquivo.")
    else:
        a.write(f"Nome: {nomeJogo}\nPlataforma: {plataforma}\n")
    finally:
        a.close()


def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, "rt")
    except:
        print("Erro ao ler o arquivo.")
    else:
        print(a.read())
    finally:
        a.close()


# programa principal
arquivo = "games.txt"
if existeArquivo(arquivo):
    print("Arquivo localizado no computador.")
else:
    print("Arquivo inexistente.")
    criarArquivo(arquivo)

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar novo item")
    print("2 - Listar cadastros")
    print("3 - Sair")

    op = valida_int("\nEscolha a opção desejada: ", 1, 3)
    if op == 1:  # Novo item
        print("Opção de cadastrar novo item selecionada...\n")
        nomeJogo = input("Nome do jogo: ")
        plataforma = input("Plataforma: ")
        cadastrarJogo(arquivo, nomeJogo, plataforma)

    elif op == 2:  # Listar
        print("Opção de listar selecionada...\n")
        listarArquivo(arquivo)

    elif op == 3:
        print("Encerrando o programa...")
        break
