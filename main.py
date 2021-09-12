from palindorme import Palindrome

# INPUT:
#   - trnas -> string (transmission).
#   - code -> string (malicious code).
#   - plaindrome -> string.
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
        # respectively, the palindomre in the transmission. COnfirming that the
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
def updated_string(string):
    newString = ['#']
    for char in string:
        newString += [char, '#']
    return ''.join(newString)

def manacher(string):
    string = updated_string(string)
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
