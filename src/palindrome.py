def is_palindrome(word: str):
    if word[0] == word[-1]:
        return True
    return False

def main():
    word = str(input("Dime una palabra o frase: "))
    if is_palindrome(word) == True:
        print('"' + word + '"' + " es palindromo")
    else:
        print('"' + word + '"' + " no es palindromo")

if __name__ == '__main__':
    main()