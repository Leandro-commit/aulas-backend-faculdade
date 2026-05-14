salario = float(input("qual o seu salário? R$"))
novo = salario + (salario * 50 / 100)
valor_formatado = f"{novo:.2f}".replace(".", ",")
print(f"Seu salário com aumento de 15% será de R$ {valor_formatado}")
