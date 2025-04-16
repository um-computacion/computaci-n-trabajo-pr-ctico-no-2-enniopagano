import string

def is_palindrome(word: str):
    word = word.lower() # Para ignorar mayusculas y minisculas
    word = word.strip() # Para ignorar espacios en blanco
    word = word.translate(str.maketrans("", "", string.punctuation)) # Para ignorar signos de puntuacion
    if word != "":
        if word[0] == word[-1]:
            return True
        return False
    return False

def main():
    word = str(input("Dime una palabra o frase: "))
    if is_palindrome(word) == True:
        print('"' + word + '"' + " es palindromo")
    else:
        print('"' + word + '"' + " no es palindromo")

if __name__ == '__main__':
    main()