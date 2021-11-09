import random
def fileMaker(file_name, n):
    alphabet = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','\n']
    file = open(file_name, "a")
    for i in range(0, n):
        file.write(alphabet[random.randint(0, len(alphabet)-1)])
    return True

# n = number of characters in file

n = 1000
file_name = 'ejemplo.txt' #Ruta del archivo

fileMaker(file_name, n)