from Player import Player
from beautifultable import BeautifulTable
import random

def PlayerList(list):
    table=BeautifulTable()
    table.column_headers=["Name","Team"]
    for user in list:
        table.append_row([user.getName(),user.getTeam()])
    print(table)

def PlayerIDList(list):
    table=BeautifulTable()
    table.column_headers=["ID","Name","Team"]
    for user in list:
        table.append_row([user.getID(),user.getName(),user.getTeam()])
    print(table)

def AddPlayerToList(list):
    name = input("Wprowadź imie: \n")
    team = input("Wprowadź zespół: \n")
    list.append(Player(name, team))

def DeletePlayerFromList(list):
    PlayerIDList(list)
    try:
        index = eval(input("Podaj ID "))
        iterator = 0
        confirm = input("Jesteś pewien T/N?").upper()
        if confirm == "T":
            for users in list:
                if users.getID() == index:
                    del list[iterator]
                iterator += 1
    except(NameError, SyntaxError, IndexError):
        pass

def AreYouSure():
    choice=input("Jesteś pewien Y/N? ")
    if (choice.upper()=="Y"):
        return True
    else:
        return False


def ShowTable(list):
    table=BeautifulTable()
    table._max_table_width=500
    table.column_headers=['Name','Team','Match','Wins','Draw','Losses','Goals +','Goals -','Goals +/-','Points']
    for player in list:
        table.append_row([player.getName(),player.getTeam(),player.getMatchNumbers(),player.getMatchNumbersWin(),
                          player.getMatchNumbersDraw(),player.getMatchNumberLoss(),player.getMatchGoalsPlus(),
                          player.getMatchGoalsMinus(),player.getMatchGoalsDiff(),player.getPlayerPoints()])
    table.sort('Goals +/-')
    table.sort('Points')
    table.reverse()
    print(table)

def MatchQtyFunction(list):
    results=0
    for i in range(1,len(list)):
        results=results+i
    return results

def MatchLottery(list):
    matchTable=[]
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            matchTable.append((list[i],list[j]))
    for i in range(len(matchTable)*18):
        matchTable=random.sample(matchTable,len(matchTable))
    return matchTable


