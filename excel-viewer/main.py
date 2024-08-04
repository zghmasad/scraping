import sys
from PyQt5.QtWidgets import QApplication, QFileDialog
from gui import ExcelViewerUI
from viewer import load_excel_file, display_data_in_table


class ExcelViewerApp(ExcelViewerUI):
    def __init__(self):
        super().__init__()

        self.file_path = None

        self.open_button.clicked.connect(self.open_file_dialog)
        self.view_button.clicked.connect(self.view_file)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx; *.xls)",
                                                   options=options)
        if file_path:
            self.file_path = file_path
            self.status_label.setText(f"Selected file: {file_path}")

    def view_file(self):
        if self.file_path:
            data = load_excel_file(self.file_path)
            if data is not None:
                display_data_in_table(data, self.table)
            else:
                self.status_label.setText("Failed to load the file.")
        else:
            self.status_label.setText("No file selected.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer_app = ExcelViewerApp()
    viewer_app.show()
    sys.exit(app.exec_())
