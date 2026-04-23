x = input('Digite uma letra ou digito: ')
if x.isdigit():
    print('Você digitou um NÚMERO')
elif x in ['a', 'e', 'i', 'o', 'u']:
    print('Você digitou uma VOGAL')
else:
    print('Você digitou uma CONSOANTE')
