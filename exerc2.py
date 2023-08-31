import math

nmrdez = float(input("Digite um numero com virgula entre 1 e 0: "))
base = int(input("Para qual base voce deseja converter? "))
nmrstr = str(nmrdez)

resultado = []

if (nmrdez < 0.0 or nmrdez > 1.0):
    print("O numero nao e valido")
else:
    for c in range(0, -8, -1):
        if nmrdez / math.pow(base, c):
            resultado.append(int(nmrdez // math.pow(base, c)))
            nmrdez = nmrdez % math.pow(base, c)
        else:
            resultado.append(0)
    print(nmrstr, "(10) = ", *resultado, "(", base, ")")