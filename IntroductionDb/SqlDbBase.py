import pyodbc


class DbBase:
    def __init__(self):
        con_string = "Driver={SQL Server};Server=TimDev\SQLEXPRESS;Database=LibraryDb;Trusted_Connection=yes;"
        print("Connecting to" + con_string)
        self.conn = pyodbc.connect(con_string)
        self.cursor = self.conn.cursor()
