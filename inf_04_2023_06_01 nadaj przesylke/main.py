def main():
    numbersArray = [i for i in range(2,100)]
    tempArray = []
    for i in numbersArray:
        for j in numbersArray:
            if j%i!=0:
                tempArray.append(j)

    print(tempArray)

if __name__=="__main__":
    main()