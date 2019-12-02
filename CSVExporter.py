import csv
from Request import Request


class CSVExporter(Request):
    def __init__(self):
        super().__init__()
        self.request = Request()

    def export_to_CSV(self):
        with open('Meteo_Info_Table.csv', mode='w', encoding='utf-8') as csv_file:
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
