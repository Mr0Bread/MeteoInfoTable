from CSVExporter import CSVExporter
from MySQLExporter import MySQLExporter


class Exporter(CSVExporter, MySQLExporter):
    def __init__(self):
        super().__init__()

