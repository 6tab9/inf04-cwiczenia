import random


def main():
    diceAmount = int(input("Podaj ilość kostek (3-10): "))
    if(diceAmount>=3 and diceAmount<=10):
        diceArray = []
        points = 0
        for i in range(diceAmount):
            randomDieValue = random.randint(1,6)
            if(diceArray.__contains__(randomDieValue)):
                points+=randomDieValue
            diceArray.append(randomDieValue)
            print(f"Kostka {i+1}: {randomDieValue}")
        print(f"Zdobyto punktów: {points}")
        if(input("Kontynuuj: (t/n): ")=="t"):
            main()

if __name__ == "__main__":
    main()