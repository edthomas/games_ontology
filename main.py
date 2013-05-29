# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Wed May 29 14:12:10 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_GamesOntology(object):
    def setupUi(self, GamesOntology):
        GamesOntology.setObjectName(_fromUtf8("GamesOntology"))
        GamesOntology.resize(399, 368)
        self.centralwidget = QtGui.QWidget(GamesOntology)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 129, 33))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 50, 85, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 100, 351, 192))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 76, 29))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 31))
        self.label.setObjectName(_fromUtf8("label"))
        GamesOntology.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(GamesOntology)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 399, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        GamesOntology.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GamesOntology)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GamesOntology.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(GamesOntology)
        QtCore.QMetaObject.connectSlotsByName(GamesOntology)

    def retranslateUi(self, GamesOntology):
        GamesOntology.setWindowTitle(_translate("GamesOntology", "MainWindow", None))
        self.pushButton.setText(_translate("GamesOntology", "OK", None))
        self.label.setText(_translate("GamesOntology", "TextLabel", None))
        self.menuAbout.setTitle(_translate("GamesOntology", "About", None))

