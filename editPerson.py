# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/editPerson.ui'
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


class Ui_editPersonUI(object):
    def setupUi(self, editPersonUI):
        editPersonUI.setObjectName("editPersonUI")
        editPersonUI.resize(432, 391)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(editPersonUI.sizePolicy().hasHeightForWidth())
        editPersonUI.setSizePolicy(sizePolicy)
        editPersonUI.setMinimumSize(QtCore.QSize(432, 391))
        editPersonUI.setMaximumSize(QtCore.QSize(432, 391))
        editPersonUI.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("icons/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        editPersonUI.setWindowIcon(icon)
        editPersonUI.setStyleSheet("background: rgb(54, 57, 63);\n"
"color: rgb(255, 255, 255)")
        self.acceptForm = QtWidgets.QPushButton(editPersonUI)
        self.acceptForm.setEnabled(False)
        self.acceptForm.setGeometry(QtCore.QRect(360, 360, 61, 23))
        self.acceptForm.setStyleSheet("QPushButton {\n"
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
        self.acceptForm.setDefault(False)
        self.acceptForm.setObjectName("acceptForm")
        self.textEdit = QtWidgets.QTextEdit(editPersonUI)
        self.textEdit.setGeometry(QtCore.QRect(10, 130, 191, 251))
        self.textEdit.setAcceptDrops(False)
        self.textEdit.setStyleSheet("QTextEdit {\n"
"    background: rgb(64, 68, 75);\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"    border-radius:5px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"}")
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        self.charInfoLabel = QtWidgets.QLabel(editPersonUI)
        self.charInfoLabel.setGeometry(QtCore.QRect(13, 110, 191, 16))
        self.charInfoLabel.setStyleSheet("QLabel {\n"
"    background: transparent;\n"
"}")
        self.charInfoLabel.setObjectName("charInfoLabel")
        self.titleLabel = QtWidgets.QLabel(editPersonUI)
        self.titleLabel.setGeometry(QtCore.QRect(13, 10, 47, 13))
        self.titleLabel.setStyleSheet("QLabel {\n"
"    background: transparent;\n"
"}")
        self.titleLabel.setObjectName("titleLabel")
        self.titleSelector = QtWidgets.QComboBox(editPersonUI)
        self.titleSelector.setGeometry(QtCore.QRect(10, 30, 71, 21))
        self.titleSelector.setStyleSheet("background: rgb(64, 68, 75);\n"
"border: 1px solid rgb(50, 50, 50);\n"
"border-radius:5px;")
        self.titleSelector.setObjectName("titleSelector")
        self.titleSelector.addItem("")
        self.titleSelector.addItem("")
        self.titleSelector.addItem("")
        self.titleSelector.addItem("")
        self.titleSelector.addItem("")
        self.titleSelector.addItem("")
        self.titleSelector.addItem("")
        self.titleSelector.addItem("")
        self.titleSelector.addItem("")
        self.titleSelector.addItem("")
        self.titleSelector.addItem("")
        self.titleSelector.addItem("")
        self.age = QtWidgets.QSpinBox(editPersonUI)
        self.age.setGeometry(QtCore.QRect(250, 80, 61, 22))
        self.age.setStyleSheet("QSpinBox {\n"
"    background: rgb(64, 68, 75);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"    border-radius:5px;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"QSpinBox:disabled {\n"
"    background: rgb(54, 57, 63);\n"
"    color: rgb(126, 126, 126);\n"
"}")
        self.age.setMaximum(9999999)
        self.age.setObjectName("age")
        self.addRelation = QtWidgets.QPushButton(editPersonUI)
        self.addRelation.setGeometry(QtCore.QRect(210, 330, 61, 23))
        self.addRelation.setStyleSheet("QPushButton {\n"
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
        self.addRelation.setObjectName("addRelation")
        self.fullNameLabel = QtWidgets.QLabel(editPersonUI)
        self.fullNameLabel.setGeometry(QtCore.QRect(103, 10, 171, 16))
        self.fullNameLabel.setStyleSheet("QLabel {\n"
"    background: transparent;\n"
"}")
        self.fullNameLabel.setObjectName("fullNameLabel")
        self.speciesLabel = QtWidgets.QLabel(editPersonUI)
        self.speciesLabel.setGeometry(QtCore.QRect(13, 60, 47, 13))
        self.speciesLabel.setStyleSheet("QLabel {\n"
"    background: transparent;\n"
"}")
        self.speciesLabel.setObjectName("speciesLabel")
        self.removeRelation = QtWidgets.QPushButton(editPersonUI)
        self.removeRelation.setEnabled(False)
        self.removeRelation.setGeometry(QtCore.QRect(360, 330, 61, 23))
        self.removeRelation.setStyleSheet("QPushButton {\n"
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
        self.removeRelation.setObjectName("removeRelation")
        self.dead = QtWidgets.QCheckBox(editPersonUI)
        self.dead.setGeometry(QtCore.QRect(330, 80, 70, 20))
        self.dead.setStyleSheet("QCheckBox{\n"
"    color: white;\n"
"    background: transparent;\n"
"}")
        self.dead.setObjectName("dead")
        self.species = QtWidgets.QLineEdit(editPersonUI)
        self.species.setGeometry(QtCore.QRect(10, 80, 131, 21))
        self.species.setAcceptDrops(False)
        self.species.setToolTip("")
        self.species.setStyleSheet("QLineEdit{\n"
"    background: rgb(64, 68, 75);\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"    border-radius:5px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"}")
        self.species.setText("")
        self.species.setObjectName("species")
        self.genderLabel = QtWidgets.QLabel(editPersonUI)
        self.genderLabel.setGeometry(QtCore.QRect(163, 60, 47, 13))
        self.genderLabel.setStyleSheet("QLabel {\n"
"    background: transparent;\n"
"}")
        self.genderLabel.setObjectName("genderLabel")
        self.name = QtWidgets.QLineEdit(editPersonUI)
        self.name.setGeometry(QtCore.QRect(100, 30, 161, 21))
        self.name.setAcceptDrops(False)
        self.name.setToolTip("")
        self.name.setStyleSheet("QLineEdit{\n"
"    background: rgb(64, 68, 75);\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"    border-radius:5px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"}")
        self.name.setText("")
        self.name.setObjectName("name")
        self.genderSelector = QtWidgets.QComboBox(editPersonUI)
        self.genderSelector.setGeometry(QtCore.QRect(160, 80, 71, 21))
        self.genderSelector.setStyleSheet("background: rgb(64, 68, 75);\n"
"border: 1px solid rgb(50, 50, 50);\n"
"border-radius:5px;")
        self.genderSelector.setObjectName("genderSelector")
        self.genderSelector.addItem("")
        self.genderSelector.addItem("")
        self.genderSelector.addItem("")
        self.ageLabel = QtWidgets.QLabel(editPersonUI)
        self.ageLabel.setGeometry(QtCore.QRect(253, 60, 47, 13))
        self.ageLabel.setStyleSheet("QLabel {\n"
"    background: transparent;\n"
"}")
        self.ageLabel.setObjectName("ageLabel")
        self.relationLabel = QtWidgets.QLabel(editPersonUI)
        self.relationLabel.setGeometry(QtCore.QRect(213, 110, 71, 16))
        self.relationLabel.setStyleSheet("QLabel {\n"
"    background: transparent;\n"
"}")
        self.relationLabel.setObjectName("relationLabel")
        self.relationTable = QtWidgets.QListWidget(editPersonUI)
        self.relationTable.setGeometry(QtCore.QRect(210, 130, 211, 191))
        self.relationTable.setMinimumSize(QtCore.QSize(0, 0))
        self.relationTable.setMaximumSize(QtCore.QSize(101010, 101010))
        self.relationTable.setStyleSheet("QListWidget{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgb(64, 68, 75);\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"    border-radius:5px;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QListWidget:item{\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    border: 1px solid transparent;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QListWidget:item:hover{\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    background: rgb(74, 76, 79);\n"
"    border: 1px solid rgb(64, 66, 75);\n"
"}\n"
"\n"
"QListWidget:item:selected{\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    background: rgb(93, 94, 97);\n"
"    border: 1px solid rgb(74, 76, 79);\n"
"}")
        self.relationTable.setObjectName("relationTable")
        self.characterID = QtWidgets.QSpinBox(editPersonUI)
        self.characterID.setEnabled(False)
        self.characterID.setGeometry(QtCore.QRect(351, 30, 61, 22))
        self.characterID.setToolTip("")
        self.characterID.setStyleSheet("QSpinBox {\n"
"    background: rgb(64, 68, 75);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"    border-radius:5px;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"QSpinBox:disabled {\n"
"    background: rgb(54, 57, 63);\n"
"    color: rgb(126, 126, 126);\n"
"}")
        self.characterID.setFrame(True)
        self.characterID.setReadOnly(True)
        self.characterID.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.characterID.setKeyboardTracking(False)
        self.characterID.setObjectName("characterID")
        self.editRelation = QtWidgets.QPushButton(editPersonUI)
        self.editRelation.setEnabled(False)
        self.editRelation.setGeometry(QtCore.QRect(285, 330, 61, 23))
        self.editRelation.setStyleSheet("QPushButton {\n"
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
        self.editRelation.setObjectName("editRelation")
        self.characterID.raise_()
        self.acceptForm.raise_()
        self.textEdit.raise_()
        self.charInfoLabel.raise_()
        self.titleLabel.raise_()
        self.titleSelector.raise_()
        self.age.raise_()
        self.addRelation.raise_()
        self.fullNameLabel.raise_()
        self.speciesLabel.raise_()
        self.removeRelation.raise_()
        self.dead.raise_()
        self.species.raise_()
        self.genderLabel.raise_()
        self.name.raise_()
        self.genderSelector.raise_()
        self.ageLabel.raise_()
        self.relationLabel.raise_()
        self.relationTable.raise_()
        self.editRelation.raise_()
        self.charInfoLabel.setBuddy(self.textEdit)
        self.titleLabel.setBuddy(self.titleSelector)
        self.fullNameLabel.setBuddy(self.name)
        self.speciesLabel.setBuddy(self.species)
        self.genderLabel.setBuddy(self.genderSelector)
        self.ageLabel.setBuddy(self.age)
        self.relationLabel.setBuddy(self.relationTable)

        self.retranslateUi(editPersonUI)
        QtCore.QMetaObject.connectSlotsByName(editPersonUI)
        editPersonUI.setTabOrder(self.titleSelector, self.name)
        editPersonUI.setTabOrder(self.name, self.species)
        editPersonUI.setTabOrder(self.species, self.genderSelector)
        editPersonUI.setTabOrder(self.genderSelector, self.age)
        editPersonUI.setTabOrder(self.age, self.dead)
        editPersonUI.setTabOrder(self.dead, self.textEdit)
        editPersonUI.setTabOrder(self.textEdit, self.relationTable)
        editPersonUI.setTabOrder(self.relationTable, self.addRelation)
        editPersonUI.setTabOrder(self.addRelation, self.acceptForm)
        editPersonUI.setTabOrder(self.acceptForm, self.editRelation)
        editPersonUI.setTabOrder(self.editRelation, self.removeRelation)
        editPersonUI.setTabOrder(self.removeRelation, self.characterID)

    def retranslateUi(self, editPersonUI):
        _translate = QtCore.QCoreApplication.translate
        self.acceptForm.setText(_translate("editPersonUI", "Submit"))
        self.charInfoLabel.setText(_translate("editPersonUI", "Character Description"))
        self.titleLabel.setText(_translate("editPersonUI", "Title"))
        self.titleSelector.setItemText(0, _translate("editPersonUI", "(None)"))
        self.titleSelector.setItemText(1, _translate("editPersonUI", "Mr"))
        self.titleSelector.setItemText(2, _translate("editPersonUI", "Ms"))
        self.titleSelector.setItemText(3, _translate("editPersonUI", "Mrs"))
        self.titleSelector.setItemText(4, _translate("editPersonUI", "Miss"))
        self.titleSelector.setItemText(5, _translate("editPersonUI", "Sir"))
        self.titleSelector.setItemText(6, _translate("editPersonUI", "Lady"))
        self.titleSelector.setItemText(7, _translate("editPersonUI", "Lord"))
        self.titleSelector.setItemText(8, _translate("editPersonUI", "King"))
        self.titleSelector.setItemText(9, _translate("editPersonUI", "Queen"))
        self.titleSelector.setItemText(10, _translate("editPersonUI", "Prince"))
        self.titleSelector.setItemText(11, _translate("editPersonUI", "Princess"))
        self.addRelation.setText(_translate("editPersonUI", "Add..."))
        self.fullNameLabel.setText(_translate("editPersonUI", "Full Name"))
        self.speciesLabel.setText(_translate("editPersonUI", "Species"))
        self.removeRelation.setText(_translate("editPersonUI", "Remove"))
        self.dead.setText(_translate("editPersonUI", "is Dead?"))
        self.species.setWhatsThis(_translate("editPersonUI", "<html><head/><body><p><br/></p></body></html>"))
        self.species.setPlaceholderText(_translate("editPersonUI", "Human, Elf, etc."))
        self.genderLabel.setText(_translate("editPersonUI", "Gender"))
        self.name.setWhatsThis(_translate("editPersonUI", "<html><head/><body><p><br/></p></body></html>"))
        self.name.setPlaceholderText(_translate("editPersonUI", "John Smith"))
        self.genderSelector.setItemText(0, _translate("editPersonUI", "(None)"))
        self.genderSelector.setItemText(1, _translate("editPersonUI", "Male"))
        self.genderSelector.setItemText(2, _translate("editPersonUI", "Female"))
        self.ageLabel.setText(_translate("editPersonUI", "Age"))
        self.relationLabel.setText(_translate("editPersonUI", "Relationships"))
        self.editRelation.setText(_translate("editPersonUI", "Edit..."))
