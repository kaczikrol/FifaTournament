from Player import Player
import HelpFunctions as hp

class Match(object):

    def __init__(self,list):
        self.Players=list
        self.MatchQty=hp.MatchQtyFunction(list)
        self.MatchTable=hp.MatchLottery(list)

    def GetMatchQty(self):
        return self.MatchQty

    def GetMatchPairs(self):
        return self.MatchTable

    def GetMatchPairsByName(self):
        newMatchTable=[]
        for pairs in self.MatchTable:
            newpairs = (pairs[0].getTeam(),pairs[1].getTeam())
            newMatchTable.append(newpairs)
        return newMatchTable

    def SetMatchResults(self):
        MatchResults=[]
        print(Match.GetMatchPairsByName(self))
        for team in self.MatchTable:
                pair=(team[0].getTeam(),team[1].getTeam())
                print(pair)
                goalsteam0=eval(input("Gole "+team[0].getTeam()+" : "))
                goalsteam1=eval(input("Gole "+team[1].getTeam()+" : "))
                team[0].setMatchGoalsPlus(goalsteam0)
                team[1].setMatchGoalsMinus(goalsteam0)
                team[0].setMatchGoalsMinus(goalsteam1)
                team[1].setMatchGoalsPlus(goalsteam1)
                if goalsteam0>goalsteam1:
                    team[0].setMatchStatus("Z")
                    team[1].setMatchStatus("P")
                elif goalsteam0==goalsteam1:
                    team[0].setMatchStatus("R")
                    team[1].setMatchStatus("R")
                elif goalsteam0<goalsteam1:
                    team[0].setMatchStatus("P")
                    team[1].setMatchStatus("Z")


