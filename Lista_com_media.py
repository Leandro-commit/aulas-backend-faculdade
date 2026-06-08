notas = []

while True:
    nota = float(input("Digite uma nota (ou um valor negativo para para): "))
    if nota < 0:
        break
    notas.append(nota)

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"A média das notas digitadas é: {media:.2f}")
else:
    print("Nenhuma nota foi digitada!")
