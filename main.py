import translator as tr

t = tr.Translator()

while(True):

    t.printMenu()
    t.loadDictionary("dictionary.txt")

    txtIn = input("Seleziona un'opzione: \n")
    if not txtIn.isdigit():
        print("\nErrore: Inserisci un numero valido.")
        continue

    scelta = int(txtIn)
    if scelta==1:
        query = input("Ok, quale parola devo aggiungere?\n")
        if len(query)==2:
            parolaAliena, parolaTradotta = query
            t.handleAdd(parolaAliena, parolaTradotta)
            print("Aggiunta! \n")
        else:
            print("Errore.\n")

    elif scelta==2:
        query = input("Ok, di quale parola aliena vuoi vedere la traduzione? \n")
        t.handleTranslate(query)

    elif scelta==3:
        query = input("Ok, quale parola devo cercare? \n")
        t.handleWildCard(query)

    elif scelta==4:
        print("Ecco il dizionario: ")
        t.dizionario.printDictionary()
        print() #aggiungo una riga vuota dopo la stampa
        break
        #scelta==5 non serve, chiudi già a 4


    # Add input control here!

    # if int(txtIn) == 1:
    #     print()
    #     txtIn = input()
    #     pass
    # if int(txtIn) == 2:
    #     pass
    # if int(txtIn) == 3:
    #     pass
    # if int(txtIn) == 4:
    #     break