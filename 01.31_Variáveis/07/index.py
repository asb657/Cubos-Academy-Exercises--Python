populacao_inicial = float(1000)
pessoas_transmissao = float(4)
tempo = float(100)

infectados = round((populacao_inicial * pessoas_transmissao ** (tempo / 7) / (1 * 10**9)), 2)

print('O numero de infectados sera de ' + str(infectados) + ' bilhoes de pessoas.')