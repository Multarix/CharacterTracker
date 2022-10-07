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
        self.layoutWidget = QtWidgets.QWidget(creditsWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 209, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.programName = QtWidgets.QLabel(self.layoutWidget)
        self.programName.setObjectName("programName")
        self.verticalLayout.addWidget(self.programName)
        self.copyright = QtWidgets.QLabel(self.layoutWidget)
        self.copyright.setObjectName("copyright")
        self.verticalLayout.addWidget(self.copyright)
        self.link = QtWidgets.QLabel(self.layoutWidget)
        self.link.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.link.setObjectName("link")
        self.verticalLayout.addWidget(self.link)
        self.pushButton = QtWidgets.QPushButton(creditsWindow)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(90, 80, 70, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.programName.setBuddy(self.pushButton)

        self.retranslateUi(creditsWindow)
        self.pushButton.clicked.connect(creditsWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(creditsWindow)

    def retranslateUi(self, creditsWindow):
        _translate = QtCore.QCoreApplication.translate
        self.programName.setText(_translate("creditsWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Character Tracker</span></p></body></html>"))
        self.copyright.setText(_translate("creditsWindow", "<html><head/><body><p align=\"center\">© 2022 Multarix</p></body></html>"))
        self.link.setText(_translate("creditsWindow", "<html><head/><body><p align=\"center\"><a href=\"https://github.com/Multarix\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/Multarix</span></a></p></body></html>"))
        self.pushButton.setText(_translate("creditsWindow", "Ok"))
