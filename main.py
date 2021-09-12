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
# Time Complexity: O(n^2).
def has_malicious(trans, code, palindrome):
    # Finds palindrome in transmission.
    index = trans.find(palindrome.word)

    # When palindrome is in the transmission.
    if index != -1:
        # Finds left & right secction of malicious code in transmission with
        # respect to palindrome in malicious code.
        left = trans.find(code[0:palindrome.start - 1], 0, index)
        right = trans.find(code[palindrome.end + 1:], index + len(palindrome.word))

        # When left & right secction of malicious code in transaction in the
        # right order; that is the same order consecutively as is in malicious
        # code.
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

    palind_mcode1 = Manachen(mcode1)
    palind_mcode2 = Manachen(mcode2)
    palind_mcode3 = Manachen(mcode3)
    palind_trans1 = Manachen(trans1)
    palind_trans2 = Manachen(trans2)

    # Part 1
    has_malicious(trans1, mcode1, palind_mcode1)
    has_malicious(trans1, mcode2, palind_mcode2)
    has_malicious(trans1, mcode3, palind_mcode3)
    has_malicious(trans2, mcode1, palind_mcode1)
    has_malicious(trans2, mcode2, palind_mcode2)
    has_malicious(trans2, mcode3, palind_mcode3)

    # Part 2
    print(str(palind_trans1.start + 1) + ' ' + str(palind_trans1.end + 1))
    print(str(palind_trans2.start + 1) + ' ' + str(palind_trans2.end + 1))

    # Part 3

    
