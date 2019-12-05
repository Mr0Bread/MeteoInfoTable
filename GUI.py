import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
from Exporter import Exporter


def is_schema_created():
    try:
        mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='mr0bread',
            database='meteoinfo'
        )
        return True
    except mysql.connector.errors.ProgrammingError:
        return False


class GUI(tk.Frame, Exporter):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.exporter = Exporter()
        master.title('iScrap')
        master.geometry('1400x700+250+200')
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
                                                             show='headings', height=50)

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
        master_table.column('Ceļa temperatūra 1 tendence (-1h)', width=80, anchor=tk.CENTER, stretch=1, minwidth=60)
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

        scrollbarV = tk.Scrollbar(self.master, orient=VERTICAL)
        scrollbarV.grid(row=0, column=2, ipady=488, rowspan=5)

        master_table.configure(yscrollcommand=scrollbarV.set)
        scrollbarV.configure(command=master_table.yview())

        master_table.grid(row=0, column=1, rowspan=5, pady=10)

    def create_buttons(self):
        self.refresh_info_for_table_button = Button(self.master, text="Please, refresh firstly", width=25,
                                                    command=self.refresh_table)
        self.refresh_info_for_table_button.grid(row=0, column=0, padx=5, pady=10, sticky=N)

        self.fill_button = Button(self.master, text='Fill table', width=25, command=self.fill_table, state=DISABLED)
        self.fill_button.grid(row=0, column=0, padx=5)

        self.send_to_mysql_button = Button(self.master, text="Send table to MySQL Database", width=25,
                                           command=self.send_to_mysql_and_refresh_related_buttons, state=DISABLED)
        self.send_to_mysql_button.grid(row=0, column=0, padx=5, sticky=S)

        self.drop_schema_button = Button(self.master, command=self.drop_schema_and_refresh_related_buttons, width=25,
                                         text="Connect to MySQL firstly", state=DISABLED)
        self.drop_schema_button.grid(row=1, column=0, padx=5, sticky=N)

        self.export_to_CSV_button = Button(self.master, width=25, text="Export table to CSV", state=DISABLED,
                                           command=self.exporter.export_to_CSV)
        self.export_to_CSV_button.grid(row=1, column=0)

        self.export_to_json_button = Button(self.master, width=25, text="Export table to JSON", state=DISABLED,
                                            command=self.exporter.export_to_json)
        self.export_to_json_button.grid(row=2, column=0, sticky=N)

        self.enable_auto_refresh_button = Button(self.master, width=23, text="Auto-refresh disabled", state=DISABLED,
                                                 command=self.enable_auto_refresh_and_refresh_related_buttons)
        self.enable_auto_refresh_button.grid(row=0, column=3, padx=5, sticky=N, pady=10)

    def refresh_table(self):
        self.exporter.request.get_info_for_table()
        self.refresh_info_for_table_button.configure(text="Table is refreshed")
        self.configure_buttons()

    def send_to_mysql_and_refresh_related_buttons(self):
        self.exporter.send_to_mysql(self.exporter.request.table.find_all('tr', attrs={'height': '30'}))
        self.enable_auto_refresh_button.configure(state=ACTIVE)
        self.refresh_buttons()

    def enable_auto_refresh_and_refresh_related_buttons(self):
        self.exporter.refresher.enable_auto_refresh()
        self.enable_auto_refresh_button.configure(text="Auto-refresh enabled",
                                                  command=self.disable_auto_refresh_and_refresh_related_buttons)
        self.refresh_info_for_table_button.configure(state=DISABLED, text="Auto-refresh enabled")

    def disable_auto_refresh_and_refresh_related_buttons(self):
        self.exporter.refresher.disable_auto_refresh()
        self.enable_auto_refresh_button.configure(text="Auto-refresh disabled",
                                                  command=self.enable_auto_refresh_and_refresh_related_buttons)
        self.refresh_info_for_table_button.configure(state=ACTIVE, text="Refresh info")

    def drop_schema_and_refresh_related_buttons(self):
        if self.exporter.refresher.thread_is_running:
            self.disable_auto_refresh_and_refresh_related_buttons()

        self.drop_schema()
        self.drop_schema_button.configure(state=DISABLED, text="Database deleted")
        self.send_to_mysql_button.configure(state=ACTIVE, text="Create new database")
        self.enable_auto_refresh_button.configure(state=DISABLED)

    def fill_table(self):
        self.table_of_contents.delete(*self.table_of_contents.get_children())
        self.values = []

        self.rows = self.exporter.request.table.find_all('tr', attrs={'height': '30'})
        i = 0
        for self.row in self.rows:
            self.values.clear()
            self.cells = self.row.find_all('td')

            for self.cell in self.cells:
                self.values.append(self.cell.text)
            self.table_of_contents.insert('', i, values=self.values)
            i += 1
        self.fill_button.configure(text="Refill table")

    def configure_buttons(self):
        self.fill_button.configure(state=ACTIVE)
        self.export_to_CSV_button.configure(state=ACTIVE)
        self.export_to_json_button.configure(state=ACTIVE)

        if is_schema_created():
            self.send_to_mysql_button.configure(state=DISABLED)
            self.drop_schema_button.configure(state=ACTIVE, text="Delete database firstly")
            self.enable_auto_refresh_button.configure(state=ACTIVE)
        else:
            self.send_to_mysql_button.configure(state=ACTIVE)
            self.drop_schema_button.configure(state=DISABLED, text="Deleting is not needed")

    def refresh_buttons(self):
        self.send_to_mysql_button.configure(state=DISABLED, text="Database created")
        self.drop_schema_button.configure(state=ACTIVE, text="Delete created database")
