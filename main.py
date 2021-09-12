from palindorme import Palindrome

def has_malicious(trans, code, palindrome):
    index = trans.find(palindrome.word)

    if index != -1:
        left = trans.find(code[0:palindrome.start - 1], 0, index)
        right = trans.find(code[palindrome.end + 1:], index + len(palindrome.word))

        if index - left == len(code[0:palindrome.start]) and right == index + len(palindrome.word) + 1:
            print("True " + str(left + 1))
            return
        
    print(False)


#Encontrar palindromos
#######################################
# Expand in both directions of `low` and `high` to find all palindromes
def expand(s, low, high, palindromes, origin):
    # run till `s[low.high]` is not a palindrome
    while low >= 0 and high < len(s) and s[low] == s[high]:
        # añade los palindromos a un set y verifica que sean palindromos
        # mayores a 4 carácteres
        if(len(s[low: high + 1])>3):
            current_palindrome = s[low : high + 1]
            palindromes.add(Palindrome(current_palindrome, low, origin))

        # Expande en ambas direcciones
        low = low - 1
        high = high + 1


# Función para encontrar todos los palindromos unicos de un string
def findPalindromicSubstrings(s, file_name):
    # Crea un set vacio para guardar todos los palindromos únicos
    palindromes = set()

    for i in range(len(s)):


        # Encuentra todos los palindromos impares con s[i] como punto medio
        expand(s, i, i, palindromes, file_name)

        # Encuentra todos los palindromos pares con s[i] y s[i+1] como punto medio
        expand(s, i, i + 1, palindromes, file_name)

    # Imprime todos los palindromos unicos
    return palindromes

def read_file(file_name):
    text_file = open(file_name, "r")
    main_string = text_file.read().replace('\n', '')
    text_file.close()

    return main_string

    ### Longest palindrome algorithm ####
def UpdatedString(string):
    newString = ['#']
    for char in string:
        newString += [char, '#']
    return ''.join(newString)

def Manachen(string):
    string = UpdatedString(string)
    LPS = [0 for _ in range(len(string))]
    C = 0
    R = 0

    for i in range(len(string)):
        iMirror = 2 * C - i
        if R > i:
            LPS[i] = min(R - i, LPS[iMirror])
        else:
            LPS[i] = 0
        try:
            while string[i + 1 + LPS[i]] == string[i - 1 - LPS[i]]:
                LPS[i] += 1
        except:
            pass

        if i + LPS[i] > R:
            C = i
            R = i + LPS[i]

    r, c = max(LPS), LPS.index(max(LPS))

    current_palindrome = Palindrome(
        string[c - r: c + r].replace("#", ""),
        c - r,
        c + r
    )

    return current_palindrome


if __name__ == '__main__':
    mcode1 = read_file("mcode1.txt")
    mcode2 = read_file("mcode2.txt")
    mcode3 = read_file("mcode3.txt")
    trans1 = read_file("transmision1.txt")
    trans2 = read_file("transmision2.txt")

    palind1 = Manachen(mcode1)
    palind2 = Manachen(mcode2)
    palind3 = Manachen(mcode3)

    has_malicious(trans1, mcode1, palind1)
    has_malicious(trans1, mcode2, palind2)
    has_malicious(trans1, mcode3, palind3)
    has_malicious(trans2, mcode1, palind1)
    has_malicious(trans2, mcode2, palind2)
    has_malicious(trans2, mcode3, palind3)

    longestPalindrome1 = Manachen(trans1)
    longestPalindrome2 = Manachen(trans2)

    print("----- longest palindrome in transmission 1 ------")
    print(longestPalindrome1)
    print("----- longest palindrome in transmission 2 ------")
    print(longestPalindrome2)

