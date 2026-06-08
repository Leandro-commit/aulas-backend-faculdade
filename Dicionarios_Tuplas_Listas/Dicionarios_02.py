game = {"nome": "Super Mario", "desenvolvedora": "Nintendo", "ano": 1990}

print(game.values())

for values in game.values():
    print(values)

print(game.keys())

for keys in game.keys():
    print(keys)

print(game.items())

for keys, values in game.items():
    print(f"{keys} = {values}")
