from Player import Player
from Match import Match
import HelpFunctions as hp

def main():
    '''Fifa Tournament Creator'''
    print("Witaj w kreatorze turniejów w FIFA. Obsłuż program za pomocą klawiatury")
    Players=[]
    ExitProgram=False
    while (ExitProgram!=True):
        Options=None
        print("Numer                Treść")
        print("0.                   Zakończ")
        print("1.                   Dodaj zawodnika")
        print("2.                   Pokaż liste zawodników")
        print("3.                   Edytuj zawodnika")
        print("4.                   Usuń zawodnika")
        print("5.                   Sprawdź tabele")
        print("6.                   Rozpocznij turniej")
        print("7.                   Eksportuj do pliku .txt")
        print("8.                   Pokaż wizualizacje")
        while (Options not in [0,1,2,3,4,5,6,7,8]):
            print("Wprowadź poprawną cyfrę.")
            try:
                Options = eval(input("Wybierz jedną z powyższych opcji i zatwierdż klawiszem Enter." + '\n'))
            except (NameError,SyntaxError):
                pass

        if (Options==0):
            if hp.AreYouSure():
                print("Dziękujemy za skorzystanie z programu!")
                ExitProgram=True
            else:
                continue

        elif(Options==1):
            if hp.AreYouSure():
                hp.AddPlayerToList(Players)
            else:
                continue

        elif(Options==2):
            hp.PlayerList(Players)

        elif(Options==3):
            pass

        elif(Options==4):
            if hp.AreYouSure():
                hp.DeletePlayerFromList(Players)
            else:
                continue

        elif(Options==5):
            hp.ShowTable(Players)

        elif(Options==6):
            if hp.AreYouSure():
                matchs=Match(Players)
                print("Liczba meczy do rozegrania w turnieju: ",matchs.GetMatchQty())
                matchs_no=0
                for match in matchs.GetMatchPairsByName():
                    matchs_no+=1
                    print("Match ",matchs_no,match)
                matchs.SetMatchResults()
            else:
                continue

main()