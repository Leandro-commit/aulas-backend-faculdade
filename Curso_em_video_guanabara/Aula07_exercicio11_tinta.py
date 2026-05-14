metros1 = float(input("Qual a altura da parede?").replace(",", "."))
metros2 = float(input("E a Comprimento?").replace(",", "."))
s = metros1 * metros2
litros = s / 2
area_formatada = f"{s:.2f}".replace(".", ",")
litros_formatada = f"{litros:.2f}".replace(".", ",")
print(f"Então sua parede tem {area_formatada}m².")
print(f"Você precisará de {litros_formatada} litros de tinta.")
