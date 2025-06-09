class utwor():
    artist = ""
    album = ""
    songsNumber = 0
    year = 0
    downloadNumber = 0
    def __str__(self):
        return f"{self.artist}\n{self.album}\n{self.songsNumber}\n{self.year}\n{self.downloadNumber}"

def main():
    utworArray = read()
    printUtwory(utworArray)



def read():
    utworArray = []
    file = open("pliki2/Data.txt", encoding="utf-8").read()
    utworToAdd = utwor()
    for i,line in enumerate(file.split("\n")):
        moduloIndex = i%6
        match moduloIndex:
            case 0:
                utworToAdd.artist=line
            case 1:
                utworToAdd.album=line
            case 2:
                utworToAdd.songsNumber=line
            case 3:
                utworToAdd.year=line
            case 4:
                utworToAdd.downloadNumber=line
            case 5:
                utworArray.append(utworToAdd)
                utworToAdd = utwor()
    return utworArray
def printUtwory(utworArray):
    for utwor in utworArray:
        print(utwor,"\n")

if __name__=="__main__":
    main()

