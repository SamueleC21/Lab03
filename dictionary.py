
class Dictionary:
    def __init__(self, language):
        self._dict = set()
        self.lingua = language

    def loadDictionary(self, path):
        with open(path, "r") as file:
            for riga in file:
                self._dict.add(riga.rstrip())

        #return self.dict

    def printAll(self):
        for parola in self._dict:
            print(parola)


    @property
    def dict(self):
        return self._dict