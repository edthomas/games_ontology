# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Wed May  8 10:43:34 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from controller import *

import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GamesOntology(QtGui.QMainWindow):
    def __init__(self, control):
        print 'fudeu'
        QtGui.QMainWindow.__init__(self)
        #self.ui = Ui_GamesOntology()
        self.control = control
        self.setupUi(self)
        self.show()
    
    def setupUi(self, GamesOntology):
        GamesOntology.setObjectName(_fromUtf8("GamesOntology"))
        GamesOntology.resize(450, 500)
        self.centralwidget = QtGui.QWidget(GamesOntology)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 231, 33))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 50, 96, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 100, 431, 381))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 50, 76, 29))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        GamesOntology.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(GamesOntology)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        GamesOntology.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GamesOntology)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GamesOntology.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAbout.menuAction())
        
        self.pushButton.clicked.connect(self.control.get_pergunta)
        for i in range(1, 12):
            self.comboBox.addItem(str(i))
    
        self.retranslateUi(GamesOntology)
        QtCore.QMetaObject.connectSlotsByName(GamesOntology)
        

    def retranslateUi(self, GamesOntology):
        GamesOntology.setWindowTitle(_translate("GamesOntology", "MainWindow", None))
        self.pushButton.setText(_translate("GamesOntology", "OK", None))
        self.menuAbout.setTitle(_translate("GamesOntology", "About", None))


#~ if __name__ == '__main__':
    #~ app = QtGui.QApplication(sys.argv)
    #~ window = Ui_GamesOntology()
    #~ window.show()
    #~ sys.exit(app.exec_())



