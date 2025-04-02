import translator as tr
t = tr.Translator()

while(True):

    t.printMenu()
    t.loadDictionary("dictionary.txt")

    txtIn = input()
    # Add input control here!

    if int(txtIn)==1:
        query = input("Ok, quale parola devo aggiungere?\n")
        #print(query.split(" "))
        t.handleAdd( query.split(" ", 1))
        print("Aggiunta!\n")

    if int(txtIn) == 2:
        query = input("Ok, di quale parola aliena vuoi vedere la traduzione? \n")
        print(t.handleTranslate(query))
    if int(txtIn) == 3:
        query = input("Ok, quale parola devo cercare? \n")
        wild = t.handleWildCard(query)
        print(wild[0])
        if len(wild)>1:
            print(wild[1])
    if int(txtIn) == 4:
        print(t._dict)