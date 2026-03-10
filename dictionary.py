class Dictionary:
    def __init__(self):
        self._dict = set()

    def loadDictionary(self, path, language):
        with open(path, "r") as file:
            for riga in file:
                self._dict.add(riga.rstrip())

        #return self.dict

    def printAll(self):
        pass


    @property
    def dict(self):
        return self._dict