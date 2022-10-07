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
        optionsWindow.resize(341, 276)
        optionsWindow.setMinimumSize(QtCore.QSize(341, 276))
        optionsWindow.setMaximumSize(QtCore.QSize(341, 276))
        self.layoutWidget = QtWidgets.QWidget(optionsWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 301, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.themeLayout = QtWidgets.QHBoxLayout()
        self.themeLayout.setObjectName("themeLayout")
        self.themeLabel = QtWidgets.QLabel(self.layoutWidget)
        self.themeLabel.setObjectName("themeLabel")
        self.themeLayout.addWidget(self.themeLabel)
        self.themeBox = QtWidgets.QComboBox(self.layoutWidget)
        self.themeBox.setMinimumSize(QtCore.QSize(100, 25))
        self.themeBox.setMaximumSize(QtCore.QSize(100, 25))
        self.themeBox.setObjectName("themeBox")
        self.themeBox.addItem("")
        self.themeBox.addItem("")
        self.themeLayout.addWidget(self.themeBox)
        self.verticalLayout.addLayout(self.themeLayout)
        self.langLayout = QtWidgets.QHBoxLayout()
        self.langLayout.setObjectName("langLayout")
        self.langLabel = QtWidgets.QLabel(self.layoutWidget)
        self.langLabel.setObjectName("langLabel")
        self.langLayout.addWidget(self.langLabel)
        self.langBox = QtWidgets.QComboBox(self.layoutWidget)
        self.langBox.setMinimumSize(QtCore.QSize(100, 25))
        self.langBox.setMaximumSize(QtCore.QSize(100, 25))
        self.langBox.setObjectName("langBox")
        self.langBox.addItem("")
        self.langBox.addItem("")
        self.langBox.addItem("")
        self.langLayout.addWidget(self.langBox)
        self.verticalLayout.addLayout(self.langLayout)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.timelineLengthLayout = QtWidgets.QHBoxLayout()
        self.timelineLengthLayout.setObjectName("timelineLengthLayout")
        self.timelineLength = QtWidgets.QLabel(self.layoutWidget)
        self.timelineLength.setObjectName("timelineLength")
        self.timelineLengthLayout.addWidget(self.timelineLength)
        self.timelineLength_spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.timelineLength_spin.setMinimumSize(QtCore.QSize(100, 25))
        self.timelineLength_spin.setMaximumSize(QtCore.QSize(100, 25))
        self.timelineLength_spin.setMinimum(1)
        self.timelineLength_spin.setMaximum(1000)
        self.timelineLength_spin.setProperty("value", 10)
        self.timelineLength_spin.setObjectName("timelineLength_spin")
        self.timelineLengthLayout.addWidget(self.timelineLength_spin)
        self.verticalLayout.addLayout(self.timelineLengthLayout)
        self.monthPerYearLayout = QtWidgets.QHBoxLayout()
        self.monthPerYearLayout.setObjectName("monthPerYearLayout")
        self.monthPerYear = QtWidgets.QLabel(self.layoutWidget)
        self.monthPerYear.setObjectName("monthPerYear")
        self.monthPerYearLayout.addWidget(self.monthPerYear)
        self.monthPerYear_spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.monthPerYear_spin.setMinimumSize(QtCore.QSize(100, 25))
        self.monthPerYear_spin.setMaximumSize(QtCore.QSize(100, 25))
        self.monthPerYear_spin.setMinimum(1)
        self.monthPerYear_spin.setMaximum(100)
        self.monthPerYear_spin.setProperty("value", 12)
        self.monthPerYear_spin.setObjectName("monthPerYear_spin")
        self.monthPerYearLayout.addWidget(self.monthPerYear_spin)
        self.verticalLayout.addLayout(self.monthPerYearLayout)
        self.startYearLayout = QtWidgets.QHBoxLayout()
        self.startYearLayout.setObjectName("startYearLayout")
        self.startYear = QtWidgets.QLabel(self.layoutWidget)
        self.startYear.setObjectName("startYear")
        self.startYearLayout.addWidget(self.startYear)
        self.startYear_spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.startYear_spin.setMinimumSize(QtCore.QSize(100, 25))
        self.startYear_spin.setMaximumSize(QtCore.QSize(100, 25))
        self.startYear_spin.setMinimum(1)
        self.startYear_spin.setMaximum(10000)
        self.startYear_spin.setProperty("value", 2022)
        self.startYear_spin.setObjectName("startYear_spin")
        self.startYearLayout.addWidget(self.startYear_spin)
        self.verticalLayout.addLayout(self.startYearLayout)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(optionsWindow)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(100, 230, 151, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.acceptCancelLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.acceptCancelLayout.setContentsMargins(0, 0, 0, 0)
        self.acceptCancelLayout.setObjectName("acceptCancelLayout")
        self.accept = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.accept.setMinimumSize(QtCore.QSize(71, 23))
        self.accept.setMaximumSize(QtCore.QSize(71, 23))
        self.accept.setObjectName("accept")
        self.acceptCancelLayout.addWidget(self.accept)
        self.cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.cancel.setMinimumSize(QtCore.QSize(71, 23))
        self.cancel.setMaximumSize(QtCore.QSize(71, 23))
        self.cancel.setObjectName("cancel")
        self.acceptCancelLayout.addWidget(self.cancel)
        self.themeLabel.setBuddy(self.themeBox)
        self.langLabel.setBuddy(self.langBox)
        self.timelineLength.setBuddy(self.timelineLength_spin)
        self.monthPerYear.setBuddy(self.monthPerYear_spin)
        self.startYear.setBuddy(self.startYear_spin)

        self.retranslateUi(optionsWindow)
        self.cancel.clicked.connect(optionsWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(optionsWindow)
        optionsWindow.setTabOrder(self.themeBox, self.langBox)
        optionsWindow.setTabOrder(self.langBox, self.timelineLength_spin)
        optionsWindow.setTabOrder(self.timelineLength_spin, self.monthPerYear_spin)
        optionsWindow.setTabOrder(self.monthPerYear_spin, self.startYear_spin)
        optionsWindow.setTabOrder(self.startYear_spin, self.accept)

    def retranslateUi(self, optionsWindow):
        _translate = QtCore.QCoreApplication.translate
        optionsWindow.setWindowTitle(_translate("optionsWindow", "Options"))
        self.themeLabel.setText(_translate("optionsWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Theme</span></p></body></html>"))
        self.themeBox.setItemText(0, _translate("optionsWindow", "Dark"))
        self.themeBox.setItemText(1, _translate("optionsWindow", "Light"))
        self.langLabel.setText(_translate("optionsWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Language</span></p></body></html>"))
        self.langBox.setItemText(0, _translate("optionsWindow", "English"))
        self.langBox.setItemText(1, _translate("optionsWindow", "German"))
        self.langBox.setItemText(2, _translate("optionsWindow", "French"))
        self.timelineLength.setText(_translate("optionsWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Timeline Length</span></p></body></html>"))
        self.timelineLength_spin.setSuffix(_translate("optionsWindow", " year(s)"))
        self.monthPerYear.setText(_translate("optionsWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Months per Year</span></p></body></html>"))
        self.monthPerYear_spin.setSuffix(_translate("optionsWindow", " month(s)"))
        self.startYear.setText(_translate("optionsWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Start Year</span></p></body></html>"))
        self.accept.setText(_translate("optionsWindow", "Accept"))
        self.cancel.setText(_translate("optionsWindow", "Cancel"))
