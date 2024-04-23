phrase = input("Escribe una frase: ")

def word_counter(phrase):
    words = phrase.split()
    word_num = len(words)
    return word_num

print("La cantidad de palabras en tu frase es:", word_counter(phrase))