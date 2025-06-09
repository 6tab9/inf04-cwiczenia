class PESELOperation:
    @classmethod
    def checkSex(cls,PESEL):
        if int(PESEL[9]) % 2 == 0:
            return 'K'
        else:
            return 'M'
    @classmethod
    def checkPesel(cls,PESEL):
        wagi = [1,3,7,9,1,3,7,9,1,3]
        S = 0
        M = 0
        R = 0
        for i,cyfra in enumerate(PESEL[0:-1]):
            S+=int(cyfra)*wagi[i]
        M = S%10
        if M:
            R = 10-M
        return R == int(PESEL[10])

def Main():
    PESEL = input("Podaj swój numer PESEL: ")
    if PESELOperation.checkSex(PESEL) == 'K':
        print("Płeć: Kobieta")
    else:
        print("Płeć: Mężczyzna")
    if PESELOperation.checkPesel(PESEL):
        print("Poprawny numer PESEL")
    else:
        print("Niepoprawny numer PESEL")

if __name__=="__main__":
    Main()