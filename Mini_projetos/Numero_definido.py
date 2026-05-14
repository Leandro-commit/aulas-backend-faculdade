numero_secreto = 7
tentativas = 0

print("-" * 41)
print("Tente acertar o número secreto de 0-100!!")
print("-" * 41)
chute = int(input("Qual o seu palpite? "))
tentativas += 1

while chute != numero_secreto:
    if chute < numero_secreto:
        print("Palpite menor que o número secreto!")
    elif chute > numero_secreto:
        print("Palpite maior que o número secreto!")

    chute = int(input("E aí, qual seu palpite? "))

    tentativas += 1
else:
    print(f"Parabéns! Você acertou em {tentativas} tentativas.")
