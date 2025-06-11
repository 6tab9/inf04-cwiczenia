import random


class ArrayOperations:
    __array:list[int]
    __arrayLength:int
    def __init__(self,arraySize:int):
        self.__arrayLength = arraySize
        self.__array = [random.randint(1,1000) for _ in range(arraySize)]
    def show(self):
        for i,element in enumerate(self.__array):
            print(f"{i}: {element}")
    def find(self,toBeFound)->int:
        for i,element in enumerate(self.__array):
            if element==toBeFound:
                return i
        return -1
    def oddNumbers(self):
        oddNumberAmount = 0
        print("Liczby nieparzyste: ")
        for element in self.__array:
            if element % 2 != 0:
                oddNumberAmount+=1
                print(element)
        return oddNumberAmount
    def arythmAvg(self)->int:
        sum = 0
        for element in self.__array:
            sum += element
        return int(sum/self.__arrayLength)
def main():
    lista = ArrayOperations(21)
    lista.show()
    szukanyIndex = lista.find(62)
    if szukanyIndex != -1:
        print("Szukany index:",szukanyIndex)
    print(f"Liczba nieparzystych liczb: {lista.oddNumbers()}")
    print(f"Średnia wszystkich elementów: {lista.arythmAvg()}")

if __name__=="__main__":
    main()