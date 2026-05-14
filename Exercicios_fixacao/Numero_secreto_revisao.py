numero_secreto = 8
tentativas = 0

while True:
    try:
        palpite = int(input("Qual seu palpite entre 0-25? "))
    except ValueError:
        print("Digite apenas números!")
        continue

    if palpite > 25:
        print("É aceito apenas palpites entre 0-25!")
        continue

    tentativas += 1

    if palpite < numero_secreto:
        print("Palpite menor que o número secreto!")

    elif palpite > numero_secreto:
        print("Palpite maior que o número secreto!")

    else:
        print(f"Parabéns, você acertou em {tentativas} tentativa(s)!")
        break
