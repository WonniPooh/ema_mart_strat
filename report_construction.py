from PySide6.QtCore import Qt, QAbstractTableModel
from PySide6.QtGui import QBrush

class FinishedDealsDataTableModel(QAbstractTableModel):
    def __init__(self, data):
        super(FinishedDealsDataTableModel, self).__init__()
        self.header_labels = ["Инструмент", "ТФ", "Направление", "Плечо", "Начало", "Окончание",
                              "Позиция $", "Докупок", "Результат", "Результат %", "Коммиссия"]

        self._data = data
        self.last_cfg_num = None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def data(self, index, role):

        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()].get_by_index(index.column())

        if role == Qt.BackgroundRole:
            if index.column() == 8: #results
                data = self._data[index.row()].get_by_index(index.column())
                color = QBrush(Qt.lightGray)
                if data < 0:
                    color = QBrush(Qt.red)
                elif data > 0:
                    color = QBrush(Qt.green)
                return color

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self.header_labels)

class RunningDealsDataTableModel(QAbstractTableModel):
    def __init__(self, data):
        super(RunningDealsDataTableModel, self).__init__()
        self.header_labels = ["Инструмент", "Направление", "Плечо", "ТФ(мин)",
                              "Вложено $", "Сред. Цена", "Докупок", "Время Открытия"]
        self._data = data

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        if len(self._data) > 0:
            return len(self._data[0])
        else:
            return 0
