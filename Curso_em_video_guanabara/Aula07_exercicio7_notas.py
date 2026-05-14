name1 = input("Aluno 01: Qual seu nome? ")
n1 = float(input(f"Qual foi sua nota,{name1}? "))
print("Obrigado pela reposta!")
#
name2 = input("Aluno 02: Qual seu nome? ")
n2 = float(input(f"Qual foi sua nota,{name2}? "))
print(
    "Obrigado, pela resposta! \nAgora somaremos a média de ambos e em seguida a mostraremos na tela:"
)
media = (n1 + n2) / 2
print(f"A média das notas é {media}")

# Podemos usar :.1f para usar apenas duas casas no resultado
