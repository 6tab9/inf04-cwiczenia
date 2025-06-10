import math

def eratostenes(tab):
    n = 100
    A = [True for _ in range(2,n)]
    for i in range(2,int(math.pow(n,1/2))):
        if A[i-2]==True:
            for j in range(2,n):
                if j*i < n:
                    A[j*i-2] = False
    for i,bool in enumerate(A):
        if bool:
            tab.append(i+2)
    print(A)
def main():
    tabToFill = []
    eratostenes(tabToFill)
    print(tabToFill)

if __name__=="__main__":
    main()