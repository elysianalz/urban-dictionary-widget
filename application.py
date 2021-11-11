import dictionary

def main():
    word = ""
    while word != "c":
        word = input("enter word for definition: ")
        d = dictionary.Dictionary(word)
        d.getDefinition()
        #d.definition()
main()
