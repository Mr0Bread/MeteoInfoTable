from CSVExporter import CSVExporter
from JsonExporter import JsonExporter
from AutoRefresher import AutoRefresher
from XLSxExporter import XLSxExporter


class Exporter(CSVExporter, JsonExporter, XLSxExporter):
    def __init__(self):
        super().__init__()
        self.refresher = AutoRefresher()

