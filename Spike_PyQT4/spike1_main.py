import sys
#from qtpy import QtCore, QtGui, uic
from qtpy import QtGui, uic
from qtpy import QtWidgets
from Ui_MainWindow2 import Ui_MainWindow2

qtCreatorFile = "mainwindow.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow2):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow2.__init__(self)
        self.setupUi(self)
        #self.setupUi(Ui_MainWindow2)
        #self.pushButton.onclick(self.doMultiply)
        self.pushButton.clicked.connect(self.doMultiply)
 
    def doMultiply(self):
        print("Got here")
        print(self.inputField1.toPlainText())
        v1 = int(self.inputField1.toPlainText())
        print (self.spinBox_SeedValue.value())
        v2 = int(self.spinBox_SeedValue.value())
        self.textEdit.setText(str(v1*v2))
        
if __name__ == "__main__":
    #app = QtGui.QGuiApplication(sys.argv)
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    
