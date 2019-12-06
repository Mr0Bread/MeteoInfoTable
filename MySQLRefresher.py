import time
from MySQLExporter import MySQLExporter
from Request import Request
from multiprocessing import Process


class MySQLRefresher(MySQLExporter):
    def __init__(self):
        self.exporter = MySQLExporter()
        self.request = Request()

    def enable_refreshment_loop(self):

    def refresh_table(self):
        time.sleep(60)
        self.command = "TRUNCATE TABLE meteonfotable"
        self.my_cursor.execute(self.command)

        values_for_database = []

        for row in self.request.table.find_all('tr', attrs={'height': '30'}):
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
