import dictionary
import spellchecker



sc = spellchecker.SpellChecker()
#d = dictionary.Dictionary()

while(True):
    sc.printMenu()

    txtIn = input("Inserisci un numero da 1 a 4: ")
    # Add input control here!
    while (txtIn not in ("1", "2", "3", "4")):
        txtIn = input("Inserisci un numero da 1 a 4: ")

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        testo = input()
        #d.loadDictionary("italian.txt")
        sc.handleSentence(testo,"italian")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        testo = input()
        sc.handleSentence(txtIn,"english")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        testo = input()
        sc.handleSentence(txtIn,"spanish")
        continue

    if int(txtIn) == 4:
        break


