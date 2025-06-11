def nwd(firstNumber:int,secondNumber:int):
    a = firstNumber
    b = secondNumber
    while a!=b:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a

# print(nwd(int(input("Podaj pierwszą liczbę: ")),int(input("Podaj drugą liczbę: "))))
print(int("A",16))