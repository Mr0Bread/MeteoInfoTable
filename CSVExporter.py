import csv
from Request import *


class CSVExporter(Request):
    def __init__(self):
        super().__init__()
        self.request = Request()

    def export_to_CSV(self):
        with open('Meteo_Info_Table.csv', mode='w') as csv_file:
            fieldnames = ['Station', 'Time', 'TemperatureOfAir', 'AirsTempChangeInOneHour', 'Humidity', 'DewPoint',
                          'Precipitation', 'Intensity', 'Visibility', 'TrackTemp', 'TracksTempChangesInOneHour',
                          'TracksCondition', 'RouteWarning', 'FreezingPoint', 'TrackTemp2',
                          'TracksTemp2ChangesInOneHour', 'TracksCondition2', 'RouteWarning2', 'FreezingPoint2']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            values_for_csv = []
            rows = self.request.table.find_all('tr', attrs={'height': '30'})
            for row in rows:
                values_for_csv.clear()
                cells = row.find_all('td')

                for cell in cells:
                    values_for_csv.append(cell.text)

                if len(values_for_csv) < 19:
                    i = 2
                    while i < 19:
                        values_for_csv.append(' ')
                        i += 1

                for value in values_for_csv:
                    print(value)

                for i in range(len(values_for_csv)):
                    if 'Ā' in values_for_csv[i]:
                        values_for_csv[i].replace('Ā', 'A')
                    elif 'ī' in values_for_csv[i]:
                        values_for_csv[i].replace('ī', 'i')
                    elif 'ž' in values_for_csv[i]:
                        values_for_csv[i].replace('ž', 'z')
                    elif 'ā' in values_for_csv[i]:
                        values_for_csv[i].replace('ā', 'a')
                    elif 'č' in values_for_csv[i]:
                        values_for_csv[i].replace('č', 'c')
                    elif 'ū' in values_for_csv[i]:
                        values_for_csv[i].replace('ū', 'u')
                    elif 'Ķ' in values_for_csv[i]:
                        values_for_csv[i].replace('Ķ', 'K')
                    elif 'š' in values_for_csv[i]:
                        values_for_csv[i].replace('š', 's')
                    elif 'ļ' in values_for_csv[i]:
                        values_for_csv[i].replace('ļ', 'l')
                    elif 'ē' in values_for_csv[i]:
                        values_for_csv[i].replace('ē', 'e')
                    elif 'ņ' in values_for_csv[i]:
                        values_for_csv[i].replace('ņ', 'n')

                for value in values_for_csv:
                    print(value)

                writer.writerow({'Station': values_for_csv[0],
                                 'Time': values_for_csv[1],
                                 'TemperatureOfAir': values_for_csv[2],
                                 'AirsTempChangeInOneHour': values_for_csv[3],
                                 'Humidity': values_for_csv[4],
                                 'DewPoint': values_for_csv[5],
                                 'Precipitation': values_for_csv[6],
                                 'Intensity': values_for_csv[7],
                                 'Visibility': values_for_csv[8],
                                 'TrackTemp': values_for_csv[9],
                                 'TracksTempChangesInOneHour': values_for_csv[10],
                                 'TracksCondition': values_for_csv[11],
                                 'RouteWarning': values_for_csv[12],
                                 'FreezingPoint': values_for_csv[13],
                                 'TrackTemp2': values_for_csv[14],
                                 'TracksTemp2ChangesInOneHour': values_for_csv[15],
                                 'TracksCondition2': values_for_csv[16],
                                 'RouteWarning2': values_for_csv[17],
                                 'FreezingPoint2': values_for_csv[18]})
