class StringOperator():
    def liczSamogloski(tekst:str)->int:
        samogloski = "aąeęiouóy"
        samogloskiLicznik = 0
        for litera in tekst:
            if samogloski.__contains__((litera).lower()):
                samogloskiLicznik+=1
        return samogloskiLicznik
    def obetnijPowtorki(tekst:str)->str:
        literaPo = ""
        tekstFinale = "" + tekst[0]
        for i,litera in enumerate(tekst[0:-1]):
            literaPo = tekst[i+1]
            if litera != literaPo:
                tekstFinale+=literaPo
        return tekstFinale

def main():
    print(StringOperator.liczSamogloski(input("Podaj tekst, aby policzyć samogłoski: ")))
    print(StringOperator.obetnijPowtorki(input("Podaj tekst, aby obciąć powtórki znaków: ")))

if __name__=="__main__":
    main()