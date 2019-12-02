from GUI import *

from tkinter import *

root = Tk()
app = GUI(master=root)


class Main(GUI):
    def __init__(self):
        super().__init__(app)
        self.gui = app
        self.mysql_exporter = MySQLExporter()
        self.csv_exporter = CSVExporter()
        self.request = Request()


app.mainloop()
