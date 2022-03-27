import math

lados = 4

soma_angulos = (lados - 2) * 180
valor_angulo = soma_angulos / lados

if (lados > 2) :
    print("O valor da soma dos ângulos de um polígono de " + str(lados) + " lados é de " + str(soma_angulos) + " graus sendo cada um equivalente a " + str(valor_angulo) + " graus.")
else :
    print("Não existe polígonos com menos de 3 lados")


    
