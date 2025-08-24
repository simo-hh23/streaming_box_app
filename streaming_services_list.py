# streaming_services_list.py

import sys
import os
import json
import webbrowser
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QToolButton, QSizePolicy
)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, Qt

# ------------------------
# Helper for PyInstaller
# ------------------------
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# ------------------------
# Load streaming services
# ------------------------
CONFIG_FILE = resource_path("services.json")

try:
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        services = json.load(f)
except Exception as e:
    print(f"Error loading services.json: {e}")
    services = []

# ------------------------
# Main App Window
# ------------------------
class StreamingLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("")  # No title
        self.setStyleSheet("background-color: #222;")  # Dark background
        self.showMaximized()  # Fullscreen

        grid = QGridLayout()
        grid.setSpacing(15)

        max_columns = 5  # Adjust for number of tiles per row
        row = col = 0

        for service in services:
            name = service.get("name", "Unknown")
            url = service.get("url", "")
            icon_path = resource_path(service.get("icon", ""))

            tile = QToolButton()
            tile.setText(name)
            tile.setFont(QFont("Arial", 12))
            tile.setIcon(QIcon(icon_path))
            tile.setIconSize(QSize(96, 96))
            tile.setMinimumSize(180, 160)
            tile.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            tile.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            tile.setStyleSheet("""
                QToolButton {
                    background-color: #333;
                    color: white;
                    border-radius: 12px;
                    padding: 10px;
                }
                QToolButton:hover {
                    background-color: #555;
                }
            """)
            tile.clicked.connect(lambda _, url=url: webbrowser.open(url))
            grid.addWidget(tile, row, col)

            col += 1
            if col >= max_columns:
                col = 0
                row += 1

        self.setLayout(grid)

# ------------------------
# Run Application
# ------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    launcher = StreamingLauncher()
    launcher.show()
    sys.exit(app.exec_())
