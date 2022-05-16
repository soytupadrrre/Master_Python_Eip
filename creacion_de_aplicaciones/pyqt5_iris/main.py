from app import Ui_MainWindow as Home
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Home()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())