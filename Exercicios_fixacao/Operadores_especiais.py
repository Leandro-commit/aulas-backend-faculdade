# soma = 0
# conta = 1
# while conta <= 5:
#     x = int(input(f"Digite o {conta}º número: "))  # Alt + 0170 ou 0186
#     soma += x  # Equivalente: soma = soma + x
#     conta += 1  # Equivalente: conta = conta + 1
# print(f"Total: {soma}")


####### USANDO FOR ########

# soma = 0

# for conta in range(1, 11):
#     x = int(input(f"Digite o {conta}º número: "))
#     soma += x

# print(f"Total: {soma}")


####### USANDO SUM() ########

soma = sum(int(input(f"Digite o {i}º número: ")) for i in range(1, 6))

print(f"Total: {soma}")
