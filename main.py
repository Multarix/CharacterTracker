from __future__ import annotations  # Type hinting

import sys
import os
import platform
import sqlite3

# QT
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from mainWindow import Ui_mainWindowUI
from editPerson import Ui_editPersonUI
from addRelation import Ui_addRelation
from info import Ui_creditsUI

#
#
#
# Edit existing Relationships - Done
# Perhaps re-order Characters - Too Complicated
# Options Menu
# Save File - Done... I think
# Search Function - Done
#
#
#

osType = platform.system()
monospace = "Monospace";

if(osType == "macOS"): # Eat shit apple fuckboys
	sys.exit();

if(osType == "Windows"):
	monospace = "Courier New";

true = True;
false = False;

def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)));
	return os.path.join(base_path, relative_path);

defaultConfig = { "theme": "Dark" }

class UI_MainWindow(QMainWindow):
	def __init__(self):
		super().__init__();
		self.setWindowTitle("Character Tracker");
		self.mainWindow = QtWidgets.QMainWindow();
		self.ui = Ui_mainWindowUI();
		self.ui.setupUi(self.mainWindow);
		self.longestRelation = 10;
		self.fileName = None;
		self.database = None;
		self.data = [];
		self._characterRelations = [];
		self.config = defaultConfig;
		
		self.deathIcon = QtGui.QIcon()
		print(resource_path(f"icons\\dead_{self.config['theme']}.png"))
		self.deathIcon.addPixmap(QtGui.QPixmap(resource_path(f"icons\\dead_{self.config['theme']}.png")));
		
		# --Buttons to open other windows--
		# Add Character
		self.ui.addPerson.clicked.connect(lambda: self.openEditCharacterUI(true));
		
		# Edit Character
		self.ui.editPerson.clicked.connect(lambda: self.openEditCharacterUI(false));
		self.ui.characterList.itemSelectionChanged.connect(lambda: self.ui.editPerson.setEnabled(true));
	
		# Remove Character
		self.ui.removePerson.clicked.connect(lambda: self.removeCharacterBtn());
		self.ui.characterList.itemSelectionChanged.connect(self.unlockEditRemoveCharacterBtns);
		self.ui.characterList.itemDoubleClicked.connect(lambda: self.openEditCharacterUI(false));
		
		# --Menu Options--
		# File Section
		# self.ui.action_New.triggered.connect(lambda: self.newFile())
		self.ui.action_Open.triggered.connect(self.openFile);
		self.ui.action_Save.triggered.connect(self.saveFile);
		self.ui.actionSave_As.triggered.connect(self.saveFileAs);
		
		# Edit Section
		self.ui.actionAdd_Character.triggered.connect(lambda: self.openEditCharacterUI(true));
		self.ui.actionEdit_Character.triggered.connect(lambda: self.openEditCharacterUI(false));
		self.ui.actionRemove_Character.triggered.connect(self.removeCharacterBtn);
		self.ui.actionRefresh.triggered.connect(lambda: self.populateList(self.ui.characterList));
		# self.ui.action_config.triggered.connect(self.openConfigUI);
		
		# Help Section
		self.ui.action_Credits.triggered.connect(self.openCreditsUI)
		
		# --Misc Items--
		# Search bar
		self.ui.characterSearch.textEdited.connect(lambda: self.searchBar(self.ui.characterSearch, self.ui.characterList));
		
		# Details
		self.ui.characterList.itemSelectionChanged.connect(self.showDetails);
		
		# DragDrop
		# self.ui.characterList.dropEvent.connect(self.indexMove) # This is too complicated for now


	#	 ██╗░░░██╗██╗    ███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
	#	 ██║░░░██║██║    ██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
	#	 ██║░░░██║██║    █████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
	#	 ██║░░░██║██║    ██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
	#	 ╚██████╔╝██║    ██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
	#	 ░╚═════╝░╚═╝    ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░
	
	
	def openCreditsUI(self):
		self.credits = QtWidgets.QDialog();
		self.creds = Ui_creditsUI();
		self.creds.setupUi(self.credits);
		self.credits.show();
	
	
	def openEditCharacterUI(self, newChar: bool):
		"""
		Function to open the editCharacterUI when pressing the add or edit button on the mainWindowUI

		Args:
			newChar (bool): Whether a character is new or not
		"""
		self.editCharacter = QtWidgets.QWidget();
		self.editChar = Ui_editPersonUI();
		self.editChar.setupUi(self.editCharacter);
		self.editChar.characterID.hide();
		self.editChar.characterID.setMaximum(9999);
		self.editChar.relationTable.setFont(QtGui.QFont(monospace, 8));
		
		self._characterRelations.clear();
		
		# Buttons
		# Add
		self.editChar.addRelation.clicked.connect(lambda: self.openAddRelationUI(false));
		
		# Edit
		self.editChar.editRelation.clicked.connect(lambda: self.openAddRelationUI(true));
		self.editChar.relationTable.currentRowChanged.connect(self.unlockEditRelationBtn)
		
		# Remove
		self.editChar.removeRelation.clicked.connect(self.removeRelationBtn);
		self.editChar.removeRelation.setDisabled(true);
		self.editChar.relationTable.itemSelectionChanged.connect(lambda: self.editChar.removeRelation.setEnabled(true));
		
		# Accept
		self.editChar.acceptForm.setDisabled(newChar);
		self.editChar.name.textEdited.connect(self.unlockSubmitCharacterBtn);
		self.editChar.acceptForm.clicked.connect(lambda: self.acceptCharacterBtn(newChar));

		if(not newChar):
			currSelected = self.ui.characterList.currentRow();
			charData = self.data[currSelected] # This should work if the list is always up to date
			# id, name, title, age, gender (0=None, 1=Male, 2=Female), species, isdead (0=Alive), information, relations
			# 0   1     2      3    4                                  5        6                 7            8
			# ID
			self.editChar.characterID.setValue(charData[0]);
			
			# Full Name
			self.editChar.name.setText(charData[1]);
			
			# Title
			self.editChar.titleSelector.setCurrentIndex(int(charData[2]));
			
			# Age
			self.editChar.age.setValue(charData[3]);
			
			# Species
			self.editChar.species.setText(charData[5]);
			
			# Character information
			self.editChar.textEdit.setText(charData[7]);
			
			# Is Dead
			if(charData[6] == 1):
				self.editChar.dead.setChecked(true);
			
			# Gender
			self.editChar.genderSelector.setCurrentIndex(charData[4]);
			
			# Relations
			relations: str;
			relations = charData[8];
			if(relations):
				relationsArray = relations.split(", "); # Each relationship is seperated by ", "
				
				for relation in relationsArray:
					rel = relation.split("|"); # Each side of the relation is seperated by a "|"
					# rel[0] is the person, rel[1] is the type of relationship
					
					self._characterRelations.append((int(rel[0]), int(rel[1]))); # Add the item to the internal list, for later
					relationType = self.relationConversion(rel[1]); # Text equivilent
					
					# Make sure they're all the same length
					spaces = (self.longestRelation - len(relationType)) * " ";
					relationType = relationType + spaces + " | ";
					
					for character in self.data:
						if(character[0] == int(rel[0])):
							self.editChar.relationTable.insertItem(self.editChar.relationTable.count(), f"{relationType}{character[1]}");
							break;
		
		self.editCharacter.show()


	def openAddRelationUI(self, existing: bool):
		"""
		Function to open the addRelationUI when pressing the add button on the editCharacterUI
		"""
		self.addRelation = QtWidgets.QWidget();
		self.addRel = Ui_addRelation();
		self.addRel.setupUi(self.addRelation);
		self.populateList(self.addRel.characterList);
	
		self.addRel.accept.clicked.connect(lambda: self.addRelationToList(existing));
		self.addRel.characterList.itemSelectionChanged.connect(self.unlockAcceptRelationBtn);
		self.addRel.relationType.itemSelectionChanged.connect(self.unlockAcceptRelationBtn);
		
		# Search bars
		self.addRel.search.textEdited.connect(lambda: self.searchBar(self.addRel.search, self.addRel.characterList));
		self.addRel.searchRelation.textEdited.connect(lambda: self.searchBar(self.addRel.searchRelation, self.addRel.relationType));
		
		if(existing): # Existing relationship
			relationIndex = self.editChar.relationTable.currentRow();
			relationship = self._characterRelations[relationIndex];
			personID = relationship[0];
			relationTypeIndex = relationship[1];
			
			for i in range(len(self.data)):
				person = self.data[i];
				if(personID == person[0]):
					self.addRel.characterList.setCurrentRow(i);
					self.addRel.relationType.setCurrentRow(relationTypeIndex);
					break;
			
			
		
		self.addRelation.show();


	#	 ██████╗░██╗░░░██╗████████╗████████╗░█████╗░███╗░░██╗    ███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
	#	 ██╔══██╗██║░░░██║╚══██╔══╝╚══██╔══╝██╔══██╗████╗░██║    ██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
	#	 ██████╦╝██║░░░██║░░░██║░░░░░░██║░░░██║░░██║██╔██╗██║    █████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
	#	 ██╔══██╗██║░░░██║░░░██║░░░░░░██║░░░██║░░██║██║╚████║    ██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
	#	 ██████╦╝╚██████╔╝░░░██║░░░░░░██║░░░╚█████╔╝██║░╚███║    ██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
	#	 ╚═════╝░░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░░╚════╝░╚═╝░░╚══╝    ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░


	def removeCharacterBtn(self):
		"""
		Function to run when pressing the remove button on the mainWindowUI
		"""
		ui = self.ui;
		indexOfItem = ui.characterList.currentRow();
		if(indexOfItem > -1):
			ui.characterList.takeItem(ui.characterList.currentRow());
			del self.data[indexOfItem];
		
		# If the list is now empty, disable the removePerson button
		if(ui.characterList.count() == 0):
			self.ui.actionRemove_Character.setDisabled(true);
			ui.removePerson.setDisabled(true);
	
	
	# Add Relation UI
	def addRelationToList(self, existing: bool):
		"""
		Function to run when pressing the accept button on the addRelationUI
		"""
		ui = self.editChar;
		
		# Person Information
		selectedPerson = self.addRel.characterList.currentRow();
		personData = self.data[selectedPerson];
		
		# Relationship
		selectedRelation = self.addRel.relationType.currentRow();
		relationship = self.relationConversion(selectedRelation);
		spaces = (self.longestRelation - len(relationship)) * " ";
		relationship = relationship + spaces +  " | ";
		
		# Add to the internal relationship list
		self._characterRelations.append((personData[0], selectedRelation))
		
		# Adding to the table
		ui.relationTable.insertItem(ui.relationTable.count(), f"{relationship}{personData[1]}");
		# ui.removeRelation.setDisabled(false); # Enable the remove button
		self.addRelation.close(); # Finally closing the UI


	# Character Editor UI
	def removeRelationBtn(self):
		"""
		Function to run when the remove button is pressed on the editCharacterUI
		"""
		ui = self.editChar;
		currRow = ui.relationTable.currentRow();
		if(currRow > -1):
			ui.relationTable.takeItem(currRow);
			del self._characterRelations[currRow];
		
		if(ui.relationTable.count() == 0):
			ui.removeRelation.setDisabled(true);


	def acceptCharacterBtn(self, newChar: bool):
		"""
		Function to run when the accept button is pressed on the editCharacterUI

		Args:
			newChar (bool): Whether a character is new or not
		"""
		ui = self.editChar;
				
		charID = ui.characterID.value();
		if(newChar and len(self.data) >=1):
			charID = self.data[-1][0] + 1;
				
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

		self.editCharacter.close(); # We no longer need anything from this ui, the rest can be done with it closed
		
		if(newChar): # New Character, apply to data
			self.data.append((int(charID), name, int(title), int(age), int(gender), species, int(isDead), info, relationString));
						
		else: # Not new character, find the character and overwrite it
			for i in range(len(self.data)):
				if(self.data[i][0] == charID):
					self.data[i] = (int(charID), name, int(title), int(age), int(gender), species, int(isDead), info, relationString);
					break;
		
		# Update the current list
		self.ui.characterList.clear();
		self.populateList(self.ui.characterList);
	
	
	#	 ███╗░░░███╗██╗░██████╗░█████╗░    ███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
	#	 ████╗░████║██║██╔════╝██╔══██╗    ██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
	#	 ██╔████╔██║██║╚█████╗░██║░░╚═╝    █████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
	#	 ██║╚██╔╝██║██║░╚═══██╗██║░░██╗    ██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
	#	 ██║░╚═╝░██║██║██████╔╝╚█████╔╝    ██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
	#	 ╚═╝░░░░░╚═╝╚═╝╚═════╝░░╚════╝░    ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░
	
	
	def showDetails(self):
		self.ui.selectionDetails.clear();
		
		if(self.ui.characterList.currentRow() > -1):
			person = self.data[self.ui.characterList.currentRow()];
	
			gender = "None";
			if(person[4] == 1):
				gender = "Male";
			elif (person[4] == 2):
				gender = "Female";
				
			title = self.titleConversion(person[2]);
			if(title == ""):
				title = "None"
			
			self.ui.selectionDetails.insertItem(0, f"Title:   {title}");
			self.ui.selectionDetails.insertItem(1, f"Name:   {person[1]}");
			self.ui.selectionDetails.insertItem(2, f"Sex:   {gender}");
			self.ui.selectionDetails.insertItem(3, f"Age:   {person[3]}");
			self.ui.selectionDetails.insertItem(4, f"Species:   {person[5]}");
			self.ui.selectionDetails.insertItem(5, f"Status:   {'Alive' if(person[6] == 0) else 'Dead'}");
			self.ui.selectionDetails.insertItem(6, f"Description:\n\r{person[7]}");
	
	
	def searchBar(self, searchBar: QLineEdit, listToSearch: QListWidget):
		"""
		Function to hide or show items in the characterList on the mainWindowUI based on searchbar text
		"""
		searchTerm = searchBar.text();
		characterList = []
		for i in range(listToSearch.count()):
			characterList.append(listToSearch.item(i))
		
		character: QListWidgetItem;
		if(searchTerm == ""): # Unhide everything
			for character in characterList:
				character.setHidden(false);

		else: # Hide/ unhide based on the results
			for character in characterList:
				character.setHidden(not (searchTerm in character.text()));
	
	def unlockEditRemoveCharacterBtns(self):
		enableOrNot = (self.ui.characterList.currentRow() == -1)
		# Edit Buttons
		self.ui.removePerson.setDisabled(enableOrNot)
		self.ui.actionRemove_Character.setDisabled(enableOrNot)
		
		# Remove Buttons
		self.ui.removePerson.setDisabled(enableOrNot)
		self.ui.actionRemove_Character.setDisabled(enableOrNot)
	
	def unlockAcceptRelationBtn(self):
		"""
		Function to unlock the accept button on the addRelationUI
		"""
		if(self.addRel.characterList.currentRow() > -1 and self.addRel.relationType.currentRow() > -1):
			self.addRel.accept.setEnabled(true);
	
	def unlockSubmitCharacterBtn(self):
		self.editChar.acceptForm.setDisabled(self.editChar.name == "");


	def unlockEditRelationBtn(self):
		self.editChar.editRelation.setEnabled(self.editChar.relationTable.currentRow() > -1);
		

	def relationConversion(self, item: int | str) -> str | int:
		"""
		Function to convert a relationship to/from an int/ string

		Args:
			item (int | str): The item to be converted

		Returns:
			str | int: The item in its converted state
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
			str | int: The item in its converted state
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


	def populateList(self, table: QListWidget):
		"""
		Fills out a list with data

		Args:
			table (QListWidget): A list object
		"""
		table.clear();
		for person in self.data:
			title = self.titleConversion(person[2])
			space = " " if(len(title) > 0) else "";
			newRow = table.count()
			table.insertItem(newRow, f"{title}{space}{person[1]}");
			if(person[6] == 1):
				table.item(newRow).setIcon(self.deathIcon);
	
	
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
	
	
	# def newFile(self):
	# 	pass
	# Gonna just wipe everything, close window and re-open
	# Also ask to confirm

	def createSchema(self):
		if(not self.database):
			return;
		
		sql = self.database.cursor();
		sql.execute('CREATE TABLE "characters" ("id" INTEGER, "name" TEXT, "title" INTEGER, "age" INTEGER, "gender" INTEGER, "species" TEXT, "isdead" INTEGER, "information" TEXT, "relationships" TEXT)');
		self.database.commit();

	
	def saveFileAs(self) -> bool:
		"""
		Function to save a file with a specific filename

		Returns:
			bool: Whether the function executed successfully or not
		"""
		fileLocation = QFileDialog.getSaveFileUrl(self, "Save File", QtCore.QUrl(""), "SQL Files (*.sqlite *.sqlite3)", "SQL Files (*.sqlite *.sqlite3)")[0].toString();
		if(fileLocation == ""):
			return;
		
		fileLocation = fileLocation.replace("file:///", "");
		fileArray = fileLocation.split("/");
		fileName = fileArray.pop();
		pathToFile = "/".join(fileArray);
		filePath = os.path.join(pathToFile, fileName);
		
		# print(filePath);
		try:
			filePath = os.path.join(pathToFile, fileName);
			if(not os.path.exists(pathToFile)):
				os.makedirs(pathToFile);
			
			file = open(filePath, "w");
			file.write("");
			file.close();
			
			self.database = sqlite3.connect(filePath);
			self.createSchema()
			
			self.fileName = filePath;
			return true;
		except:
			self.errorMessage("An error occured while saving the file");
			return false;
		
				
	def saveFile(self):
		if(not self.fileName):
			successful = self.saveFileAs();
			
			if(not successful):
				self.errorMessage("An error occured while saving the file");
		
		self.deleteRecords();
		print("Saving Changes...");
		try:
			for person in self.data:
				sql = self.database.cursor()
				sql.execute(f"INSERT INTO characters (id, name, title, age, gender, species, isdead, information, relationships) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", person);
				self.database.commit();
			
		except:
			self.errorMessage("An error occured while saving the file");


	def deleteRecords(self):
		try:
			sql = self.database.cursor();
			sql.execute("DELETE FROM characters");
			self.database.commit();
		except:
			self.errorMessage("An error occured while saving the file");
		

	def openFile(self):
		"""
		Opens an sqlite database

		Args:
			file (str): The URL to the file
		"""
		fileName = QFileDialog.getOpenFileName(self, "Choose File", "", "SQL Files (*.sqlite *.sqlite3);;All Files (*)");
		if(not fileName[0]):
			return;
		
		try:
			self.database = sqlite3.connect(fileName[0]);
			sql = self.database.cursor();
			sql.execute("SELECT * FROM characters");
			
			self.data = sql.fetchall();
			self.populateList(self.ui.characterList);
			self.fileName = fileName[0];
		except:
			self.errorMessage("An error occured while trying to open the file");
			
	
	def errorMessage(self, message: str):
		QMessageBox.critical(self, "Error", message);


if __name__ == "__main__":
	app = QApplication(sys.argv);
	app.setApplicationDisplayName("Character Tracker");
	win = UI_MainWindow();
	win.mainWindow.show();
	sys.exit(app.exec());