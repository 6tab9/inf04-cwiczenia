class ArrayOperation():
    __tableToSort = []
    def __init__(self):
        for i in range(10):
            self.__tableToSort.append(int(input(f"Podaj {i+1} liczbę do wpisania w tablicę: ")))
    def sortowaniePrzezWybieranie(self):
        for i in range(int(len(self.__tableToSort))):
            biggest, biggestIndex = self.__maxWartość(i)
            self.__tableToSort[i],self.__tableToSort[biggestIndex] = self.__tableToSort[biggestIndex],self.__tableToSort[i]
        return self.__tableToSort
    def __maxWartość(self,i):
        max = 0
        maxIndex = 0
        for j in range(i,len(self.__tableToSort)):
            if self.__tableToSort[j] > max:
                max = self.__tableToSort[j]
                maxIndex = j
        return max,maxIndex

def main():
    operacjeNaListach = ArrayOperation()
    print(operacjeNaListach.sortowaniePrzezWybieranie())

if __name__=="__main__":
    main()