def moeda(valor):
    return f"{valor:.2f}".replace(".", ",")


peso = float(input("Qual o peso do pacote em kg: "))
print("-" * 30)
print("Tipo de envio:\n")
print("E. Econômico")
print("N. Normal")
print("EX. Expresso\n")
envio = input("Escolha a letra correspondente (E, N ou EX): ").upper()
print("-" * 30)

if envio == "E":
    if peso <= 5:
        frete = peso * 0.50
        print("Faixa de peso: Até 5kg")
    else:
        frete = peso * 0.80
        print("Faixa de peso: Acima 5kg")
    print("Tipo de envio: Econômico")
    print(f"Valor do frete: R$ {moeda(frete)}")

elif envio == "N":
    if peso <= 5:
        frete = peso * 0.90
        print("Faixa de peso: Até 5kg")
    else:
        frete = peso * 1.20
        print("Faixa de peso: Acima de 5kg")
    print("Tipo de envio: Normal")
    print(f"Valor do frete: R$ {moeda(frete)}")

elif envio == "EX":
    if peso <= 5:
        frete = peso * 1.50
        print("Faixa de peso: Até 5kg")
    else:
        frete = peso * 2.00
        print("Faixa de peso: Acima de 5kg")
    print("Tipo de envio: Expresso")
    print(f"Valor do frete: R$ {moeda(frete)}")

else:
    print("Opção inválida!")
