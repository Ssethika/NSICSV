import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtCore import QUrl, QByteArray, Qt

class ImageLoader(QWidget):
    def __init__(self, image_link: str):
        super().__init__()

        self.image_link = image_link

        # UI Setup
        self.label = QLabel("Loading image...")

        self.retry_button = QPushButton("Retry")
        self.retry_button.hide()
        self.retry_button.clicked.connect(self.load_image)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.retry_button)
        self.setLayout(layout)


        # Create a single instance of QNetworkAccessManager
        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self.on_image_downloaded)

        # Start downloading the image

    def change_image(self, new_link):
        self.image_link = new_link
        self.load_image()

    def load_image(self):
        """Fetches the image from the web."""
        self.label.setText("Loading image...")  # Show loading text
        url = QUrl(self.image_link)
        reply = self.manager.get(QNetworkRequest(url))
        reply.errorOccurred.connect(lambda error: self.handle_network_error(error, reply))

        # Send request

    def on_image_downloaded(self, reply):
        """Handles the downloaded image and updates the QLabel."""
        if reply.error():
            self.label.setText("Failed to load image")
            error_message = f"Failed to load image: {reply.errorString()}"
            print(error_message)  # Log error for debugging
            self.label.setText(error_message)
            self.retry_button.show()

        else:
            self.retry_button.hide()
            self.label.setText("")
            pixmap = QPixmap()
            pixmap.loadFromData(reply.readAll())  # Load into QPixmap
            scaled_pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.label.setPixmap(scaled_pixmap)  # Display image
            self.label.setText("")  # Remove the loading text

        reply.deleteLater()  # Clean up network reply

    def handle_network_error(self, error, reply):
        self.label.setText("Network Error")
        print(error, reply)