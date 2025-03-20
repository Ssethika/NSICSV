from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QWidget, QLabel, QVBoxLayout, QFrame
from Poke_api import get_pokemon_sprite, get_pokemon_description
from ImageLoader import ImageLoader

class PokemonView(QFrame):
    def __init__(self, table, action):
        super().__init__()
        self.table = table
        self.action = action
        self.image = ImageLoader("pikachu")
        self.pokemon_description = QLabel("")
        self.image = ImageLoader(get_pokemon_sprite("pikachu"))
        self.image.setMaximumHeight(450)
        # self.pokemon_description.setMinimumWidth(300)r
        self.pokemon_description.setContentsMargins(70, 0, 0, 0)
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.image)
        self.vlayout.addWidget(self.pokemon_description)
        self.vlayout.setAlignment(Qt.AlignTop)
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Panel)

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.black, 2)  # Black border, 2 pixels thick
        painter.setPen(pen)
        painter.drawRect(0, 0, self.width() - 1, self.height() - 1)  # Draw border
