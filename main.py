# main.py
import sys
from PyQt5.QtWidgets import QApplication
from view import XMLReaderView
from controller import XMLReaderController

def main():
    app = QApplication(sys.argv)
    view = XMLReaderView()
    controller = XMLReaderController(view)
    view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()