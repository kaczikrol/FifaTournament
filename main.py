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
        print("3.                   Usuń zawodnika")
        print("4.                   Sprawdź tabele")
        print("5.                   Sprawdź terminarz")
        print("6.                   Eksportuj do pliku .txt")
        print("7.                   Pokaż wizualizacje")
        while (Options not in [0,1,2,3,4,5,6,7]):
            print("Wprowadź poprawną cyfrę.")
            try:
                Options = eval(input("Wybierz jedną z powyższych opcji i zatwierdż klawiszem Enter." + '\n'))
            except (NameError,SyntaxError):
                pass

        if (Options==0):
            print("Dziękujemy za skorzystanie z programu!")
            ExitProgram=True

        elif(Options==1):
            hp.AddPlayerToList(Players)

        elif(Options==2):
            hp.PlayerList(Players)

        elif(Options==3):
            hp.DeletePlayerFromList(Players)

        elif(Options==4):
            hp.ShowTable(Players)

        elif(Options==5):
            matchs=Match(Players)
            print("Liczba meczy: ",matchs.GetMatchQty())
            matchs.GetMatchPairs()
            matchs.GetMatchPairsByName()
            matchs.SetMatchResults()

main()