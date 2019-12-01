from Application import *
import pymysql
import mysql.connector


class Main(Application):
    def __init__(self, master):
        super().__init__(master)
        self.connect_to_database()

    def connect_to_database(self):
        database = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='mr0bread',
            database='meteoinfotable'
        )


