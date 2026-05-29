def validar_numero(numero):
    """
    Valida se o número é positivo.
    Retorna True se for válido.
    """

    if numero >= 0:
        return True

    else:
        return False


def fatorial(numero):

    resultado = 1

    for i in range(1, numero + 1):
        resultado *= i

    return resultado


num = int(input("Digite um número positivo: "))

if validar_numero(num):

    resultado_final = fatorial(num)

    print(f"O fatorial de {num} é {resultado_final}")

else:
    print("Digite apenas números positivos.")
