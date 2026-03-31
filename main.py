import sys
from PySide6.QtWidgets import QApplication
from ui.ui import App

app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec())