from Player import Player
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
            name=input("Wprowadź imie: \n")
            team=input("Wprowadź zespół: \n")
            Players.append(Player(name,team))

        elif(Options==2):
            hp.PlayerList(Players)

        elif(Options==3):
            hp.PlayerIDList(Players)
            try:
                index=eval(input("Podaj ID "))
                confirm=input("Jesteś pewien T/N?")
                if confirm=="T":
                    del Players[index]
                else: break
            except (IndexError,NameError):
                pass
main()