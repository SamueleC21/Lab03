import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.d = d.Dictionary()


    def printDic(self, language):
        path = language + ".txt"
        self.d.loadDictionary(path)

    def searchWord(self, words:list, language):
        for word in words:
            self.rw = rw.RichWord(word)



