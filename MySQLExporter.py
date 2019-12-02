import mysql.connector
from Request import Request


class MySQLExporter(Request):

    def drop_schema(self):
        self.connect_to_MySQL()
        self.command = "DROP DATABASE meteoinfo"
        self.my_cursor.execute(self.command)
        self.database.commit()

    def send_to_mysql(self, rows):
        self.create_MySQL_table_in_database()
        values_for_database = []

        for row in rows:
            values_for_database.clear()
            cells = row.find_all('td')

            for cell in cells:
                values_for_database.append(cell.text)

            if len(values_for_database) < 19:
                i = 2
                while i < 19:
                    values_for_database.append('')
                    i += 1

            self.command = "INSERT INTO meteoinfotable (Station, Time, TemperatureOfAir, AirsTempChangeInOneHour,  Humidity, DewPoint, Precipitation, Intensity, Visibility, TrackTemp, TracksTempChangesInOneHour, TracksCondition, RouteWarning, FreezingPoint, TrackTemp2, TracksTemp2ChangesInOneHour, TracksCondition2, RouteWarning2, FreezingPoint2) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.my_cursor.execute(self.command, values_for_database)
            self.database.commit()

    def create_MySQL_table_in_database(self):
        self.connect_to_database()
        self.command = "CREATE TABLE meteoinfotable (Station VARCHAR(30), Time VARCHAR(45), TemperatureOfAir VARCHAR(8), AirsTempChangeInOneHour VARCHAR(10),  Humidity VARCHAR(3), DewPoint VARCHAR(6), Precipitation VARCHAR(30), Intensity VARCHAR(6), Visibility VARCHAR(4), TrackTemp VARCHAR(8), TracksTempChangesInOneHour VARCHAR(8), TracksCondition VARCHAR(20), RouteWarning VARCHAR(20), FreezingPoint VARCHAR(10), TrackTemp2 VARCHAR(8), TracksTemp2ChangesInOneHour VARCHAR(8), TracksCondition2 VARCHAR(20), RouteWarning2 VARCHAR(20), FreezingPoint2 VARCHAR(10))"
        self.my_cursor.execute(self.command)
        self.database.commit()

    def connect_to_database(self):
        self.create_database()
        self.database = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='mr0bread',
            database='meteoinfo'
        )
        self.my_cursor = self.database.cursor()

    def create_database(self):
        self.connect_to_MySQL()
        self.command = "CREATE DATABASE meteoinfo"
        self.my_cursor.execute(self.command)

    def connect_to_MySQL(self):
        self.database = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='mr0bread'
        )
        self.my_cursor = self.database.cursor()
