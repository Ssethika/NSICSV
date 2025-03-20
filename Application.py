from tkinter.messagebox import showinfo

from PyQt5.QtCore import Qt

from CSVFileFunctions import CSVFileFunctions
from CSVFileManagement import CSVFileManagement
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QSizePolicy, \
    QCheckBox, QTextEdit, QLineEdit

from Poke_api import get_pokemon_sprite, get_pokemon_description
from PokemonView import PokemonView
from Widget import Table
from ImageLoader import ImageLoader
from PokemonView import PokemonView

class Application():
    def __init__(self):
        self.file_manager = CSVFileManagement("file.csv", "file2.csv")
        self.output_reader = CSVFileFunctions.read_csv_file_to_file("output.csv")
        print(self.output_reader)
        self.app = QApplication([])
        self.table = Table(self.output_reader, self.show_info)
        self.window = QWidget()
        self.window.setGeometry(100, 100, 300, 200)  # (x, y, width, height)
        self.window.setWindowTitle("PyQt5 Window")
        self.hlayout = QHBoxLayout()
        self.pokemon_view_widget = PokemonView(self.table, self.show_info)
        self.button = QPushButton("Filter")
        self.button.setMaximumWidth(100)
        self.vlayout_pokemon = QVBoxLayout()
        self.vlayout_pokemon.addLayout(self.pokemon_view_widget.vlayout)
        self.vlayout_pokemon.addWidget(self.button)
        self.hlayout.addLayout(self.table.vlayout)
        self.hlayout.addLayout(self.vlayout_pokemon)
        self.window.setLayout(self.hlayout)

    def run(self):
        self.window.show()
        self.app.exec_()

    def show_info(self):
        pokemon_name = self.table.table.item(self.table.table.currentRow(),0).text()
        self.pokemon_view_widget.image.change_image(get_pokemon_sprite(pokemon_name))
        self.pokemon_view_widget.pokemon_description.setText(get_pokemon_description(pokemon_name))