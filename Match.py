from Player import Player
import HelpFunctions as hp


class Match(object):

    def __init__(self,list):
        self.MatchQty=hp.MatchQtyFunction(list)

    def GetMatchQty(self):
        return self.MatchQty

