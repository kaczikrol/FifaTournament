from Player import Player
from beautifultable import BeautifulTable

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
