import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multiD = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        #self.multiD.printDic(language)
        tempo1 = time.time()
        txtIn = replaceChars(txtIn)
        words = txtIn.split()
        parole_sbagliate = self.multiD.searchWord(words, language)
        for parola in parole_sbagliate:
            print(parola)
        tempo2 = time.time()
        print(f"il tempo necessario è {tempo2 - tempo1}")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text