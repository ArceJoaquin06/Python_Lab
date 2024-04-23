word = input("Escribe una palabra: ")
drow = ""

def palindrome(word, drow):
    i = len(word) -1
    while i >= 0:
        drow += word[i]
        i -= 1
        
    if word == drow:
        x = drow.capitalize()
        return f'{x} es una palabra palindromo'
    elif word != drow:
        y = word.capitalize()
        return f'{y} no es una palabra palindromo'

print(palindrome(word, drow))