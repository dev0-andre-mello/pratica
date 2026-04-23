def contador(text: str) -> int:

    vogais = 'aeiou'
    contador = 0
    for letra in text.lower():
        if letra in vogais:
            contador += 1
    return contador

print(contador('entrevista de emprego'))
