def receber_dois_numeros_e_somar(n1: float, n2: float) -> float:

    soma = n1 + n2
    return soma

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro número: '))

result = receber_dois_numeros_e_somar(n1, n2)
print(f'A soma dos valores {n1} e {n2} é de: {result}')
