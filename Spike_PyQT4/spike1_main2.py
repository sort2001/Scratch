import sys
#from qtpy import QtCore, QtGui, uic
from qtpy import QtGui, uic
from qtpy import QtWidgets
from Ui_MainWindow2 import Ui_MainWindow2

qtCreatorFile = "mainwindow.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow2):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow2.__init__(self)
        #self.setupUi(self)
        self.setupUi(Ui_MainWindow2)
        self.pushButton.onclick(self.doMultiply)
 
    def doMultiply(self):
        v1 = int(self.inputField1.toPlainText())
        v2 = int(self.spinBox_SeedValue.value())
        self.textEdit.setText(v1*v2)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    MyApp(MainWindow, ui)
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
