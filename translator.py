from dictionary import Dictionary
class Translator:

    def __init__(self):
        self._dict = Dictionary() #crei un dizionario qui usando la classe Dizionario

#-------------------------------------------------------------------------------------------
    def printMenu(self):
        print("-------------------------------------------")
        print("      Translator Alien-Italian")
        print("-------------------------------------------")
        print(" 1. Aggiungi nuova parola")
        print(" 2. Cerca una traduzione")
        print(" 3. Cerca con wildcard")
        print(" 4. Stampa tutto il dizionario")
        print(" 5. Exit")
        print("-------------------------------------------")

# -------------------------------------------------------------------------------------------
    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        # prima pulisci dict cosicchè nella stampa non lo hai doppio
        self._dict.clear()
        infile = open("dictionary.txt", "r", encoding="utf-8")
        for line in infile:
            campi = line.strip().split(" ", 1)  # 1--> dividi solo una volta
            self._dict.addWord( campi[0], campi[1])          # aggiungo dentro il dizionario che ho creato vuoto tutte le parole
        infile.close()

# -------------------------------------------------------------------------------------------
    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        wild, ita = entry
        if not wild.isalpha():
            print("Si accettano solo caratteri alfabetici")
        else:
            for it in ita:
                if not it.isalpha():
                    print("Si accettano solo caratteri alfabetici")
                    break

                self._dict.addWord(wild, it)
            try:
                infile = open("dictionary.txt", "a", encoding="utf-8") #a: vuol dire append-->aggiungi alla fine ai dati che già hai
                infile.write("\n" + wild + " " + ita)
                infile.close()
            except IOError:
                print("Si è verificato un errore")
# -------------------------------------------------------------------------------------------
    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        return self._dict.translate(query.lower())

# -------------------------------------------------------------------------------------------
    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        return self._dict.translateWordWildCard(query)