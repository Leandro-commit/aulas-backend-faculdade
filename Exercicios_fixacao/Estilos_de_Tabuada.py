# ## USANDO 2X O WHILE ##

# tabuada = 1
# while tabuada <= 10:
#     print("-" * 20)
#     print(f"TABUADA DO {tabuada}\n")
#     i = 1
#     while i <= 10:
#         print(f"{tabuada} x {i} = {tabuada * i}")
#         i += 1
#     tabuada += 1


# ## USANDO 2x O FOR ##

# for tabuada in range(1, 11):
#     print(f"TABUADA DO {tabuada}:")
#     for i in range(1, 11):
#         print(f"{tabuada} x {i} = {tabuada * i}")


## USANDO WHILE + FOR ##

tabuada = 1
while tabuada <= 10:
    print(f"TABUADA DO {tabuada}:")
    for i in range(1, 11, 1):
        print(f"{tabuada} x {i} = {tabuada * i}")
    tabuada += 1
