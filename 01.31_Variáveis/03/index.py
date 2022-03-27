saldo = float(80)
preco_tenis = float(100)

desconto = round((1 - saldo/preco_tenis) * 100, 2)

print("O desconto devera ser de " + str(desconto) + "%.")