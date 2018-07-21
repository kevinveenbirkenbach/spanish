from .Definite import Definite
from .Undefinite import Undefinite

class Article(object):
    """
    This class represents the ruleset of an article
    """
    def __init__(self):
        self.definite = None
        self.undefinite = None
        self.__gender = None
    def __setRuleset(self):
        self.definite = Definite(self)
        self.undefinite = Undefinite(self)
    def setGender(self,gender):
        self.__gender = gender
        self.__setRuleset()
    def getGender(self):
        return self.__gender
    def getDefinite(self)->str:
        return self.definite
    def getUndefinite(self)->str:
        return self.undefinite
