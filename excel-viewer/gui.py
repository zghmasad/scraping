from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem, \
    QLabel


class ExcelViewerUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create widgets
        self.open_button = QPushButton('Open Excel File')
        self.view_button = QPushButton('View')
        self.table = QTableWidget()
        self.status_label = QLabel('')

        # Layouts
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.open_button)
        button_layout.addWidget(self.view_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.table)
        main_layout.addWidget(self.status_label)

        self.setLayout(main_layout)

        # Window settings
        self.setWindowTitle('Excel File Viewer')
        self.resize(800, 600)
