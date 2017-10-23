from Player import Player
import HelpFunctions as hp

class Match(object):

    def __init__(self,list):
        self.Players=list
        self.MatchQty=hp.MatchQtyFunction(list)
        self.MatchTable=hp.MatchLottery(list)

    def GetMatchQty(self):
        return self.MatchQty

    def GetMatchPairsByName(self):
        newMatchTable=[]
        for pairs in self.MatchTable:
            newpairs = (pairs[0].getTeam(),pairs[1].getTeam())
            newMatchTable.append(newpairs)
        return newMatchTable

    def SetMatchResults(self):
        MatchResults=[]
        for team in self.MatchTable:
                pair=(team[0].getTeam(),team[1].getTeam())
                print("Mecz pomiędzy:",pair)
                goalsteam0=eval(input("Gole dla "+team[0].getTeam()+" : "))
                goalsteam1=eval(input("Gole dla "+team[1].getTeam()+" : "))
                team[0].setMatchGoalsPlus(goalsteam0)
                team[1].setMatchGoalsMinus(goalsteam0)
                team[0].setMatchGoalsMinus(goalsteam1)
                team[1].setMatchGoalsPlus(goalsteam1)
                if goalsteam0>goalsteam1:
                    team[0].setMatchStatus("W")
                    team[1].setMatchStatus("L")
                elif goalsteam0==goalsteam1:
                    team[0].setMatchStatus("D")
                    team[1].setMatchStatus("D")
                elif goalsteam0<goalsteam1:
                    team[0].setMatchStatus("L")
                    team[1].setMatchStatus("W")
                hp.ShowTable(self.Players)

