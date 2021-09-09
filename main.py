from palindorme import Palindrome

class finder:
    def __init__(self):
        self.mcode1 = self.read_file("mcode1.txt")
        self.mcode2 = self.read_file("mcode2.txt")
        self.mcode3 = self.read_file("mcode3.txt")
        self.trans1 = self.read_file("transmision1.txt")
        self.trans2 = self.read_file("transmision2.txt")
        self.palindromes = self.findPalindromicSubstrings(self.mcode1, "mcode1")
        self.palindromes |= self.findPalindromicSubstrings(self.mcode2, "mcode2")
        self.palindromes |= self.findPalindromicSubstrings(self.mcode3, "mcode3")
    
        # for palindrome in self.palindromes:
        #     print(palindrome)


    #Encontrar palindromos
    #######################################
    # Expand in both directions of `low` and `high` to find all palindromes
    def expand(self, s, low, high, palindromes, origin):
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
    def findPalindromicSubstrings(self, s, file_name):
        # Crea un set vacio para guardar todos los palindromos únicos
        palindromes = set()

        for i in range(len(s)):


            # Encuentra todos los palindromos impares con s[i] como punto medio
            self.expand(s, i, i, palindromes, file_name)

            # Encuentra todos los palindromos pares con s[i] y s[i+1] como punto medio
            self.expand(s, i, i + 1, palindromes, file_name)

        # Imprime todos los palindromos unicos
        return palindromes
    #########################################################

    def read_file(self, file_name):
        text_file = open(file_name, "r")
        main_string = text_file.read().replace('\n', '')
        text_file.close()

        return main_string


if __name__ == '__main__':
   find = finder()
