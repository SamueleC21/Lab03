import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.italian = d.Dictionary("italian")
        self.english = d.Dictionary("english")
        self.spanish = d.Dictionary("spanish")

        self.italian.loadDictionary("resources/Italian.txt")
        self.english.loadDictionary("resources/English.txt")
        self.spanish.loadDictionary("resources/Spanish.txt")


    def printDic(self, language):
        if language == "italian":
            self.italian.printAll()
        elif language == "english":
            self.english.printAll()
        elif language == "spanish":
            self.spanish.printAll()
        else:
            print("Lingua non disponibile")


    def searchWord(self, words:list, language):
        parole_sbagliate = []
        if language == "italian":
            for word in words:
                self.rw = rw.RichWord(word, True)
                if word not in self.italian.dict:
                    parole_sbagliate.append(word)
                    self.rw.corretta = False
            return parole_sbagliate

        elif language == "english":
            for word in words:
                self.rw = rw.RichWord(word, True)
                if word not in self.english.dict:
                    parole_sbagliate.append(word)
                    self.rw.corretta = False
            return parole_sbagliate

        elif language == "spanish":
            for word in words:
                self.rw = rw.RichWord(word, True)
                if word not in self.spanish.dict:
                    parole_sbagliate.append(word)
                    self.rw.corretta = False
            return parole_sbagliate





