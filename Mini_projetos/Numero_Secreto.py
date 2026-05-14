import random

while True:
    numero_secreto = random.randint(0, 20)
    tentativas = 0
    limite = 5

    print("\nNovo jogo iniciado ✅")

    while tentativas < limite:
        try:
            chute = int(input("\nDigite um número entre 0-20: "))
        except ValueError:
            print("Digite um número!")
            continue

        tentativas += 1

        if chute > 20 or chute < 0:
            print("Digite um número entre 0 e 20")

        elif chute < numero_secreto:
            print("Palpite menor que o número secreto!")
        elif chute > numero_secreto:
            print("Palpite maior que o número secreto!")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativa(s)")
            break

        resta = limite - tentativas
        if resta > 0:
            print(f"Restam {resta} tentativa(s).")
        else:
            print(f"Suas tentativas acabaram! O número secreto era {numero_secreto}.")

    jogar_novamente = input("\nQuer jogar novamente? (s/n): ").lower()
    if jogar_novamente != "s":
        print("Valeu por jogar!")
        break
