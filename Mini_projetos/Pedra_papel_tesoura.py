import random

vitorias = 0
derrotas = 0
empates = 0

while True:
    computador = random.choice(["pedra", "papel", "tesoura"])

    print("\nNovo jogo iniciado ▶️")

    print("\n1. Pedra\n2. Papel\n3. Tesoura")
    jogada = input("\nEscolha uma opção: ")
    if jogada not in ["1", "2", "3"]:
        print("Jogada inválida")
        continue

    if jogada == computador:
        print("Empate")
        empates += 1

    elif (
        (jogada == "1" and computador == "tesoura")
        or (jogada == "3" and computador == "papel")
        or (jogada == "2" and computador == "pedra")
    ):
        print("Você ganhou ✅")
        vitorias += 1

    else:
        print("Você perdeu ❌")
        derrotas += 1

    print(f"Vitórias: {vitorias} | Derrotas: {derrotas} | Empates: {empates}")

    encerrar = input("\nDeseja continuar? (s/n): ").lower()
    if encerrar == "s":
        continue
    else:
        print("Obrigado por jogar!")
        break
