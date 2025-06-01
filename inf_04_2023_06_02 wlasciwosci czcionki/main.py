import random


def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    print(array)

def main():
    array = [random.randint(0,100) for _ in range(0,100)]
    bubblesort(array)

if __name__=="__main__":
    main()