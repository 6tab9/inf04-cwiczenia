import random

class ArrayOperation:
    tab = []
    def fillTab(self):
        for _ in range(50):
            self.tab.append(random.randint(1,100))
    def findInTab(self,x):
        totalIndex = len(self.tab)-1
        self.tab.append(x)
        for i in range(len(self.tab)):
            if x == self.tab[i] and i != totalIndex+1:
                print(self.tab, f"Szukany element ma indeks: {i}")
                break
            elif i == totalIndex+1:
                print("Brak szukanego elementu")

def main():
    arrayOperator = ArrayOperation()
    arrayOperator.fillTab()
    arrayOperator.findInTab(int(input("Podaj liczbę do szukania ")))

if __name__ == "__main__":
    main()