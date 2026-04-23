def receber_dados_de_cliente(nome: str, idade: int, genero: str):
    print(f'{nome} tem {idade} anos e é do sexo {genero}')

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
genero = input('Digite seu sexo: ')

receber_dados_de_cliente(nome, idade, genero)
