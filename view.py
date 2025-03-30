# view.py
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, 
    QFileDialog, QTableWidget, QTableWidgetItem, QMessageBox, QDialog, QListWidget
)
from DefineConst import *

class XMLReaderView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_TITLE)
        self.resize(*APP_SIZE)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        
        self.create_widgets()
        
    def create_widgets(self):
        # File path frame
        file_layout = QHBoxLayout()
        
        self.file_label = QLabel(FILE_LABEL)
        file_layout.addWidget(self.file_label)
        
        self.file_path_edit = QLineEdit()
        file_layout.addWidget(self.file_path_edit)
        
        self.browse_button = QPushButton(BROWSE_BUTTON_TEXT)
        file_layout.addWidget(self.browse_button)
        
        self.layout.addLayout(file_layout)
        
        # Search frame
        search_layout = QHBoxLayout()
        
        self.search_label = QLabel(SEARCH_LABEL)
        search_layout.addWidget(self.search_label)
        
        self.search_edit = QLineEdit()
        search_layout.addWidget(self.search_edit)
        
        self.search_button = QPushButton(SEARCH_BUTTON_TEXT)
        search_layout.addWidget(self.search_button)
        
        self.history_button = QPushButton(HISTORY_BUTTON_TEXT)
        search_layout.addWidget(self.history_button)
        
        self.layout.addLayout(search_layout)
        
        # Results area
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(len(COLUMN_NAMES))
        self.results_table.setHorizontalHeaderLabels([COLUMN_HEADINGS[col] for col in COLUMN_NAMES])
        self.layout.addWidget(self.results_table)
        
    def set_browse_callback(self, callback):
        self.browse_button.clicked.connect(callback)
        
    def set_search_callback(self, callback):
        self.search_button.clicked.connect(callback)
        
    def set_history_callback(self, callback):
        self.history_button.clicked.connect(callback)
        
    def get_file_path(self):
        return self.file_path_edit.text()
        
    def get_search_element(self):
        return self.search_edit.text()
        
    def set_file_path(self, path):
        self.file_path_edit.setText(path)
        
    def clear_results(self):
        self.results_table.setRowCount(0)
        
    def display_results(self, results):
        self.clear_results()
        self.results_table.setRowCount(len(results))
        for row, result in enumerate(results):
            self.results_table.setItem(row, 0, QTableWidgetItem(result["name"]))
            self.results_table.setItem(row, 1, QTableWidgetItem(result["value"]))
            self.results_table.setItem(row, 2, QTableWidgetItem(result["xpath"]))
            
    def show_error(self, message):
        QMessageBox.critical(self, ERROR_TITLE, message)
        
    def show_info(self, title, message):
        QMessageBox.information(self, title, message)
        
    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open XML File", "", FILE_TYPES)
        if file_path:
            self.file_path_edit.setText(file_path)
        return file_path
        
    def display_history(self, history_items):
        if not history_items:
            self.show_info(HISTORY_TITLE, NO_HISTORY)
            return
            
        history_dialog = QDialog(self)
        history_dialog.setWindowTitle(HISTORY_TITLE)
        history_dialog.resize(500, 300)
        
        list_widget = QListWidget(history_dialog)
        list_widget.resize(500, 300)
        
        for idx, item in enumerate(history_items):
            list_widget.addItem(HISTORY_LIST_ITEM.format(idx+1, item['file'], item['term']))
        
        history_dialog.exec_()