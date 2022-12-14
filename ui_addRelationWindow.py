# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/addRelation.ui'
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


class Ui_addRelationWindow(object):
    def setupUi(self, addRelationWindow):
        addRelationWindow.setObjectName("addRelationWindow")
        addRelationWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        addRelationWindow.resize(401, 201)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addRelationWindow.sizePolicy().hasHeightForWidth())
        addRelationWindow.setSizePolicy(sizePolicy)
        addRelationWindow.setMinimumSize(QtCore.QSize(401, 201))
        addRelationWindow.setMaximumSize(QtCore.QSize(401, 201))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("icons/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        addRelationWindow.setWindowIcon(icon)
        addRelationWindow.setToolTip("")
        self.characterList = QtWidgets.QListWidget(addRelationWindow)
        self.characterList.setGeometry(QtCore.QRect(10, 70, 221, 121))
        self.characterList.setIconSize(QtCore.QSize(11, 11))
        self.characterList.setUniformItemSizes(True)
        self.characterList.setObjectName("characterList")
        self.accept = QtWidgets.QPushButton(addRelationWindow)
        self.accept.setEnabled(False)
        self.accept.setGeometry(QtCore.QRect(240, 170, 71, 23))
        self.accept.setObjectName("accept")
        self.label = QtWidgets.QLabel(addRelationWindow)
        self.label.setGeometry(QtCore.QRect(10, 5, 181, 31))
        self.label.setObjectName("label")
        self.relationType = QtWidgets.QListWidget(addRelationWindow)
        self.relationType.setGeometry(QtCore.QRect(240, 70, 151, 91))
        self.relationType.setUniformItemSizes(True)
        self.relationType.setObjectName("relationType")
        item = QtWidgets.QListWidgetItem()
        self.relationType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.relationType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.relationType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.relationType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.relationType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.relationType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.relationType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.relationType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.relationType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.relationType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.relationType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.relationType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.relationType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.relationType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.relationType.addItem(item)
        self.cancel = QtWidgets.QPushButton(addRelationWindow)
        self.cancel.setGeometry(QtCore.QRect(320, 170, 71, 23))
        self.cancel.setObjectName("cancel")
        self.search = QtWidgets.QLineEdit(addRelationWindow)
        self.search.setGeometry(QtCore.QRect(10, 40, 221, 21))
        self.search.setAcceptDrops(False)
        self.search.setToolTip("")
        self.search.setText("")
        self.search.setObjectName("search")
        self.searchRelation = QtWidgets.QLineEdit(addRelationWindow)
        self.searchRelation.setGeometry(QtCore.QRect(240, 40, 151, 21))
        self.searchRelation.setAcceptDrops(False)
        self.searchRelation.setToolTip("")
        self.searchRelation.setText("")
        self.searchRelation.setObjectName("searchRelation")
        self.label.setBuddy(self.characterList)

        self.retranslateUi(addRelationWindow)
        self.cancel.clicked.connect(addRelationWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(addRelationWindow)
        addRelationWindow.setTabOrder(self.characterList, self.relationType)
        addRelationWindow.setTabOrder(self.relationType, self.accept)
        addRelationWindow.setTabOrder(self.accept, self.cancel)

    def retranslateUi(self, addRelationWindow):
        _translate = QtCore.QCoreApplication.translate
        addRelationWindow.setWindowTitle(_translate("addRelationWindow", "Add Relation"))
        self.accept.setText(_translate("addRelationWindow", "Accept"))
        self.label.setText(_translate("addRelationWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Add Relation</span></p><p><br/></p></body></html>"))
        __sortingEnabled = self.relationType.isSortingEnabled()
        self.relationType.setSortingEnabled(False)
        item = self.relationType.item(0)
        item.setText(_translate("addRelationWindow", "Father"))
        item = self.relationType.item(1)
        item.setText(_translate("addRelationWindow", "Mother"))
        item = self.relationType.item(2)
        item.setText(_translate("addRelationWindow", "Son"))
        item = self.relationType.item(3)
        item.setText(_translate("addRelationWindow", "Daughter"))
        item = self.relationType.item(4)
        item.setText(_translate("addRelationWindow", "Brother"))
        item = self.relationType.item(5)
        item.setText(_translate("addRelationWindow", "Sister"))
        item = self.relationType.item(6)
        item.setText(_translate("addRelationWindow", "Uncle"))
        item = self.relationType.item(7)
        item.setText(_translate("addRelationWindow", "Aunt"))
        item = self.relationType.item(8)
        item.setText(_translate("addRelationWindow", "Nephew"))
        item = self.relationType.item(9)
        item.setText(_translate("addRelationWindow", "Niece"))
        item = self.relationType.item(10)
        item.setText(_translate("addRelationWindow", "Boyfriend"))
        item = self.relationType.item(11)
        item.setText(_translate("addRelationWindow", "Girlfriend"))
        item = self.relationType.item(12)
        item.setText(_translate("addRelationWindow", "Fianc??"))
        item = self.relationType.item(13)
        item.setText(_translate("addRelationWindow", "Husband"))
        item = self.relationType.item(14)
        item.setText(_translate("addRelationWindow", "Wife"))
        self.relationType.setSortingEnabled(__sortingEnabled)
        self.cancel.setText(_translate("addRelationWindow", "Cancel"))
        self.search.setWhatsThis(_translate("addRelationWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.search.setPlaceholderText(_translate("addRelationWindow", "Search Characters"))
        self.searchRelation.setWhatsThis(_translate("addRelationWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.searchRelation.setPlaceholderText(_translate("addRelationWindow", "Search Relations"))
