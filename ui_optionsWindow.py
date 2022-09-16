# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/options.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)));
	return os.path.join(base_path, relative_path);


class Ui_optionsWindow(object):
    def setupUi(self, optionsWindow):
        optionsWindow.setObjectName("optionsWindow")
        optionsWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        optionsWindow.resize(191, 120)
        optionsWindow.setMinimumSize(QtCore.QSize(191, 120))
        optionsWindow.setMaximumSize(QtCore.QSize(191, 120))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("icons/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        optionsWindow.setWindowIcon(icon)
        optionsWindow.setStyleSheet("background: rgb(54, 57, 63);\n"
"color: rgb(255, 255, 255);")
        optionsWindow.setModal(True)
        self.acceptCancel = QtWidgets.QDialogButtonBox(optionsWindow)
        self.acceptCancel.setGeometry(QtCore.QRect(20, 80, 151, 32))
        self.acceptCancel.setStyleSheet("QPushButton {\n"
"    background: rgb(64, 68, 75);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(79, 83, 89);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: rgb(54, 57, 63);\n"
"    color: rgb(126, 126, 126);\n"
"}")
        self.acceptCancel.setOrientation(QtCore.Qt.Horizontal)
        self.acceptCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.acceptCancel.setObjectName("acceptCancel")
        self.layoutWidget = QtWidgets.QWidget(optionsWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 171, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.themeLabel = QtWidgets.QLabel(self.layoutWidget)
        self.themeLabel.setStyleSheet("QLabel {\n"
"    background: transparent;\n"
"    font: font \"Fira Code\";\n"
"}")
        self.themeLabel.setObjectName("themeLabel")
        self.horizontalLayout_2.addWidget(self.themeLabel)
        self.themeBox = QtWidgets.QComboBox(self.layoutWidget)
        self.themeBox.setMinimumSize(QtCore.QSize(71, 21))
        self.themeBox.setMaximumSize(QtCore.QSize(71, 21))
        self.themeBox.setStyleSheet("QComboBox {\n"
"    background: rgb(64, 68, 75);\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"    border-radius:5px;\n"
"    padding-left: 3px;\n"
"}")
        self.themeBox.setObjectName("themeBox")
        self.themeBox.addItem("")
        self.themeBox.addItem("")
        self.horizontalLayout_2.addWidget(self.themeBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.langLabel = QtWidgets.QLabel(self.layoutWidget)
        self.langLabel.setStyleSheet("QLabel {\n"
"    background: transparent;\n"
"    font: font \"Fira Code\";\n"
"}")
        self.langLabel.setObjectName("langLabel")
        self.horizontalLayout.addWidget(self.langLabel)
        self.langBox = QtWidgets.QComboBox(self.layoutWidget)
        self.langBox.setMinimumSize(QtCore.QSize(71, 21))
        self.langBox.setMaximumSize(QtCore.QSize(71, 21))
        self.langBox.setStyleSheet("QComboBox {\n"
"    background: rgb(64, 68, 75);\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"    border-radius:5px;\n"
"    padding-left: 3px;\n"
"}")
        self.langBox.setObjectName("langBox")
        self.langBox.addItem("")
        self.langBox.addItem("")
        self.langBox.addItem("")
        self.horizontalLayout.addWidget(self.langBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.themeLabel.setBuddy(self.themeBox)
        self.langLabel.setBuddy(self.themeBox)

        self.retranslateUi(optionsWindow)
        self.acceptCancel.rejected.connect(optionsWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(optionsWindow)

    def retranslateUi(self, optionsWindow):
        _translate = QtCore.QCoreApplication.translate
        optionsWindow.setWindowTitle(_translate("optionsWindow", "Options"))
        self.themeLabel.setText(_translate("optionsWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Theme:</span></p></body></html>"))
        self.themeBox.setItemText(0, _translate("optionsWindow", "Dark"))
        self.themeBox.setItemText(1, _translate("optionsWindow", "Light"))
        self.langLabel.setText(_translate("optionsWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Language:</span></p></body></html>"))
        self.langBox.setItemText(0, _translate("optionsWindow", "English"))
        self.langBox.setItemText(1, _translate("optionsWindow", "German"))
        self.langBox.setItemText(2, _translate("optionsWindow", "French"))
