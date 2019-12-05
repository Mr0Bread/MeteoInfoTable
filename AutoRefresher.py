from MySQLExporter import MySQLExporter
from Request import Request
import threading
import time
import mysql.connector
import asyncio


class AutoRefresher(MySQLExporter, Request):
    def __init__(self):
        super().__init__()
        self.thread = threading.Thread(target=self.auto_refresh)
        self.exporter = MySQLExporter()
        self.thread_is_running = False
        self.database = mysql.connector.connect(host='localhost',
                                                user='root',
                                                passwd='mr0bread'
                                                )
        self.my_cursor = self.database.cursor()

    def enable_auto_refresh(self):
        self.database.connect(host='localhost',
                              user='root',
                              passwd='mr0bread',
                              database='meteoinfo')
        self.my_cursor = self.database.cursor()
        self.thread_is_running = True
        self.thread.start()
        print("thread started")

    def disable_auto_refresh(self):
        self.thread_is_running = False
        self.thread.join()
        print("thread ended")

    def auto_refresh(self):
        values_to_be_exported = []
        while self.thread_is_running:
            try:
                time.sleep(5)
                self.get_info_for_table()
                rows = self.table.find_all('tr', attrs={'height': '30'})
                counter = 1
                for row in rows:
                    values_to_be_exported.clear()
                    cells = row.find_all('td')

                    for cell in cells:
                        values_to_be_exported.append(cell.text)

                    self.command = "SELECT * FROM meteoinfotable WHERE rowID = %s"
                    rowID = counter
                    self.my_cursor.execute(self.command, (rowID,))
                    record = self.my_cursor.fetchall()
                    list_of_imported_values = record[0]
                    print(list_of_imported_values)

                    # if 2 != values_to_be_exported[x]:
                    #     self.command = "UPDATE meteoinfotable SET Station = %s, Time = %s, TemperatureOfAir = %s, AirsTempChangeInOneHour = %s,  Humidity = %s, DewPoint = %s, Precipitation = %s, Intensity = %s, Visibility = %s, TrackTemp = %s, TracksTempChangesInOneHour = %s, TracksCondition = %s, RouteWarning = %s, FreezingPoint = %s, TrackTemp2 = %s, TracksTemp2ChangesInOneHour = %s, TracksCondition2 = %s, RouteWarning2 = %s, FreezingPoint2 = %s WHERE rowID = %s"
                    #     values = (values_to_be_exported[0], values_to_be_exported[1], values_to_be_exported[2],
                    #               values_to_be_exported[3], values_to_be_exported[4], values_to_be_exported[5],
                    #               values_to_be_exported[6], values_to_be_exported[7], values_to_be_exported[8],
                    #               values_to_be_exported[9], values_to_be_exported[10], values_to_be_exported[11],
                    #               values_to_be_exported[12], values_to_be_exported[13], values_to_be_exported[14],
                    #               values_to_be_exported[15], values_to_be_exported[16], values_to_be_exported[17],
                    #               values_to_be_exported[18], counter + 1)
                    #     self.my_cursor.execute(self.command, values)
                    #     self.database.commit()
                    #     print("checked row")
                    counter += 1
            except mysql.connector.errors.ProgrammingError:
                print("Database was deleted before ending of refresh cycle")
