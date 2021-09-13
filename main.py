from palindorme import Palindrome

# INPUT:
#   - trans -> string (transmission).
#   - code -> string (malicious code).
#   - palindrome -> string.
# OUTPUT: None.
# DESCRIPTION: Finds malicious code insdie the transmision based on the longest
#              palindrome found in the malicious code. If the malicious code is
#              isn't found a False will be printed otherwise it will print true
#              and the possition (starting at 1) where the malicious code was
#              found.
# Time Complexity: O((n-m) * m) Where n is the transmission's length and m is
# the malicious code's length. 
def has_malicious(trans, code, palindrome):
    # Finds palindrome in transmission.
    index = trans.find(palindrome.word)

    # When palindrome is in the transmission.
    if index != -1:
        # code_left = code[0:palindrome.start - 1] # mcode left to the longest palindrome
        # code_right = code[palindrome.end + 1:] # mcdoe right to the longest palindrome

        # Finds left & right secction of malicious code in transmission
        # limitting the search to the length where they are suppose to be in
        # order for malicious code to be in transmission
        left = trans.find(
            code[0:palindrome.start - 1],
            index - palindrome.start - 1,
            index
        )
        right = trans.find(
            code[palindrome.end + 1:],
            index + (palindrome.end - palindrome.start) + 1,
            index + (palindrome.end - palindrome.start) + (len(code) - palindrome.end)
        )

        # Verifies that `left_code` & `right_code` are before and after,
        # respectively, the palindrome in the transmission. Confirming that the
        # mcode is in the transmission.
        if index - left == len(code[0:palindrome.start]) and right == index + len(palindrome.word) + 1:
            print("True " + str(left + 1))
            return

    # malicious code not found in transmission.
    print(False)


# INPUT: file_name -> string.
# OUTPUT: main_string -> string(file content)
# Description: Returns the file content.
def read_file(file_name):
    text_file = open(file_name, "r")
    main_string = text_file.read().replace('\n', '')
    text_file.close()

    return main_string


### Longest palindrome algorithm ####

# INPUT: string_file -> string (the string to convert)
# OUTPUT: converted_string -> string
# DESCRIPTION: This method returns a string with characters '#' in between
# Time Complexity: O(n) where n is the characters in the string
def updated_string(string_file):
    new_string_file = ['#']
    for char in string_file:
        new_string_file += [char, '#']
    converted_string = ''.join(new_string_file)
    return converted_string


# INPUT: string_file -> string (the string of the file we are working with)
# OUTPUT: current_palindrome -> is an instance of the palindrome class which saves the positions
#                               start and final of the longest palindrome
# DESCRIPTION: This method finds the longest palindrome in a string very efficiently
#               this approach takes advantage of properties of a palindrome to avoid
#               unnecessary computation.
# Time Complexity: O(n) where n is the length of the string
def manacher(string_file):
    string_file = updated_string(string_file)
    LPS = [0 for _ in range(len(string_file))]
    C = 0
    R = 0

    for i in range(len(string_file)):
        Mirror_i = 2 * C - i
        if R > i:
            LPS[i] = min(R - i, LPS[Mirror_i])
        else:
            LPS[i] = 0
        try:
            while string_file[i + 1 + LPS[i]] == string_file[i - 1 - LPS[i]]:
                LPS[i] += 1
        except:
            pass

        if i + LPS[i] > R:
            C = i
            R = i + LPS[i]

    r, c = max(LPS), LPS.index(max(LPS))

    current_palindrome = Palindrome(
        string_file[c - r: c + r].replace("#", ""),
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

    # Part 1
    palind1 = manacher(mcode1)
    palind2 = manacher(mcode2)
    palind3 = manacher(mcode3)

    has_malicious(trans1, mcode1, palind1)
    has_malicious(trans1, mcode2, palind2)
    has_malicious(trans1, mcode3, palind3)
    has_malicious(trans2, mcode1, palind1)
    has_malicious(trans2, mcode2, palind2)
    has_malicious(trans2, mcode3, palind3)

    # Part 2.
    longestPalindrome1 = manacher(trans1)
    longestPalindrome2 = manacher(trans2)

    print("----- longest palindrome in transmission 1 ------")
    print(str(longestPalindrome1.start) + ' ' + str(longestPalindrome1.end))
    print("----- longest palindrome in transmission 2 ------")
    print(str(longestPalindrome2.start) + ' ' + str(longestPalindrome2.end))

    # Part 3.
