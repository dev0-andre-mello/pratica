import string
import unicodedata

def text_cleaner(phrase):
    phrase = unicodedata.normalize('NFD', phrase)
    phrase = ''.join(c for c in phrase if unicodedata.category(c) != 'Mn')

    phrase = phrase.translate(str.maketrans('', '', string.punctuation))
    phrase = phrase.lower()

    return phrase

def transcript_analyzer(phrase):
    phrase = text_cleaner(phrase)
    words = phrase.split()
    word_count = len(words)
    return word_count
phrase = input('Digite uma frase: ')

result = transcript_analyzer(phrase)
print(f'Quantidade de palavras: {result}')

def contar_caracteres_sem_espaco(phrase):
    phrase = text_cleaner(phrase)
    frase_sem_espaco = phrase.replace(' ', '')
    word_count = len(frase_sem_espaco)
    return word_count
result = contar_caracteres_sem_espaco(phrase)
print(f'Quantidade de caracteres sem espaço: {result}')


def main():
    phrase = input('Digite uma frase: ')
    clean_phrase = text_cleaner(phrase)

    result_words = transcript_analyzer(clean_phrase)
    print(f'Quantidade de palavras: {result_words}')

    result_chars = contar_caracteres_sem_espaco(clean_phrase)
    print(f'Quantidade de caracteres sem espaço: {result_chars}')

if __name__ == '__main__':
    main()
