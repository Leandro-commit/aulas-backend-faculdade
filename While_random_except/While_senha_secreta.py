senha = 1234
tentativas = 0
limite = 3

while tentativas < limite:
    chute = int(input("Adivinhe a senha de 4 digitos: "))
    tentativas += 1

    if chute == senha:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    else:
        restantes = limite - tentativas
        print("Senha incorrenta!")
        if restantes > 0:
            print(f"Você ainda tem {restantes} tentativas")
