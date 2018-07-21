from gender.Female import Female
from gender.Male import Male
from article.Article  import Article
class Noun(object):
    """
    This class represents a noun.
    """
    def __init__(self,noun:str):
        self.__noun = noun
        self.__gender = None
        self.__setGenderRoutine()
        self.__article = Article(self.__gender)
    def __setGenderRoutine(self):
        last_letter = self.__noun[-1:]
        if last_letter == 'a':
            self.__gender = Female()
            return
        if last_letter == 'o':
            self.__gender = Male()
            return
        raise Exception('The gender could not be defined!')
    def getNoun(self)->str:
        return self.__noun
    def getGender(self):
        return self.__gender
    def getArticle(self):
        return self.__article
    def getPlural(self):
        return '{0}s'.format(self.__noun)