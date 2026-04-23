def e_palindromo(palavra: str) -> bool:
    p = palavra.strip().lower().replace(' ', '')
    return p == p[::-1]

print(e_palindromo('vaga de estagio'))
print(e_palindromo('python'))
