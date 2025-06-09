class Notatka():
    __noteCount:int = 0
    __id:int
    _title:str
    _content:str
    def __init__(self,title,content):
        Notatka.__noteCount+=1
        self.__id=Notatka.__noteCount
        self._title=title
        self._content=content
    def read(self):
        print(f"Tytuł notatki: {self._title}\nTreść notatki: {self._content}")
    def diagnose(self):
        print(f"{Notatka.__noteCount}; {self.__id}; {self._title}; {self._content}")

def main():
    movieNote = Notatka("Star Wars","SciFi")
    consolesNote = Notatka("Sony","PSX, PS2, PSP, PS3, PS4, PSVita, PS5")
    movieNote.read()
    consolesNote.diagnose()
if __name__ == "__main__":
    main()
