import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtCore import QUrl, QByteArray, Qt

class ImageLoader(QWidget):
    def __init__(self, image_link: str):
        super().__init__()

        self.image_link = image_link

        # UI Setup
        self.label = QLabel("Loading image...")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Create a single instance of QNetworkAccessManager
        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self.on_image_downloaded)

        # Start downloading the image
        self.load_image()

    def change_image(self, new_link):
        self.image_link = new_link
        self.load_image()

    def load_image(self):
        """Fetches the image from the web."""
        self.label.setText("Loading image...")  # Show loading text
        url = QUrl(self.image_link)
        self.manager.get(QNetworkRequest(url))  # Send request

    def on_image_downloaded(self, reply):
        """Handles the downloaded image and updates the QLabel."""
        if reply.error():
            self.label.setText("Failed to load image")
        else:
            pixmap = QPixmap()
            pixmap.loadFromData(reply.readAll())  # Load into QPixmap
            scaled_pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.label.setPixmap(scaled_pixmap)  # Display image
            self.label.setText("")  # Remove the loading text

        reply.deleteLater()  # Clean up network reply