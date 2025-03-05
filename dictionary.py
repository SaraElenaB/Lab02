class Dictionary:

    def __init__(self):
        self.dizionario = {}

    def addWord(self, parolaAliena, parolaTradotta):
        self.dizionario[parolaAliena.lower()] = parolaTradotta

    def translate(self, parolaAliena):
        if parolaAliena.lower() in self.dizionario.keys():
            return self.dizionario[parolaAliena.lower()]

    def translateWordWildCard(self, parolaAliena):
        for parola in self.dizionario.keys():
            if parola==parolaAliena.lower():
                return self.dizionario[parolaAliena]
        print("La parola aliena non esiste o non è ancora stata tradotta! Riprovare")
        return None
        # attenzione, non va bene scrivere if: else: perchè vuol dire che se alla prima iterazione l'if
        # non è verificato stampa subito l'else. perciò mettilo fuori dal ciclo di for

    def printDictionary(self):
        if len(self.dizionario) == 0:
            print("Errore di stampa. Dizionario Vuoto!")
        else:
            for parolaAliena in self.dizionario.keys():
                parolaTradotta = self.dizionario[parolaAliena]
                print(f"{parolaAliena} - {parolaTradotta}")
            #for parolaAliena, parolaTradotta in self.dizionario.items(): --> itera su tutti gli elementi, sia chiave che valore