import pandas
from IntroductionDb import SqlDbBase


def showTable(cursor):
    result = cursor.fetchall()
    for item in result:
        print(item)
    print()


class Select(SqlDbBase.DbBase):
    selectQueryBooks = 'SELECT * FROM [LibraryDb].[dbo].[BOOKs]'

    def __del__(self):
        self.cursor.cancel()

    def getDateFrameBooks(self):
        table_result = pandas.read_sql(self.selectQueryBooks, self.conn)
        df = pandas.DataFrame(table_result)
        return df

    def getBooks(self, condition=""):
        query = self.selectQueryBooks
        if len(condition) != 0:
            query += " WHERE " + condition
        self.cursor.execute(query)
        showTable(self.cursor)

    def getBookById(self, book_id):
        query = self.selectQueryBooks + " WHERE [BOOKs].ID = " + str(book_id)
        self.cursor.execute(query)
        showTable(self.cursor)
