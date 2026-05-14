usuario_correto = "admin"
senha_correta = "1234"
tentativas = 0
limite = 3

while tentativas < limite:
    usuario = input("Digite o usuário: ").lower()
    senha = input("Digite a senha: ")

    if usuario != usuario_correto and senha != senha_correta:
        print("Usuário e senha incorretos!")
    elif usuario != usuario_correto:
        print("Usuário incorreto!")
    elif senha != senha_correta:
        print("senha incorreta!")
    else:
        print("Acesso permitido...")
        break

    tentativas += 1
    resta = limite - tentativas

    if resta > 0:
        print(f"Restam {resta} tentativa(s)")

else:
    print("Acesso bloqueado! Tente novamente mais tarde.")
