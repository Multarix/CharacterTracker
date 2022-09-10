from __future__ import annotations
from typing import TypedDict
from typing import Tuple

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *

from ui_mainWindow import Ui_mainWindow as mainWindow
from ui_editPersonWindow import Ui_editPersonWindow as editPersonWindow
from ui_addRelationWindow import Ui_addRelationWindow as addRelationWindow
from ui_worldBuildingWindow import Ui_worldBuildingWindow as worldBuildingWindow
from ui_optionsWindow import Ui_optionsWindow as optionsWindow
from ui_infoWindow import Ui_creditsWindow as creditsWindow


character = Tuple[int, str, int, int, int, str, int, str, str]
worldItem = Tuple[str, int]
class dataLayout(TypedDict):
	"""Character and World data layout"""
	characters: list[character];
	world: list[worldItem];


class miscDataLayout(TypedDict):
	font: QtGui.QFont;
	palette: QtGui.QPalette


class config(TypedDict):
	"""Config settings layout"""
	theme: str;
	lang: int;


class startProgram():
	def __init__(self) -> None:
		# Main Window
		self.mainWindow = QtWidgets.QMainWindow();
		self.ui = mainWindow();
		self.ui.setupUi();

		# Credits Window
		self.creditsWindow = QtWidgets.QDialog();
		self.creditsUI = creditsWindow();
		self.creditsUI.setupUi();
		
		# Options Window (Disabled)
		self.optionsWindow = QtWidgets.QDialog();
		self.optionsUI = optionsWindow();
		self.optionsUI.setupUi();
		
		# Edit Character Window
		self.editCharacterWindow = QtWidgets.QWidget();
		self.characterUI = editPersonWindow();
		self.characterUI.setupUi();
		
		# Add Relation Window
		self.addRelationWindow = QtWidgets.QWidget();
		self.addRelationUI = addRelationWindow();
		self.addRelationUI.setupUi();
		
		# World Building Window
		self.worldBuildingWindow = QtWidgets.QDialog();
		self.worldBuildingUI = worldBuildingWindow();
		self.worldBuildingUI.setupUi();
		
		self.settings: config
		self.settings = {
			"theme":"Dark",
			"lang": 0,
		}
		self.data: dataLayout;
		self.data = {
			"characters": [],
			"world": []
		};
		
		self._characterRelations = [];
	
	def acceptCharacterBtn(self, newChar: bool):
		"""
		Function to run when the accept button is pressed on the editCharacterUI

		Args:
			newChar (bool): Whether a character is new or not
		"""
		pass;


	def removeCharacterBtn(self):
		"""
		Function to run when pressing the remove button on the mainWindowUI
		"""
		pass;


	def addRelationToListBtn(self, existing: bool):
		"""
		Function to run when pressing the accept button on the addRelationUI
		"""
		pass;
		
	
	def removeRelationBtn(self):
		"""
		Function to run when the remove button is pressed on the editCharacterUI
		"""
		pass;
	
	
	def addWorldBuildingToListBtn(self, newDetail: bool):
		"""
		Function to run when clicking the accept button on the worldBuildingUI

		Args:
			newDetail (bool): Whether or not it's a new detail
		"""
		pass;
	
	
	def removeWorldBuilding(self):
		"""
		Function to run when clicking the remove button on the mainWindowUI
		"""
		pass;

	
	def searchBar(self, searchBar: QLineEdit, listToSearch: QListWidget):
		"""
		Function to hide or show items in the characterList on the mainWindowUI based on searchbar text
		"""
		pass;
		
	
	def unlockWorldBuildingEditRemoveBtns(self):
		pass;
	
	def unlockWorldBuildingAcceptBtn(self):
		pass;
	
	def unlockEditRemoveCharacterBtns(self):
		pass;
	
	def unlockSubmitCharacterBtn(self):
		pass;
	
	def unlockEditRemoveRelationBtn(self):
		pass;
	
	def unlockAcceptRelationBtn(self):
		pass;
	
	
	def relationConversion(self, item: int | str) -> str | int:
		"""
		Function to convert a relationship to/from an int/ string

		Args:
			item (int | str): The item to be converted

		Returns:
			(str | int): The item in its converted state
		"""
		pass;
	
	def relationTupleConversion(self, relationship: tuple) -> tuple | None:
		pass;
	
	
	def titleConversion(self, item: int | str | None) -> str | int:
		"""
		Function to convert a title to/from an int/ string

		Args:
			item (int | str | None): The item to be converted

		Returns:
			(str | int): The item in its converted state
		"""
		pass;
	
	
	def populateList(self, table: QListWidget, type: str):
		"""
		Fills out a list with data

		Args:
			table (QListWidget): A list object
		"""
		pass;