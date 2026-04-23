name = input('Digite seu nome: ')
password = input('Digite sua senha: ')

while password == name:
    print('Erro! A senha não pode ser igual ao nome!')
    password = input('Digite a senha novamente: ')
print('Acesso concedido!')
