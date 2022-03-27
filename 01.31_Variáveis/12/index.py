montante = 90000
capital = 60000
periodos = 24


taxaJuros = ((montante/capital) ** (1/periodos) -1) * 100

print('O seu financiamento de R$ ' + str(capital) + ' reais teve uma taxa de juros de ' + str(round(taxaJuros, 2)) + ' %, pois após ' + str(periodos) + ' meses você teve que pagar R$ ' + str(montante) + ' reais.')