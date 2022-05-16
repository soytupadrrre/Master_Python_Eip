# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\app\gui\template\home.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
try:
    from alldata import Ui_DialogDatos
    from resumen import Ui_DialogResumen
    from precision import Ui_DialogPrecision
    from insertar import Ui_DialogInsertar
    from predecir import Ui_DialogPredecir
    from actualizar_id import Ui_DialogActualizarPorID
    from actualizar_ultimo import Ui_DialogActualizarUltimo
    from eliminar import Ui_DialogEliminar
except:
    from app.gui.alldata import Ui_DialogDatos
    from app.gui.resumen import Ui_DialogResumen
    from app.gui.precision import Ui_DialogPrecision
    from app.gui.insertar import Ui_DialogInsertar
    from app.gui.predecir import Ui_DialogPredecir
    from app.gui.actualizar_id import Ui_DialogActualizarPorID
    from app.gui.actualizar_ultimo import Ui_DialogActualizarUltimo
    from app.gui.eliminar import Ui_DialogEliminar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 451)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 601, 401))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 26))
        self.menubar.setObjectName("menubar")
        self.menuVer = QtWidgets.QMenu(self.menubar)
        self.menuVer.setObjectName("menuVer")
        self.menuInsertar = QtWidgets.QMenu(self.menubar)
        self.menuInsertar.setObjectName("menuInsertar")
        self.menuActualizar = QtWidgets.QMenu(self.menubar)
        self.menuActualizar.setObjectName("menuActualizar")
        self.menuEliminar = QtWidgets.QMenu(self.menubar)
        self.menuEliminar.setObjectName("menuEliminar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionVerDatos = QtWidgets.QAction(MainWindow)
        self.actionVerDatos.setObjectName("actionVerDatos")
        self.actionVerResumen = QtWidgets.QAction(MainWindow)
        self.actionVerResumen.setObjectName("actionVerResumen")
        self.actionVerPrecision = QtWidgets.QAction(MainWindow)
        self.actionVerPrecision.setObjectName("actionVerPrecision")
        self.actionGraficos = QtWidgets.QAction(MainWindow)
        self.actionGraficos.setObjectName("actionGr_ficos")
        self.actionInsertarDato = QtWidgets.QAction(MainWindow)
        self.actionInsertarDato.setObjectName("actionInsertarDato")
        self.actionPredecirDato = QtWidgets.QAction(MainWindow)
        self.actionPredecirDato.setObjectName("actionPredecirDato")
        self.actionActualizarUltimaFila = QtWidgets.QAction(MainWindow)
        self.actionActualizarUltimaFila.setObjectName("actionActualizarUltimaFila")
        self.actionActualizarPorID = QtWidgets.QAction(MainWindow)
        self.actionActualizarPorID.setObjectName("actionActualizarPorID")
        self.actionEliminarUltimaFila = QtWidgets.QAction(MainWindow)
        self.actionEliminarUltimaFila.setObjectName("actionEliminarUltimaFila")
        self.actionEliminarPorID = QtWidgets.QAction(MainWindow)
        self.actionEliminarPorID.setObjectName("actionEliminarPorID")
        self.menuVer.addAction(self.actionVerDatos)
        self.menuVer.addAction(self.actionVerResumen)
        self.menuVer.addAction(self.actionVerPrecision)
        self.menuInsertar.addAction(self.actionInsertarDato)
        self.menuInsertar.addAction(self.actionPredecirDato)
        self.menuActualizar.addAction(self.actionActualizarUltimaFila)
        self.menuActualizar.addAction(self.actionActualizarPorID)
        self.menuEliminar.addAction(self.actionEliminarUltimaFila)
        self.menuEliminar.addAction(self.actionEliminarPorID)
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.menuInsertar.menuAction())
        self.menubar.addAction(self.menuActualizar.menuAction())
        self.menubar.addAction(self.menuEliminar.menuAction())

        self.actionVerDatos.triggered.connect(self.verDatos)
        self.actionVerResumen.triggered.connect(self.verResumen)
        self.actionVerPrecision.triggered.connect(self.verPrecision)
        self.actionInsertarDato.triggered.connect(self.verInsertar)
        self.actionPredecirDato.triggered.connect(self.verPredecir)
        self.actionActualizarUltimaFila.triggered.connect(self.verActualizarUltimo)
        self.actionActualizarPorID.triggered.connect(self.verActualizarPorID)
        self.actionEliminarUltimaFila.triggered.connect(self.verEliminar)
        self.actionEliminarPorID.triggered.connect(self.verEliminar)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def verDatos(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_DialogDatos()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def verResumen(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_DialogResumen()
        self.ui.setupUi(self.dialog)
        self.dialog.show()
    
    def verPrecision(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_DialogPrecision()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def verInsertar(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_DialogInsertar()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def verPredecir(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_DialogPredecir()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def verActualizarUltimo(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_DialogActualizarUltimo()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def verActualizarPorID(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_DialogActualizarPorID()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def verEliminar(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_DialogEliminar()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Víctor Luque - PyQT5 - Home"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Esta aplicación permite interactuar y visualizar información contenida en Iris Dataset.\n"
"\n"
"Desde el menú de navegacion es posible acceder a las diferentes páginas de la aplicación.\n"
"\n"
"Las páginas son:\n"
"\n"
"- Show:\n"
"  * Mostrar todos los datos\n"
"  * Mostrar el resumen\n"
"  * Mostrar la precisión\n"
"  * Mostrar un gráfico de puntos de la información de las longitudes\n"
"  * Mostrar un gráfico de puntos de la información de las anchuras\n"
"\n"
"- Insert:\n"
"  * Insertar nuevos datos al Iris dataset\n"
"  * Insertar datos y predecir el resultado\n"
"\n"
"- Update:\n"
"  * Actualizar la última fila de Iris Dataset\n"
"  * Actualizar una fila especificando un ID\n"
"\n"
"- Delete:\n"
"  * Elimar el último registro de Iris Dataset\n"
"  * Eliminar un registro especificando un ID"))
        self.menuVer.setTitle(_translate("MainWindow", "Ver"))
        self.menuInsertar.setTitle(_translate("MainWindow", "Insertar"))
        self.menuActualizar.setTitle(_translate("MainWindow", "Actualizar"))
        self.menuEliminar.setTitle(_translate("MainWindow", "Eliminar"))
        self.actionVerDatos.setText(_translate("MainWindow", "Datos"))
        self.actionVerResumen.setText(_translate("MainWindow", "Resumen"))
        self.actionVerPrecision.setText(_translate("MainWindow", "Precision"))
        self.actionGraficos.setText(_translate("MainWindow", "Gráficos"))
        self.actionInsertarDato.setText(_translate("MainWindow", "Insertar Dato"))
        self.actionPredecirDato.setText(_translate("MainWindow", "Predecir Dato"))
        self.actionActualizarUltimaFila.setText(_translate("MainWindow", "Ultima fila"))
        self.actionActualizarPorID.setText(_translate("MainWindow", "Por ID"))
        self.actionEliminarUltimaFila.setText(_translate("MainWindow", "Ultima fila"))
        self.actionEliminarPorID.setText(_translate("MainWindow", "Por ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())