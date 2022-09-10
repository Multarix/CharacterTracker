from __future__ import annotations	# Type hinting

# Misc Imports
import sys
import os
import platform

# Saving, Loading etc
from fileManagement import fileManager, dataLayout
from all_ui_Elements import windows

# QT
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *

from ui_mainWindow import Ui_mainWindow as mainWindow

##########################
## To Do:				##
## Options Menu			##
## - Theme				##
## - Language?			##
##						##
## New File				##
## Window Modality		##
## Fix placeholder text	##
##########################

fontStyle = QtGui.QFont.StyleHint;
styleHint = fontStyle.TypeWriter

osType = platform.system();
if(osType == "Linux"):
	styleHint = fontStyle.Monospace;
	
if(osType == "Windows"):
	styleHint = fontStyle.TypeWriter;


true = True;
false = False;

defaultConfig = {
	"theme":"Dark",
	"lang": 0,
}

monospace = QtGui.QFont("Fira Code", 8);
monospace.setStyleHint(styleHint);


def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)));
	return os.path.join(base_path, relative_path);


class startProgram(QMainWindow):
	def __init__(self):
		super().__init__();
		self.setWindowTitle("Character Tracker");
		self.mainWindow = QtWidgets.QMainWindow();
		self.ui = mainWindow();
		self.ui.setupUi(self.mainWindow);
		
		# Palette fix cause modal window breaks it for some reason?
		palette = self.ui.characterSearch.palette()
		palette.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor("#a0a2a5"))
		self.ui.characterSearch.setPalette(palette);
		self.ui.worldBuildingSearch.setPalette(palette);
		
		miscData = {
			"font": monospace,
			"palette": palette
		}
		
		# ageSlider is not functional yet, so hide it
		self.ui.ageSlider.setHidden(true);
		self.ui.ageSliderCount.setHidden(true);
		
		# setup the rest of the stuff
		self.longestRelation = 10;
		self.settings = defaultConfig;
		
		self.windows = windows();
		self.file = fileManager();
		
		self.data: dataLayout;
		self.data = {
			"characters": [],
			"world": []
		};
		self._characterRelations = [];
		
		self.deathIcon = QtGui.QIcon();
		self.deathIcon.addPixmap(QtGui.QPixmap(resource_path(f"icons\\dead_{self.settings['theme']}.png")));
		
		# --Buttons to open other windows--
		# Add Character
		self.ui.addPerson.clicked.connect(lambda: self.windows.openEditCharacterWindow(self, miscData, true));
		# Edit Character
		self.ui.editPerson.clicked.connect(lambda: self.windows.openEditCharacterWindow(self, miscData, false));
		self.ui.characterList.itemDoubleClicked.connect(lambda: self.windows.openEditCharacterWindow(self, miscData, false));
		# Add World Building
		self.ui.worldBuildingAdd.clicked.connect(lambda: self.windows.openWorldBuildingWindow(self, miscData, true));
		# Edit World Building
		self.ui.worldBuildingEdit.clicked.connect(lambda: self.windows.openWorldBuildingWindow(self, miscData, false));
		self.ui.worldBuildingList.itemDoubleClicked.connect(lambda: self.windows.openWorldBuildingWindow(self, miscData, false));
		
		# Remove Character
		self.ui.removePerson.clicked.connect(lambda: self.removeCharacterBtn());
		# Remove World Building
		self.ui.worldBuildingRemove.clicked.connect(self.removeWorldBuilding);
		
		# Row Moving
		self.ui.moveUp.clicked.connect(lambda: self.moveRow(-1));
		self.ui.moveDown.clicked.connect(lambda: self.moveRow(1));
		
		# Unlocking/ Locking Buttons
		self.ui.characterList.itemSelectionChanged.connect(self.unlockEditRemoveCharacterBtns);
		self.ui.worldBuildingList.itemSelectionChanged.connect(self.unlockWorldBuildingEditRemoveBtns);
				
		# --Menu Options--
		# File Section
		# self.ui.action_New.triggered.connect(lambda: self.newFile())
		self.ui.action_Open.triggered.connect(self._open);
		self.ui.action_Save.triggered.connect(lambda: self.file.save(self, false, self.data));
		self.ui.actionSave_As.triggered.connect(lambda: self.file.save(self, true, self.data));
		
		# Edit Section
		self.ui.actionAdd_Character.triggered.connect(lambda: self.windows.openEditCharacterWindow(self, miscData, true));
		self.ui.actionEdit_Character.triggered.connect(lambda: self.windows.openEditCharacterWindow(self, miscData, false));
		self.ui.actionRemove_Character.triggered.connect(self.removeCharacterBtn);
		self.ui.actionRefresh.triggered.connect(lambda: self.populateList(self.ui.characterList, "characters"));
		self.ui.action_config.triggered.connect(lambda: self.windows.openOptionsWindow(self));
		
		# Help Section
		self.ui.action_Credits.triggered.connect(lambda: self.windows.openCreditsWindow(self));
		
		# --Misc Items--
		# Search bar
		self.ui.characterSearch.textEdited.connect(lambda: self.searchBar(self.ui.characterSearch, self.ui.characterList));
		self.ui.worldBuildingSearch.textEdited.connect(lambda: self.searchBar(self.ui.worldBuildingSearch, self.ui.worldBuildingList));
		
		# Details
		self.ui.characterList.itemSelectionChanged.connect(self.showDetails);
		
		# Font
		self.ui.characterSearch.setFont(monospace);
		self.ui.characterList.setFont(monospace);
		self.ui.selectionDetails.setFont(monospace);
		self.ui.worldBuildingList.setFont(monospace);
		self.ui.worldBuildingSearch.setFont(monospace);
	


	#	 ██████╗░██╗░░░██╗████████╗████████╗░█████╗░███╗░░██╗    ███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
	#	 ██╔══██╗██║░░░██║╚══██╔══╝╚══██╔══╝██╔══██╗████╗░██║    ██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
	#	 ██████╦╝██║░░░██║░░░██║░░░░░░██║░░░██║░░██║██╔██╗██║    █████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
	#	 ██╔══██╗██║░░░██║░░░██║░░░░░░██║░░░██║░░██║██║╚████║    ██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
	#	 ██████╦╝╚██████╔╝░░░██║░░░░░░██║░░░╚█████╔╝██║░╚███║    ██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
	#	 ╚═════╝░░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░░╚════╝░╚═╝░░╚══╝    ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░


	# Character stuff
	def acceptCharacterBtn(self, newChar: bool):
		"""
		Function to run when the accept button is pressed on the editCharacterUI

		Args:
			newChar (bool): Whether a character is new or not
		"""
		ui = self.characterUI;
				
		charID = ui.characterID.value();
		if(newChar and len(self.data["characters"]) >=1):
			charID = self.data["characters"][-1][0] + 1;
				
		name = ui.name.text();
		title = ui.titleSelector.currentIndex();
		age = ui.age.value();
		species = ui.species.text();
		info = ui.textEdit.toPlainText();
		gender = ui.genderSelector.currentIndex();
		
		isDead = 0;
		if(ui.dead.isChecked()):
			isDead = 1;
		
		relationArray = []
		for relation in self._characterRelations:
			relationArray.append(f"{relation[0]}|{relation[1]}");

		relationString = ", ".join(relationArray);

		self.editCharacterWindow.close(); # We no longer need anything from this ui, the rest can be done with it closed
		
		if(newChar): # New Character, apply to data
			self.data["characters"].append((int(charID), name, int(title), int(age), int(gender), species, int(isDead), info, relationString));
						
		else: # Not new character, find the character and overwrite it
			for i in range(len(self.data["characters"])):
				if(self.data["characters"][i][0] == charID):
					self.data["characters"][i] = (int(charID), name, int(title), int(age), int(gender), species, int(isDead), info, relationString);
					break;
		
		# Update the current list
		self.ui.characterList.clear();
		self.populateList(self.ui.characterList, "characters");


	def removeCharacterBtn(self):
		"""
		Function to run when pressing the remove button on the mainWindowUI
		"""
		ui = self.ui;
		indexOfItem = ui.characterList.currentRow();
		ui.characterList.takeItem(ui.characterList.currentRow());
		del self.data["characters"][indexOfItem];


	# Relation stuff
	def addRelationToListBtn(self, existing: bool):
		"""
		Function to run when pressing the accept button on the addRelationUI
		"""
		ui = self.characterUI;
		
		# Person Information
		selectedPerson = self.addRelationUI.characterList.currentRow();
		personData = self.data["characters"][selectedPerson];
		
		# Relationship
		selectedRelation = self.addRelationUI.relationType.currentRow();
		relationship = self.relationConversion(selectedRelation);
		spaces = (self.longestRelation - len(relationship)) * " ";
		relationship = relationship + spaces +  " | ";
		
		if(existing):
			itemRow = self.characterUI.relationTable.currentRow();
			self._characterRelations[itemRow] = (personData[0], selectedRelation);
		else:
			# Add to the internal relationship list
			self._characterRelations.append((personData[0], selectedRelation));
			# Adding to the table
		
		self.characterUI.relationTable.clear();
		self.populateList(self.characterUI.relationTable, "relation");
		self.addRelationWindow.close(); # Finally closing the UI


	def removeRelationBtn(self):
		"""
		Function to run when the remove button is pressed on the editCharacterUI
		"""
		currRow = self.characterUI.relationTable.currentRow();
		if(currRow > -1):
			self.characterUI.relationTable.takeItem(currRow);
			del self._characterRelations[currRow];
	

	# World Buidling Stuff
	def addWorldBuildingToListBtn(self, newDetail: bool):
		"""
		Function to run when clicking the accept button on the worldBuildingUI

		Args:
			newDetail (bool): Whether or not it's a new detail
		"""
		text = self.worldBuildingUI.textEditor.toPlainText();
		if(newDetail):
			self.data["world"].append((text, 0));
		else:
			itemRow = self.ui.worldBuildingList.currentRow();
			self.data["world"][itemRow] = (text, 0);
		
		self.ui.worldBuildingList.clear();
		self.populateList(self.ui.worldBuildingList, "world");
		self.worldBuildingWindow.close();
	
	
	def removeWorldBuilding(self):
		"""
		Function to run when clicking the remove button on the mainWindowUI
		"""
		currRow = self.ui.worldBuildingList.currentRow();
		if(currRow > -1):
			self.ui.worldBuildingList.takeItem(currRow);
			del self.data["world"][currRow];
			
	
	def moveRow(self, upDown: int):
		"""
		Function to move a list item up or down

		Args:
			upDown (int): 1 for down, -1 for up
		"""
		currentRow = self.ui.characterList.currentRow();
		currentItemText = self.ui.characterList.item(currentRow).text();
		currentItemIcon = self.ui.characterList.item(currentRow).icon();
		
		newRowIndex = currentRow + upDown;
		newItemText = self.ui.characterList.item(newRowIndex).text();
		newItemIcon = self.ui.characterList.item(newRowIndex).icon();
		
		# Swapping the data in the internal
		self.data["characters"][currentRow], self.data["characters"][newRowIndex] = self.data["characters"][newRowIndex], self.data["characters"][currentRow];
		
		# Setting newItem
		self.ui.characterList.item(currentRow).setText(newItemText);
		self.ui.characterList.item(currentRow).setIcon(newItemIcon);
		# Setting currentItem
		self.ui.characterList.item(newRowIndex).setText(currentItemText);
		self.ui.characterList.item(newRowIndex).setIcon(currentItemIcon);
		
		self.ui.characterList.setCurrentRow(currentRow + upDown);
		
	
	#	 ███╗░░░███╗██╗░██████╗░█████╗░    ███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
	#	 ████╗░████║██║██╔════╝██╔══██╗    ██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
	#	 ██╔████╔██║██║╚█████╗░██║░░╚═╝    █████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
	#	 ██║╚██╔╝██║██║░╚═══██╗██║░░██╗    ██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
	#	 ██║░╚═╝░██║██║██████╔╝╚█████╔╝    ██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
	#	 ╚═╝░░░░░╚═╝╚═╝╚═════╝░░╚════╝░    ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░
	
	
	def showDetails(self):
		self.ui.selectionDetails.clear();
		
		if(self.ui.characterList.currentRow() > -1):
			person = self.data["characters"][self.ui.characterList.currentRow()];
	
			gender = "None";
			if(person[4] == 1):
				gender = "Male";
			elif (person[4] == 2):
				gender = "Female";
				
			title = self.titleConversion(person[2]);
			if(title == ""):
				title = "None"
			
			self.ui.selectionDetails.insertItem(0, f"Title   ::  {title}");
			self.ui.selectionDetails.insertItem(1, f"Name    ::  {person[1]}");
			self.ui.selectionDetails.insertItem(2, f"Sex     ::  {gender}");
			self.ui.selectionDetails.insertItem(3, f"Age     ::  {person[3]}");
			self.ui.selectionDetails.insertItem(4, f"Species ::  {person[5]}");
			self.ui.selectionDetails.insertItem(5, f"Status  ::  {'Alive' if(person[6] == 0) else 'Dead'}");
			self.ui.selectionDetails.insertItem(6, f"\n{person[7]}");
	
	
	def searchBar(self, searchBar: QLineEdit, listToSearch: QListWidget):
		"""
		Function to hide or show items in the characterList on the mainWindowUI based on searchbar text
		"""
		searchTerm = searchBar.text();
		characterList = []
		for i in range(listToSearch.count()):
			characterList.append(listToSearch.item(i));
		
		character: QListWidgetItem;
		if(searchTerm == ""): # Unhide everything
			for character in characterList:
				character.setHidden(false);

		else: # Hide/ unhide based on the results
			for character in characterList:
				character.setHidden(not (searchTerm.lower() in character.text().lower()));

	# Disable/ Enable Buttons
	def unlockWorldBuildingEditRemoveBtns(self):
		enableOrNot = (self.ui.worldBuildingList.currentRow() > -1);
		self.ui.worldBuildingEdit.setEnabled(enableOrNot);
		self.ui.worldBuildingRemove.setEnabled(enableOrNot);
	
	def unlockWorldBuildingAcceptBtn(self):
		self.worldBuildingUI.accept.setDisabled(self.worldBuildingUI.textEditor.toPlainText() == "");


	def unlockEditRemoveCharacterBtns(self):
		currentRow = self.ui.characterList.currentRow();
		enableOrNot = (currentRow > -1);
		
		# Up Button
		upEnable = (currentRow > 0)
		self.ui.moveUp.setEnabled(upEnable);
		
		# Down Button
		downEnable = (-1 < currentRow < (self.ui.characterList.count() - 1));
		self.ui.moveDown.setEnabled(downEnable);
		
		# Edit Buttons
		self.ui.editPerson.setEnabled(enableOrNot);
		self.ui.actionEdit_Character.setEnabled(enableOrNot);
		
		# Remove Buttons
		self.ui.removePerson.setEnabled(enableOrNot);
		self.ui.actionRemove_Character.setEnabled(enableOrNot);


	def unlockSubmitCharacterBtn(self):
		self.characterUI.acceptForm.setDisabled(self.characterUI.name == "");


	def unlockEditRemoveRelationBtn(self):
		enableOrNot = (self.characterUI.relationTable.currentRow() > -1)
		self.characterUI.editRelation.setEnabled(enableOrNot);
		self.characterUI.removeRelation.setEnabled(enableOrNot);


	def unlockAcceptRelationBtn(self):
		"""
		Function to unlock the accept button on the addRelationUI
		"""
		if(self.addRelationUI.characterList.currentRow() > -1 and self.addRelationUI.relationType.currentRow() > -1):
			self.addRelationUI.accept.setEnabled(true);

	# Conversions
	def relationConversion(self, item: int | str) -> str | int:
		"""
		Function to convert a relationship to/from an int/ string

		Args:
			item (int | str): The item to be converted

		Returns:
			(str | int): The item in its converted state
		"""
		# Max Length is Girlfriend at 10
		relationDict = {
			0   : "Father",
			"0" : "Father",
			1   : "Mother",
			"1" : "Mother",
			2   : "Son",
			"2" : "Son",
			3   : "Daughter",
			"3" : "Daughter",
			4   : "Brother",
			"4" : "Brother",
			5   : "Sister",
			"5" : "Sister",
			6   : "Uncle",
			"6" : "Uncle",
			7   : "Aunt",
			"7" : "Aunt",
			8   : "Nephew",
			"8" : "Nephew",
			9   : "Niece",
			"9" : "Niece",
			10  : "Boyfriend",
			"10": "Boyfriend",
			11  : "Girlfriend",
			"11": "Girlfriend",
			12  : "Fiancé",
			"12": "Fiancé",
			13  : "Husband",
			"13": "Husband",
			14  : "Wife",
			"14": "Wife"
		}
			
		return relationDict[item];
	
	
	def titleConversion(self, item: int | str | None) -> str | int:
		"""
		Function to convert a title to/from an int/ string

		Args:
			item (int | str | None): The item to be converted

		Returns:
			(str | int): The item in its converted state
		"""
		titleDict = {
			0: "",
			"0": "",
			1: "Mr",
			"1": "Mr",
			2: "Ms",
			"2": "Ms",
			3: "Mrs",
			"3": "Mrs",
			4: "Miss",
			"4": "Miss",
			5: "Sir",
			"5": "Sir",
			6: "Lady",
			"6": "Lady",
			7: "Lord",
			"7": "Lord",
			8: "King",
			"8": "King",
			9: "Queen",
			"9": "Queen",
			10: "Prince",
			"10": "Prince",
			11: "Princess",
			"11": "Princess"
		}
		return titleDict[item];
		
		
	def relationTupleConversion(self, relationship: tuple) -> tuple | None:
		personID = relationship[0]
		personRelation = relationship[1];
		
		personName = None;
		for person in self.data["characters"]:
			if(person[0] == personID):
				personName = person[1];
		
		if(personName == None):
			return None;
		
		personRelationName = self.relationConversion(personRelation);
		return (personName, personRelationName)


	def populateList(self, table: QListWidget, type: str):
		"""
		Fills out a list with data

		Args:
			table (QListWidget): A list object
		"""
		table.clear();
		if(type == "characters"):
			for person in self.data[type]:
				title = self.titleConversion(person[2])
				space = " " if(len(title) > 0) else "";
				newRow = table.count()
				table.insertItem(newRow, f"{title}{space}{person[1]}");
				if(person[6] == 1):
					table.item(newRow).setIcon(self.deathIcon);
		
		if(type == "world"):
			for item in self.data[type]:
				newRow = table.count()
				table.insertItem(newRow, item[0]);
		
		if(type == "relation"):
			for relation in self._characterRelations:
				
				converted = self.relationTupleConversion(relation);
				if(not converted[0]):
					continue; # The relationship came up empty
				
				spaces = (self.longestRelation - len(converted[1])) * " ";
				fullRelation = converted[1] + spaces + " | " + converted[0];
				
				newRow = table.count()
				table.insertItem(newRow, fullRelation);
	
	
	#	 ███████╗██╗██╗░░░░░███████╗  
	#	 ██╔════╝██║██║░░░░░██╔════╝  
	#	 █████╗░░██║██║░░░░░█████╗░░  
	#	 ██╔══╝░░██║██║░░░░░██╔══╝░░  
	#	 ██║░░░░░██║███████╗███████╗  
	#	 ╚═╝░░░░░╚═╝╚══════╝╚══════╝  
	#	 ███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗███╗░░░███╗███████╗███╗░░██╗████████╗
	#	 ████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝████╗░████║██╔════╝████╗░██║╚══██╔══╝
	#	 ██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░
	#	 ██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░
	#	 ██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░
	#	 ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░
		
	
	def _open(self):
		self.file.open(self);
		self.data = self.file.data;
		self.populateList(self.ui.characterList, "characters");
		self.populateList(self.ui.worldBuildingList, "world");
		pass;


if __name__ == "__main__":
	app = QApplication(sys.argv);
	app.setApplicationDisplayName("Character Tracker");
	win = startProgram();
	win.mainWindow.show();
	sys.exit(app.exec());