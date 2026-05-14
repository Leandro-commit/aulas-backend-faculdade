numero_secreto = 16
tentativas = 0

while True:
    chute = int(input("Adivinhe o número secreto entre 0-20: "))
    tentativas += 1

    if chute > 20 or chute < 0:
        print("Digite um número entre 0 e 20")
    elif chute < numero_secreto:
        print("Muito baixo! Tente de novo.")
    elif chute > numero_secreto:
        print("Muito alto! Tente de novo.")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s)!")
        break
