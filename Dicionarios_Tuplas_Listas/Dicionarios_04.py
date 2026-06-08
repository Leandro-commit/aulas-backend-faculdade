game = {}
games = []

# Para fazer a pergunta 3 vezes

for i in range(3):
    game["nome"] = input("Qual o nome do jogo? ")
    game["videogame"] = input("Para qual video-game ele foi lançado? ")
    game["ano"] = input("Qual o ano de lançamento? ")
    games.append(game.copy())
print("-" * 20)
for jogos in games:
    for chave, valor in jogos.items():
        print(f"O campo {chave} tem o valor {valor}.")
