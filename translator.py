class Translator:

    def __init__(self):
        self.dizionario = {}

#-------------------------------------------------------------------------------------------
    def printMenu(self):
        print("-------------------------------------------")
        print("    Translator Alien-Italian")
        print("-------------------------------------------")
        print(" 1. Aggiungi nuova parola")
        print(" 2. Cerca una traduzione")
        print(" 3. Cerca con wildcard")
        print(" 4. Stampa tutto il dizionario")
        print(" 5. Exit")
        print("-------------------------------------------")

# -------------------------------------------------------------------------------------------
    def loadDictionary(self, filename):

        dict = {}
        try:
            with open(filename, "r", encoding="UTF-8") as file:
                for line in file:
                    campi = line.strip().split(" ", 1) #1--> dividi solo una volta
                    if len(campi) == 2:
                        dict.addWord(campi[0], campi[1])
        except FileNotFoundError:
            print("Il dizionario non è stato trovato!")

# -------------------------------------------------------------------------------------------
    def handleAdd(self, entry):
         """
         tupla --> 2 elementi insieme, già loro mi dicono che entry è una tupla di a e b
         :param entry: tupla
         :return:
         """
         parolaAliena, parolaTradotta = entry
         if parolaAliena.isAlpha & parolaTradotta.isAlpha:
             self.dizionario.addWord(parolaAliena, parolaTradotta)
         else:
             print("\nErrore: sono ammessi solo caratteri alfabetici.")

# -------------------------------------------------------------------------------------------
    def handleTranslate(self, parolaAliena):
        #query era = a parolaAliena
        traduzione = self.dizionario.translate(parolaAliena)
        if traduzione is None:
            print("La traduzione non è ancora stata trovata! ")
            return None
        print(f"{traduzione}+.n")
        print(self.dizionario[parolaAliena]) #boo

    # -------------------------------------------------------------------------------------------
    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        aliena = self.dizionario.translateWordWildCard(query)
        if aliena is None:
            print("La parola aliena non è ancora stata trovata! ")
            return None
        print(f"{aliena}+.n")
        print(self.dizionario.get(aliena))  # boo