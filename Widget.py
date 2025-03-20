from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QWidget, QLineEdit, QVBoxLayout


class Table(QWidget):
    def __init__(self, table_list: [[]], action):
        super().__init__()
        self.action = action
        self.table_list = table_list
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.textChanged.connect(self.filter_table)
        self.search_bar.setMaximumWidth(930)
        self.table = QTableWidget()
        self.table.setMaximumWidth(930)
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.search_bar)
        self.vlayout.addWidget(self.table)

        self.initialize_table()

    def initialize_table(self):
        first_column_descriptors = self.table_list[0].keys()
        self.table.setRowCount(len(self.table_list) - 1)  # Excluding header row if present
        self.table.setColumnCount(len(first_column_descriptors))  # Based on the first row (headers)

        # Set headers (assuming the first row contains headers)
        self.table.setHorizontalHeaderLabels(first_column_descriptors)

        for row_index, li in enumerate(self.table_list):
            print(li)
            for col_index, el in enumerate(li.values()):
                self.table.setItem(row_index, col_index, QTableWidgetItem(el))

        self.table.cellClicked.connect(self.action)

    def filter_table(self):
        """Filter table rows based on search input"""
        search_text = self.search_bar.text().lower()

        for row in range(self.table.rowCount()):
            item = self.table.item(row, 0)  # Get first column (Name)
            if item and search_text in item.text().lower():
                self.table.setRowHidden(row, False)  # Show row
            else:
                self.table.setRowHidden(row, True)  # Hide ro