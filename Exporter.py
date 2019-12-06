from CSVExporter import CSVExporter
from MySQLExporter import MySQLExporter
from JsonExporter import JsonExporter


class Exporter(CSVExporter, MySQLExporter, JsonExporter):
    def __init__(self):
        super().__init__()

