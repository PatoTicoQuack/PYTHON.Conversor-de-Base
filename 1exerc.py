import math

nmrdez = int(input("Digite um numero na base 10: "))
base = int(input("Para qual base voce deseja converter? "))
nmrstr = str(nmrdez)

resultado = []

if nmrdez >= math.pow(base, 8):
    print ("O numero ultrapassou os 8 digitos")
else:
    for c in range(7, -1, -1):
        if nmrdez / math.pow(base, c):
            resultado.append(int(nmrdez // math.pow(base, c)))
            nmrdez = nmrdez % math.pow(base, c)
        else:
            resultado.append(0)
    print (nmrstr, "(10) = ", *resultado, "(", base, ")")