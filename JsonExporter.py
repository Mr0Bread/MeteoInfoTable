import json
from Request import Request


class JsonExporter(Request):
    def __init__(self):
        super().__init__()
        self.request = Request()

    def export_to_json(self):
        with open('Meteo_Info_Table_JSON.json', mode='w', encoding='utf-8') as json_file:
            j = 0
            value_for_exporting = []
            data_for_exporting = {}
            rows = self.request.table.find_all('tr', attrs={'height': '30'})
            for row in rows:
                value_for_exporting.clear()
                cells = row.find_all('td')

                for cell in cells:
                    value_for_exporting.append(cell.text)

                if len(value_for_exporting) < 19:
                    i = 2
                    while i < 19:
                        value_for_exporting.append(' ')
                        i += 1

                child_of_data_for_exporting = {
                    'Stations': {
                        value_for_exporting[0]: {
                            'Time': value_for_exporting[1],
                            'TemperatureOfAir': value_for_exporting[2],
                            'AirsTempChangeInOneHour': value_for_exporting[3],
                            'Humidity': value_for_exporting[4],
                            'DewPoint': value_for_exporting[5],
                            'Precipitation': value_for_exporting[6],
                            'Intensity': value_for_exporting[7],
                            'Visibility': value_for_exporting[8],
                            'TrackTemp': value_for_exporting[9],
                            'TracksTempChangesInOneHour': value_for_exporting[10],
                            'TracksCondition': value_for_exporting[11],
                            'RouteWarning': value_for_exporting[12],
                            'FreezingPoint': value_for_exporting[13],
                            'TrackTemp2': value_for_exporting[14],
                            'TracksTemp2ChangesInOneHour': value_for_exporting[15],
                            'TracksCondition2': value_for_exporting[16],
                            'RouteWarning2': value_for_exporting[17],
                            'FreezingPoint2': value_for_exporting[18]
                        }
                    }
                }

                data_for_exporting[j] = child_of_data_for_exporting
                j += 1

            json.dump(data_for_exporting, json_file, indent=1)
