# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\app\gui\template\resumen.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from app import RestIris

class Ui_DialogResumen(object):
    def setupUi(self, DialogResumen):
        DialogResumen.setObjectName("DialogResumen")
        DialogResumen.resize(566, 482)
        self.verticalLayoutWidget = QtWidgets.QWidget(DialogResumen)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 160, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonTotal = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonTotal.setFont(font)
        self.pushButtonTotal.setObjectName("pushButtonTotal")
        self.verticalLayout.addWidget(self.pushButtonTotal)
        self.pushButtonMedia = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonMedia.setFont(font)
        self.pushButtonMedia.setObjectName("pushButtonMedia")
        self.verticalLayout.addWidget(self.pushButtonMedia)
        self.pushButtonMinimo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonMinimo.setFont(font)
        self.pushButtonMinimo.setObjectName("pushButtonMinimo")
        self.verticalLayout.addWidget(self.pushButtonMinimo)
        self.pushButtonMaximo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonMaximo.setFont(font)
        self.pushButtonMaximo.setObjectName("pushButtonMaximo")
        self.verticalLayout.addWidget(self.pushButtonMaximo)
        self.pushButtonDesviacion = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonDesviacion.setFont(font)
        self.pushButtonDesviacion.setObjectName("pushButtonDesviacion")
        self.verticalLayout.addWidget(self.pushButtonDesviacion)
        self.pushButtonPer25 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonPer25.setFont(font)
        self.pushButtonPer25.setObjectName("pushButtonPer25")
        self.verticalLayout.addWidget(self.pushButtonPer25)
        self.pushButtonPer50 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonPer50.setFont(font)
        self.pushButtonPer50.setObjectName("pushButtonPer50")
        self.verticalLayout.addWidget(self.pushButtonPer50)
        self.pushButtonPer75 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonPer75.setFont(font)
        self.pushButtonPer75.setObjectName("pushButtonPer75")
        self.verticalLayout.addWidget(self.pushButtonPer75)
        self.gridLayoutWidget = QtWidgets.QWidget(DialogResumen)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 130, 341, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.labelSplRes = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSplRes.setFont(font)
        self.labelSplRes.setObjectName("labelSplRes")
        self.gridLayout.addWidget(self.labelSplRes, 0, 2, 1, 1)
        self.labelSpwRes = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSpwRes.setFont(font)
        self.labelSpwRes.setObjectName("labelSpwRes")
        self.gridLayout.addWidget(self.labelSpwRes, 1, 2, 1, 1)
        self.labelPtlRes = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelPtlRes.setFont(font)
        self.labelPtlRes.setObjectName("labelPtlRes")
        self.gridLayout.addWidget(self.labelPtlRes, 2, 2, 1, 1)
        self.labelPtwRes = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelPtwRes.setFont(font)
        self.labelPtwRes.setObjectName("labelPtwRes")
        self.gridLayout.addWidget(self.labelPtwRes, 3, 2, 1, 1)
        
        self.render_resumen()
        self.pushButtonTotal.clicked.connect(self.show_total)
        self.pushButtonMedia.clicked.connect(self.show_media)
        self.pushButtonMinimo.clicked.connect(self.show_minimo)
        self.pushButtonMaximo.clicked.connect(self.show_maximo)
        self.pushButtonDesviacion.clicked.connect(self.show_desviacion)
        self.pushButtonPer25.clicked.connect(self.show_per25)
        self.pushButtonPer50.clicked.connect(self.show_per50)
        self.pushButtonPer75.clicked.connect(self.show_per75)

        self.retranslateUi(DialogResumen)
        QtCore.QMetaObject.connectSlotsByName(DialogResumen)

    def retranslateUi(self, DialogResumen):
        _translate = QtCore.QCoreApplication.translate
        DialogResumen.setWindowTitle(_translate("DialogResumen", "Víctor Luque - PyQT5 - Resumen"))
        self.pushButtonTotal.setText(_translate("DialogResumen", "Totales"))
        self.pushButtonMedia.setText(_translate("DialogResumen", "Media"))
        self.pushButtonMinimo.setText(_translate("DialogResumen", "Mínimo"))
        self.pushButtonMaximo.setText(_translate("DialogResumen", "Máximo"))
        self.pushButtonDesviacion.setText(_translate("DialogResumen", "Desviación"))
        self.pushButtonPer25.setText(_translate("DialogResumen", "25%"))
        self.pushButtonPer50.setText(_translate("DialogResumen", "50%"))
        self.pushButtonPer75.setText(_translate("DialogResumen", "75%"))
        self.label_2.setText(_translate("DialogResumen", "Sepal Width (cm): "))
        self.label_3.setText(_translate("DialogResumen", "Petal Length (cm):"))
        self.label_4.setText(_translate("DialogResumen", "Petal Width (cm):"))
        self.label.setText(_translate("DialogResumen", "Sepal Length (cm):"))
        self.labelSplRes.setText(_translate("DialogResumen", "0"))
        self.labelSpwRes.setText(_translate("DialogResumen", "0"))
        self.labelPtlRes.setText(_translate("DialogResumen", "0"))
        self.labelPtwRes.setText(_translate("DialogResumen", "0"))

    def render_resumen(self):
        iris = RestIris()
        data =  iris.get_resumen()
        self.count = data["count"]
        self.mean = data["mean"]
        self.std = data["std"]
        self.min = data["min"]
        self.max = data["max"]
        self.percentile25 = data["25%"]
        self.percentile50 = data["50%"]
        self.percentile75 = data["75%"]

    def show_total(self):
        self.labelSplRes.setText(str(self.count["sepal_length"]))
        self.labelSpwRes.setText(str(self.count["sepal_width"]))
        self.labelPtlRes.setText(str(self.count["petal_length"]))
        self.labelPtwRes.setText(str(self.count["petal_width"]))

    def show_media(self):
        self.labelSplRes.setText(str(self.mean["sepal_length"]))
        self.labelSpwRes.setText(str(self.mean["sepal_width"]))
        self.labelPtlRes.setText(str(self.mean["petal_length"]))
        self.labelPtwRes.setText(str(self.mean["petal_width"]))

    def show_minimo(self):
        self.labelSplRes.setText(str(self.min["sepal_length"]))
        self.labelSpwRes.setText(str(self.min["sepal_width"]))
        self.labelPtlRes.setText(str(self.min["petal_length"]))
        self.labelPtwRes.setText(str(self.min["petal_width"]))

    def show_maximo(self):
        self.labelSplRes.setText(str(self.max["sepal_length"]))
        self.labelSpwRes.setText(str(self.max["sepal_width"]))
        self.labelPtlRes.setText(str(self.max["petal_length"]))
        self.labelPtwRes.setText(str(self.max["petal_width"]))

    def show_desviacion(self):
        self.labelSplRes.setText(str(self.std["sepal_length"]))
        self.labelSpwRes.setText(str(self.std["sepal_width"]))
        self.labelPtlRes.setText(str(self.std["petal_length"]))
        self.labelPtwRes.setText(str(self.std["petal_width"]))

    def show_per25(self):
        self.labelSplRes.setText(str(self.percentile25["sepal_length"]))
        self.labelSpwRes.setText(str(self.percentile25["sepal_width"]))
        self.labelPtlRes.setText(str(self.percentile25["petal_length"]))
        self.labelPtwRes.setText(str(self.percentile25["petal_width"]))

    def show_per50(self):
        self.labelSplRes.setText(str(self.percentile50["sepal_length"]))
        self.labelSpwRes.setText(str(self.percentile50["sepal_width"]))
        self.labelPtlRes.setText(str(self.percentile50["petal_length"]))
        self.labelPtwRes.setText(str(self.percentile50["petal_width"]))

    def show_per75(self):
        self.labelSplRes.setText(str(self.percentile75["sepal_length"]))
        self.labelSpwRes.setText(str(self.percentile75["sepal_width"]))
        self.labelPtlRes.setText(str(self.percentile75["petal_length"]))
        self.labelPtwRes.setText(str(self.percentile75["petal_width"]))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogResumen = QtWidgets.QDialog()
    ui = Ui_DialogResumen()
    ui.setupUi(DialogResumen)
    DialogResumen.show()
    sys.exit(app.exec_())
