import sys
from IntroductionDb.Select import Select

qwe = "Hi"
instaSelect = Select()

instaSelect.getBooks()
query2 = instaSelect.getBookById(761)
instaSelect.getBooks("COUNT = 2")

dataFrame = instaSelect.getDateFrameBooks()
print(dataFrame)

qwe = ''
