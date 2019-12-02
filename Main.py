from GUI import Request, MySQLExporter, GUI

from tkinter import *

root = Tk()
app = GUI(master=root)


class Main(GUI):
    def __init__(self):
        super().__init__(app)
        self.gui = app
        self.exporter = MySQLExporter()
        self.request = Request()


app.mainloop()
