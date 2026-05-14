numero_secreto = 7
tentativas = 0
limite = 5

while tentativas < limite:
    chute = int(input("Adivinhe o número entre 0 e 20: "))
    tentativas += 1
    if chute > 20 or chute < 0:
        print("Digite um número entre 0 e 20")
    elif chute > numero_secreto:
        print("Muito alto! Tenta novamente.")
    elif chute < numero_secreto:
        print("Muito baixo! Tenta novamente.")

    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s)")
        break

    resta = limite - tentativas
    if resta > 0:
        print(f"Você ainda tem {resta} tentativa(s).")
    else:
        print("Suas tentativas acabaram!")
