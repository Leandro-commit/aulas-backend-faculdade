def moeda(valor):
    return f"{valor:.2f}".replace(".", ",")


kwh = float(input("Quantos kWh foram consumidos este mês? "))
print("-" * 30)
print("R. Residência\nI. Indústria\nC. Comércio\n")
local = input(
    "Escolha a letra correspondente ao tipo de instalação (R, I ou C): "
).upper()
print("-" * 30)

if local == "R":
    if kwh <= 500:
        consumo = kwh * 0.40
        print(f"Consumo até 500kWh = 0,40")
    else:
        consumo = kwh * 0.65
        print(f"Consumo acima de 500kWh = 0,65")
    print(f"Sua conta este mês foi de: R$ {moeda(consumo)}.")

elif local == "C":
    if kwh <= 1000:
        consumo = kwh * 0.55
        print(f"Consumo até 1.000kWh = 0,55")
    else:
        consumo = kwh * 0.60
        print(f"Consumo acima de 1.000kWh = 0,60")
    print(f"Sua conta este mês foi de: R$ {moeda(consumo)}.")

elif local == "I":
    if kwh <= 5000:
        consumo = kwh * 0.55
        print(f"Consumo até 5.000kWh = 0,55")
    else:
        consumo = kwh * 0.60
        print(f"Consumo acima de 5.000kWh = 0,60")
    print(f"Sua conta este mês foi de: R$ {moeda(consumo)}.")

else:
    print("Opção inválida!")
