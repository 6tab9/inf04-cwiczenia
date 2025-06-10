class Osoba:
    __id:int
    __imie:str
    liczbaInstancji = 0

    def __init__(self, id=0,imie=""):
        Osoba.liczbaInstancji+=1
        self.__id=id
        self.__imie=imie
    def greet(self,personToGreet):
        if self.__imie!="":
            print(f"Cześć {personToGreet}, mam na imię {self.__imie}")
        else:
            print("Brak danych")
    @classmethod
    def kopiuj(cls, innaOsoba):
        return cls(innaOsoba.__id,innaOsoba.__imie)
def main():
    Piotrek = Osoba(0,"Piotrek")
    Piotrek.greet("Szymon")
    Piotrek2 = Osoba.kopiuj(Piotrek)
    Piotrek2.greet("Szymon")

if __name__ == "__main__":
    main()