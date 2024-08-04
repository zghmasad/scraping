import pandas as pd
from PyQt5.QtWidgets import QTableWidgetItem


def load_excel_file(file_path):
    try:
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return None


def display_data_in_table(data, table_widget):
    table_widget.setColumnCount(len(data.columns))
    table_widget.setRowCount(len(data.index))
    table_widget.setHorizontalHeaderLabels(data.columns)

    for row in range(len(data.index)):
        for col in range(len(data.columns)):
            item = QTableWidgetItem(str(data.iat[row, col]))
            table_widget.setItem(row, col, item)
