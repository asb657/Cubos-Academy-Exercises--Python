import math

diametro_esfera = 6

volume = 4/3 * math.pi * ((diametro_esfera/2)**3)

print("O volume de uma esfera de raio "+ str(round(diametro_esfera/2, 0)) + " é " + str(round(volume, 1)))
