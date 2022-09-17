# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/info.ui'
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


class Ui_creditsWindow(object):
    def setupUi(self, creditsWindow):
        creditsWindow.setObjectName("creditsWindow")
        creditsWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        creditsWindow.resize(251, 113)
        creditsWindow.setMinimumSize(QtCore.QSize(251, 113))
        creditsWindow.setMaximumSize(QtCore.QSize(251, 113))
        creditsWindow.setWindowTitle("")
        creditsWindow.setStyleSheet("background: rgb(54, 57, 63);\n"
"color: rgb(255, 255, 255);")
        self.layoutWidget = QtWidgets.QWidget(creditsWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 6, 209, 69))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("QLabel {\n"
"    background: transparent;\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("QLabel {\n"
"    background: transparent;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("QLabel {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QLabel:link {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_3.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(creditsWindow)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(90, 80, 70, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.label.setBuddy(self.pushButton)

        self.retranslateUi(creditsWindow)
        self.pushButton.clicked.connect(creditsWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(creditsWindow)

    def retranslateUi(self, creditsWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("creditsWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Character Tracker</span></p></body></html>"))
        self.label_2.setText(_translate("creditsWindow", "<html><head/><body><p align=\"center\">© 2022 Multarix. All Rights Reserved</p></body></html>"))
        self.label_3.setText(_translate("creditsWindow", "<html><head/><body><p align=\"center\">https://github.com/Multarix</p></body></html>"))
        self.pushButton.setText(_translate("creditsWindow", "I see..."))
