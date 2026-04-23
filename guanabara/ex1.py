def calcular_imposto(vendas: int = 100):
    if vendas > 50:
        imposto = vendas * 0.25
    elif vendas > 25:
        imposto = vendas * 0.15
    else:
        imposto = 0
    return imposto

valor = int(input('Digite o valor do produto: '))

imposto = calcular_imposto(valor)

print(f'O imposto que você irá pagar pelo produto é de R${imposto}')
