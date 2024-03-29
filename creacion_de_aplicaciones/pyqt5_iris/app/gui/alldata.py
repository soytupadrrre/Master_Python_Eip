# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\app\gui\template\data.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from app import RestIris


class Ui_DialogDatos(object):
    def setupUi(self, DialogDatos):
        DialogDatos.setObjectName("DialogDatos")
        DialogDatos.resize(803, 441)
        self.scrollArea = QtWidgets.QScrollArea(DialogDatos)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 801, 441))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 439))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 801, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(DialogDatos)
        QtCore.QMetaObject.connectSlotsByName(DialogDatos)

    def retranslateUi(self, DialogDatos):
        _translate = QtCore.QCoreApplication.translate
        DialogDatos.setWindowTitle(_translate("DialogDatos", "Víctor Luque - PyQT5 - Datos"))
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 140)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DialogDatos", "Sepal Length (cm)"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DialogDatos", "Sepal Width (cm)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("DialogDatos", "Petal Length (cm)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("DialogDatos", "Petal Width (cm)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("DialogDatos", "Species"))
        self.load_data()

    def load_data(self):
        iris = RestIris()
        data = iris.get_data()
        self.tableWidget.setRowCount(len(data))
        row = 0
        for obj in data:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(obj["sepal_length"])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(obj["sepal_width"])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(obj["petal_length"])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(obj["petal_width"])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(obj["species"])))
            row += 1
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogDatos = QtWidgets.QDialog()
    ui = Ui_DialogDatos()
    ui.setupUi(DialogDatos)
    DialogDatos.show()
    sys.exit(app.exec_())
