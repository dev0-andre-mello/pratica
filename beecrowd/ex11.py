n = int(input('valor: '))

print(n)

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    quantidade = n // nota
    print(f"{quantidade} nota(s) de R$ {nota},00")
    n = n % nota
