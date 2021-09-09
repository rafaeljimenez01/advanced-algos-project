class Palindrome:
    def __init__(self, word, start, origin):
        self.origin = origin
        self.word = word
        self.start = start

    def __str__(self):
        return self.origin + " " + self.word + " " + str(self.start) + "\n"