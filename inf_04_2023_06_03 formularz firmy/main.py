class Film():
    _title:str
    _borrowAmount:int
    def __init__(self):
        self._title=""
        self._borrowAmount=0
    def titleSetter(self,newTitle):
        self._title=newTitle
    def titleGetter(self)->str:
        return self._title
    def borrowAmountGetter(self)->int:
        return self._borrowAmount
    def borrowAmountIncrement(self):
        self._borrowAmount+=1
    def __str__(self):
        return f"title: {self._title}\nborrow amount: {self._borrowAmount}"

def main():
    filmObject = Film()
    filmObject.titleSetter("Neon genesis evangelion")
    print(filmObject)
    print(f"\nTytuł: {filmObject.titleGetter()}, Liczba wypożyczeń przed: {filmObject.borrowAmountGetter()}")
    filmObject.borrowAmountIncrement()
    print(f"\nLiczba wypożyczeń po: {filmObject.borrowAmountGetter()}")



if __name__=="__main__":
    main()