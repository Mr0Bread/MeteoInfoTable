import tkinter as tk
from tkinter import *
from tkinter import ttk
from Request import *
import mysql.connector


class Application(tk.Frame, Request):
    def __init__(self, master):
        super().__init__(master)
        self.request = Request()
        self.master = master
        master.title('iScrap')
        master.geometry('1400x700')
        self.create_table()
        self.create_buttons()

    def create_table(self):
        master_table = self.table_of_contents = ttk.Treeview(self.master, columns=('Stacija',
                                                                                   'Laiks',
                                                                                   'Gaisa temperatūra',
                                                                                   'Gaisa temperatūras tendence (-1 h)',
                                                                                   'Gaisa mitrums',
                                                                                   'Rasas punkts',
                                                                                   'Nokrišņi',
                                                                                   'Intensitāte mm/h',
                                                                                   'Redzamība',
                                                                                   'Ceļa temperatūra 1',
                                                                                   'Ceļa temperatūra 1 tendence (-1h)',
                                                                                   'Ceļa stāvoklis 1',
                                                                                   'Ceļa brīdinājums 1',
                                                                                   'Sasalšanas punkts 1',
                                                                                   'Ceļa temperatūra 2',
                                                                                   'Ceļa temperatūra 2 tendence (-1h)',
                                                                                   'Ceļa stāvoklis 2',
                                                                                   'Ceļa brīdinājums 2',
                                                                                   'Sasalšanas punkts 2',),
                                                             show='headings', height=45)

        master_table.column('Stacija', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Laiks', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Gaisa temperatūra', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Gaisa temperatūras tendence (-1 h)', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Gaisa mitrums', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Rasas punkts', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Nokrišņi', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Intensitāte mm/h', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Redzamība', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Ceļa temperatūra 1', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Ceļa temperatūra 1 tendence (-1h)', width=60, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Ceļa stāvoklis 1', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Ceļa brīdinājums 1', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Sasalšanas punkts 1', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Ceļa temperatūra 2', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Ceļa temperatūra 2 tendence (-1h)', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Ceļa stāvoklis 2', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Ceļa brīdinājums 2', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
        master_table.column('Sasalšanas punkts 2', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)

        master_table.heading('Stacija', text='Stacija')
        master_table.heading('Laiks', text='Laiks')
        master_table.heading('Gaisa temperatūra', text='Gaisa temperatūra')
        master_table.heading('Gaisa temperatūras tendence (-1 h)', text='Gaisa temperatūrastendence (-1 h)')
        master_table.heading('Gaisa mitrums', text='Gaisa mitrums')
        master_table.heading('Rasas punkts', text='Rasas punkts')
        master_table.heading('Nokrišņi', text='Nokrišņi')
        master_table.heading('Intensitāte mm/h', text='Intensitāte mm/h')
        master_table.heading('Redzamība', text='Redzamība')
        master_table.heading('Ceļa temperatūra 1', text='Ceļatemperatūra 1')
        master_table.heading('Ceļa temperatūra 1 tendence (-1h)', text='Ceļatemperatūra 1 tendence (-1h)')
        master_table.heading('Ceļa stāvoklis 1', text='Ceļa stāvoklis 1')
        master_table.heading('Ceļa brīdinājums 1', text='Ceļa brīdinājums 1')
        master_table.heading('Sasalšanas punkts 1', text='Sasalšanas punkts 1')
        master_table.heading('Ceļa temperatūra 2', text='Ceļa temperatūra 2')
        master_table.heading('Ceļa temperatūra 2 tendence (-1h)', text='Ceļa temperatūra 2 tendence (-1h)')
        master_table.heading('Ceļa stāvoklis 2', text='Ceļa stāvoklis 2')
        master_table.heading('Ceļa brīdinājums 2', text='Ceļa brīdinājums 2')
        master_table.heading('Sasalšanas punkts 2', text='Sasalšanas punkts 2')

        scrollbar = tk.Scrollbar(self.master)
        scrollbar.grid(row=2, column=2, ipady=440)

        master_table.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=master_table.yview())

        master_table.grid(row=2, column=1)

    def create_buttons(self):
        self.refresh_button = Button(self.master, text="Please, refresh firstly", width=20,
                                     command=self.refresh_table)
        self.refresh_button.grid(row=0, column=0, pady=20, padx=20)

        fill_button = Button(self.master, text='Fill table', width=20, command=self.fill_table)
        fill_button.grid(row=0, column=1)

        self.send_to_mysql_button = Button(self.master, text="Send database to MySQL", width=20,
                                           command=self.send_to_mysql)
        self.send_to_mysql_button.grid(row=0, column=2, padx=20)

    def send_to_mysql(self):
        self.create_database()
        self.connect_to_database()
        self.create_MySQL_table_in_database()

        self.rows = self.request.table.find_all('tr', attrs={'height': '30'})
        self.values_for_database = []

        for self.row in self.rows:
            self.values_for_database.clear()
            self.cells = self.row.find_all('td')

            for self.cell in self.cells:
                self.values_for_database.append(self.cell.text)

            if len(self.values_for_database) < 19:
                i = 2
                while i < 19:
                    self.values_for_database.append('-')
                    i += 1

            self.command = "INSERT INTO meteoinfotable (Station, Time, TemperatureOfAir, AirsTempChangeInOneHour,  Humidity, DewPoint, Precipitation, Intensity, Visibility, TrackTemp, TracksTempChangesInOneHour, TracksCondition, RouteWarning, FreezingPoint, TrackTemp2, TracksTemp2ChangesInOneHour, TracksCondition2, RouteWarning2, FreezingPoint2) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.my_cursor.execute(self.command, self.values_for_database)
            self.database.commit()

    def create_database(self):
        self.connect_to_MySQL()
        self.my_cursor = self.database.cursor()
        self.command = "CREATE DATABASE meteoinfo"
        self.my_cursor.execute(self.command)

    def create_MySQL_table_in_database(self):
        self.command = "CREATE TABLE meteoinfotable (Station VARCHAR(30), Time VARCHAR(45), TemperatureOfAir VARCHAR(8), AirsTempChangeInOneHour VARCHAR(10),  Humidity VARCHAR(3), DewPoint VARCHAR(6), Precipitation VARCHAR(30), Intensity VARCHAR(6), Visibility VARCHAR(4), TrackTemp VARCHAR(8), TracksTempChangesInOneHour VARCHAR(8), TracksCondition VARCHAR(20), RouteWarning VARCHAR(20), FreezingPoint VARCHAR(10), TrackTemp2 VARCHAR(8), TracksTemp2ChangesInOneHour VARCHAR(8), TracksCondition2 VARCHAR(20), RouteWarning2 VARCHAR(20), FreezingPoint2 VARCHAR(10))"
        self.my_cursor.execute(self.command)
        self.database.commit()

    def connect_to_MySQL(self):
        self.database = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='mr0bread',
        )

    def refresh_table(self):
        self.request.get_info_for_table()
        self.refresh_button.configure(text="Table is refreshed")

    def fill_table(self):
        self.table_of_contents.delete(*self.table_of_contents.get_children())
        self.values = []

        self.rows = self.request.table.find_all('tr', attrs={'height': '30'})
        i = 0
        for self.row in self.rows:
            self.values.clear()
            self.cells = self.row.find_all('td')

            for self.cell in self.cells:
                self.values.append(self.cell.text)
            self.table_of_contents.insert('', i, values=self.values)
            i += 1

    def connect_to_database(self):
        self.database.connect(
            host='localhost',
            user='root',
            passwd='mr0bread',
            database='meteoinfo'
        )


root = Tk()
app = Application(master=root)
app.mainloop()
