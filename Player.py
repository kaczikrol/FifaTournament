class Player(object):
    NumberOfPlayers=0

    @classmethod
    def GetNumberOfPlayers(cls):
        return cls.NumberOfPlayers


    def __init__(self,name,team):
        self.name=name.upper()
        self.team=team.upper()
        self.id=Player.NumberOfPlayers
        Player.PlayersID()

    @classmethod
    def PlayersID(cls):
        cls.NumberOfPlayers+=1
        return cls.NumberOfPlayers


    def getName(self):
        return self.name

    def getTeam(self):
        return self.team

    def getID(self):
        return int(self.id)

    def setName(self,name):
        self.name=name.upper()

    def setTeam(self,team):
        self.team=team.upper()
