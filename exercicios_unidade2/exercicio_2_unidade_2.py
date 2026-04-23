idade = int(input('Digite uma idade: '))
while(idade < 0 or idade > 130):
    idade = int(input('Idade inválida! Digite uma idade novamente: '))

print(f'Idade válida: {idade}')