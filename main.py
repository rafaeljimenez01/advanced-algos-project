#Encontrar palindromos
#######################################
# Expand in both directions of `low` and `high` to find all palindromes
def expand(s, low, high, palindromes):
    # run till `s[low.high]` is not a palindrome
    while low >= 0 and high < len(s) and s[low] == s[high]:
        # añade los palindromos a un set y verifica que sean palindromos
        # mayores a 4 carácteres
        if(len(s[low: high + 1])>3):
            palindromes.add(s[low: high + 1])

        # Expande en ambas direcciones
        low = low - 1
        high = high + 1


# Función para encontrar todos los palindromos unicos de un string
def findPalindromicSubstrings(s):
    # Crea un set vacio para guardar todos los palindromos únicos
    palindromes = set()

    for i in range(len(s)):


        # Encuentra todos los palindromos impares con s[i] como punto medio
        expand(s, i, i, palindromes)

        # Encuentra todos los palindromos pares con s[i] y s[i+1] como punto medio
        expand(s, i, i + 1, palindromes)

    # Imprime todos los palindromos unicos
    print(palindromes, end='')
#########################################################



if __name__ == '__main__':
    text_file = open("ejemplo.txt", "r")
    main_string = text_file.read().replace('\n', '')
    text_file.close()
    s = main_string
    findPalindromicSubstrings(s)
