from article.Article import Article
from gender.Gender import Gender
from gender.Male import Male
from gender.Female import Female
"""
    Overview over the articles:
"""
print ('artìculo:')
article = Article()
def articleSpecific(article:Article,kind:str):
    print('artículo {0}: {1}'.format(kind,article.getSingular()))
    print('artículo {0}: {1}'.format(kind,article.getPlural()))
def articleOverview(article:Article,gender:Gender):
    article.setGender(gender)
    print ('{}:'.format(gender.getName()))
    articleSpecific(article.getDefinite(),'específico')
    articleSpecific(article.getUndefinite(),'indefinido')
articleOverview(article,Female())
articleOverview(article,Male())
