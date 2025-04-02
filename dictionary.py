class Dictionary:

    def __init__(self):
        self._dizionario = {}

    def __str__(self):
         str=""
         for (key, value) in self._dizionario.items():
             str += f"{key} {value};\n"
         return str

    def clear(self):
        self._dizionario.clear()  #svotare il dizionario

#---------------------------------------------------------------------------------------------------------------
    def addWord(self, wild, ita):
        if wild.lower() in self._dizionario and ita.lower()==self._dizionario[wild.lower()]:
            pass
        else:
            if wild.lower() not in self._dizionario:
                self._dizionario[ wild.lower() ] = []
            self._dizionario[wild.lower()].append(ita.lower())

# ---------------------------------------------------------------------------------------------------------------
    def translate(self, wild):
        #dal file translator.py capisco che ha wild come parametro
        return self._dizionario.get(wild.lower(), "Parola non trovata")
    """risposta=[]
       for (alien,ita) in self._dizionario.items():
            if parolaAliena.lower()==alien:
                risposta.append(ita)
            if risposta==[]
                return "Parola non trovata"
            return risposta """

# ---------------------------------------------------------------------------------------------------------------
    def translateWordWildCard(self, wild):
        #dal file translator.py capisco che è il caso con "?"
        risposta=[]
        for alien in self._dizionario:
            if len(wild)==len(alien) and (wild.split("?")[0].lower() in alien.lower() and wild.split("?")[1].lower() in alien.lower()) :
                risposta.append(alien)                      #stampa prima la parola aliena senza "?"
                risposta.append(self.translate(alien))      #stampa la traduzione attraverso il metodo precedente
                return risposta

        if risposta==[]:
            risposta.append("Parola non trovata")
        return risposta

