class Player(object):
    NumberOfPlayers=0

    @classmethod
    def GetNumberOfPlayers(cls):
        return cls.NumberOfPlayers

    @classmethod
    def PlayersID(cls):
        cls.NumberOfPlayers+=1
        return cls.NumberOfPlayers

    def __init__(self,name,team):
        self.name=name.upper()
        self.team=team.upper()
        self.id=Player.NumberOfPlayers
        self.matchstatus=[]
        self.matchgoalsplus=[]
        self.matchgoalsminus=[]
        Player.PlayersID()

    def getName(self):
        return str(self.name)

    def getTeam(self):
        return self.team

    def getID(self):
        return int(self.id)

    def getMatchStatus(self):
        return self.matchstatus

    def getMatchGoalsPlus(self):
        return sum(self.matchgoalsplus)

    def getMatchGoalsMinus(self):
        return sum(self.matchgoalsminus)

    def getMatchGoalsDiff(self):
        return (self.getMatchGoalsPlus()-self.getMatchGoalsMinus())

    def getMatchNumbers(self):
        return len(self.matchstatus)

    def getMatchNumbersWin(self):
        return self.matchstatus.count("W")

    def getMatchNumbersDraw(self):
        return self.matchstatus.count("D")

    def getMatchNumberLoss(self):
        return self.matchstatus.count("L")

    def getPlayerPoints(self):
        return self.getMatchNumbersWin()*3+self.getMatchNumbersDraw()

    def setName(self,name):
        self.name=name.upper()

    def setTeam(self,team):
        self.team=team.upper()

    def setMatchStatus(self,status):
        self.matchstatus.append(status)

    def setMatchGoalsPlus(self,goals):
        self.matchgoalsplus.append(goals)

    def setMatchGoalsMinus(self,goals):
        self.matchgoalsminus.append(goals)
