def func_maior(msg, *num):
    maior = 0
    for i in num:
        if i > maior:
            maior = i
    print(msg, maior)


# programa principal
func_maior("Maior: ", 8, 6, 4, 78, 600, 12, 9)
