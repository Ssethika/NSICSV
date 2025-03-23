from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QWidget, QLineEdit, QVBoxLayout, QComboBox


class Table(QWidget):
    """ Widget for the table"""
    def __init__(self, table_list: [[]], action):

        super().__init__()
        self.action = action
        self.table_list = table_list
        print(table_list)
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.textChanged.connect(self.filter_table)
        self.search_bar.setMaximumWidth(930)

        self.table = QTableWidget()
        self.table.setMaximumWidth(930)

        self.type_combo = QComboBox(self)
        self.type_combo.addItem("All Types")  # Default option
        self.types = [
            "Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison",
            "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark",
            "Steel", "Fairy"
        ]

        self.type_combo.addItems(sorted(self.types))
        self.type_combo.currentTextChanged.connect(self.update_table)


        self.stat_combo = QComboBox(self)
        self.stat_combo.addItems(["Attack", "Defense", "Sp. Attack", "Sp. Defense"])  # Sorting options
        self.stat_combo.currentTextChanged.connect(self.update_table)



        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.search_bar)
        self.vlayout.addWidget(self.type_combo)
        self.vlayout.addWidget(self.stat_combo)
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

    def update_table(self):
        """Update the table based on the filters and sorting options."""
        selected_type = self.type_combo.currentText()
        selected_stat = self.stat_combo.currentText()  # Convert to lowercase for dict keys

        # Filter by type
        filtered_pokemon = [p for p in self.table_list if selected_type == "All Types" or p["Type1"] == selected_type or p["Type2"] == selected_type]

        # Sort by selected stat if chosen
        if selected_stat in {"Attack", "Defense", "Sp. Attack", "Sp. Defense"}:
            filtered_pokemon.sort(key=lambda p: p[selected_stat], reverse=True)
            print()

        # Apply search filter and update table display
        self.apply_filters(filtered_pokemon)

    def apply_filters(self, filtered_pokemon):
        """Apply the filters (search + type + stat sorting) and update table."""
        search_text = self.search_bar.text().lower()

        # Update the table data with the filtered and sorted Pokémon list
        self.table.setRowCount(len(filtered_pokemon))  # Adjust row count
        for row_index, pokemon in enumerate(filtered_pokemon):
            # Apply search filter
            if any(search_text in str(value).lower() for value in pokemon.values()):
                for col_index, (key, value) in enumerate(pokemon.items()):
                    self.table.setItem(row_index, col_index, QTableWidgetItem(str(value)))
            else:
                self.table.setRowHidden(row_index, True)

        self.table.repaint()

    def filter_table(self):
        """Filter table rows based on search input"""
        search_text = self.search_bar.text().lower()

        for row in range(self.table.rowCount()):
            item = self.table.item(row, 0)  # Get first column (Name)
            if item and search_text in item.text().lower():
                self.table.setRowHidden(row, False)  # Show row
            else:
                self.table.setRowHidden(row, True)  # Hide row

