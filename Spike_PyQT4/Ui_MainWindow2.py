from qtpy import QtWidgets, QtCore, QtGui

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        #MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(400, 300)
        
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.centralWidget.setFixedSize(400,300)
        self.inputField1 = QtWidgets.QTextEdit(self.centralWidget)
        self.inputField1.setGeometry(QtCore.QRect(160, 50, 104, 21))
        self.inputField1.setObjectName("inputField1")
        self.label1 = QtWidgets.QLabel(self.centralWidget)
        self.label1.setGeometry(QtCore.QRect(50, 50, 101, 16))
        self.label1.setObjectName("label1")
        self.spinBox_SeedValue = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_SeedValue.setGeometry(QtCore.QRect(160, 90, 47, 23))
        self.spinBox_SeedValue.setObjectName("spinBox_SeedValue")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(70, 90, 81, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 120, 80, 22))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 150, 104, 31))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 19))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "Enter a value"))
        self.label.setText(_translate("MainWindow", "Offset Value"))
        self.pushButton.setText(_translate("MainWindow", "Multiply"))



