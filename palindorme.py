class Palindrome:
    def __init__(self, word, start, end):
        self.word = word
        self.start = int(start / 2)
        self.end = int(end / 2)

    def __str__(self):
        return self.word + " " + str(self.start) + " " + str(self.end) + "\n"