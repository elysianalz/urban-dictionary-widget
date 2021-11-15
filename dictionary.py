import scraper

class Dictionary:
    def __init__(self, word):
        self.word = word
        self.definitions = ["placeholder definition"]

    def printWord(self):
        print(self.word)

    def definition(self):
        print("\ndefinitions for " + self.word + ":\n")
        for d in self.definitions:
            print(d + "\n")

    def getDefinition(self):
        s = scraper.Scraper(self.word)
        res = s.getResponse()
        # word searched
        print(res[0])
        # meaning of word
        print(res[1][0].get_text())
        # example of use
        print(res[2][0].get_text())
