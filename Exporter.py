from CSVExporter import CSVExporter
from JsonExporter import JsonExporter
from AutoRefresher import AutoRefresher


class Exporter(CSVExporter, JsonExporter, AutoRefresher):
    def __init__(self):
        super().__init__()
        self.refresher = AutoRefresher()
