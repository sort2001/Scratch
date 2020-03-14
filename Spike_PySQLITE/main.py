import sys
#from qtpy import QtCore, QtGui, uic
from PyQt5 import QtWidgets, uic

qtCreatorFile = "TimeCardMain.ui" # Enter file here.
 
UiMainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, UiMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UiMainWindow.__init__(self)
        #self.setupUi(self)
        self.setupUi(self)
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())