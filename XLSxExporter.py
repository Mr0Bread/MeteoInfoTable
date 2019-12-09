import xlsxwriter
from Request import Request


class XLSxExporter:
    def __init__(self):
        self.request = Request()
        self.workbook = xlsxwriter.Workbook('MeteoInfoTableXLSX.xlsx')
        self.worksheet = self.workbook.add_worksheet()
        self.row = 0
        self.col = 0

    def export_to_xlsx(self):
        list_for_values = []

        rows = self.request.table.find_all('tr', attrs={'height': '30'})

        for row in rows:
            list_for_values.clear()
            cells = row.find_all('td')

            for cell in cells:
                list_for_values.append(cell.text)

            if len(list_for_values) < 19:
                for i in range(2, 19):
                    list_for_values.append('')

            # for station, time, temperatureOfAir, airsTempChangeInOneHour, humidity, dewPoint, precipitation, intensity, visibility, trackTemp, tracksTempChangesInOneHour, tracksCondition, routeWarning, freezingPoint, trackTemp2, tracksTemp2ChangesInOneHour, tracksCondition2, routeWarning2, freezingPoint2 in list_for_values:
            #     self.worksheet.write(self.row, self.col)

            for x in range(19):
                self.worksheet.write(self.row, self.col + x, list_for_values[x])
            self.row += 1

        self.worksheet.set_column(0, 18, 23)
        self.workbook.close()
