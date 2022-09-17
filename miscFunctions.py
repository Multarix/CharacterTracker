#	 ███╗░░░███╗██╗░██████╗░█████╗░    ███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
#	 ████╗░████║██║██╔════╝██╔══██╗    ██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
#	 ██╔████╔██║██║╚█████╗░██║░░╚═╝    █████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
#	 ██║╚██╔╝██║██║░╚═══██╗██║░░██╗    ██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
#	 ██║░╚═╝░██║██║██████╔╝╚█████╔╝    ██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
#	 ╚═╝░░░░░╚═╝╚═╝╚═════╝░░╚════╝░    ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░

from __future__ import annotations

import os, sys

from PyQt5.QtWidgets import *
from typehinting import startProgram

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

# Fixing python to not be shit
true = True;
false = False;


class miscFunctions():
	def __init__(this, self: startProgram) -> None:
		this.self = self;
	
	# Stolen from stackoverflow
	def resource_path(this, relativePath: str) -> str: # Borrowed from stackoverflow
		""" Get absolute path to resource, works for dev and for PyInstaller"""
		basePath = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)));
		return os.path.join(basePath, relativePath);
	
	
	def showDetails(this) -> None:
		self = this.self;
		self.ui.selectionDetails.clear();
		
		if(self.ui.characterList.currentRow() > -1):
			person = self.data["characters"][self.ui.characterList.currentRow()];
	
			gender = "None";
			if(person[4] == 1):
				gender = "Male";
			elif (person[4] == 2):
				gender = "Female";
				
			title = this.titleConversion(person[2]);
			if(title == ""):
				title = "None";
			
			self.ui.selectionDetails.insertItem(0, f"Title   ::  {title}");
			self.ui.selectionDetails.insertItem(1, f"Name    ::  {person[1]}");
			self.ui.selectionDetails.insertItem(2, f"Sex     ::  {gender}");
			self.ui.selectionDetails.insertItem(3, f"Age     ::  {person[3]}");
			self.ui.selectionDetails.insertItem(4, f"Species ::  {person[5]}");
			self.ui.selectionDetails.insertItem(5, f"Status  ::  {'Alive' if(person[6] == 0) else 'Dead'}");
			self.ui.selectionDetails.insertItem(6, f"\n{person[7]}");
	# End of function
	
	
	def searchBar(this, searchBar: QLineEdit, listToSearch: QListWidget) -> None:
		"""
		Function to hide or show items in the characterList on the mainWindowUI based on searchbar text
		"""
		self = this.self;
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
	# End of function
	

	# Disable/ Enable Buttons
	def unlockWorldBuildingEditRemoveBtns(this) -> None:
		self = this.self;
		enableOrNot = (self.ui.worldBuildingList.currentRow() > -1);
		self.ui.worldBuildingEdit.setEnabled(enableOrNot);
		self.ui.worldBuildingRemove.setEnabled(enableOrNot);
	# End of function
	
	def unlockWorldBuildingAcceptBtn(this):
		self = this.self;
		self.worldBuildingUI.accept.setDisabled(self.worldBuildingUI.textEditor.toPlainText() == "");
	# End of function

	def unlockEditRemoveCharacterBtns(this) -> None:
		self = this.self;
		currentRow = self.ui.characterList.currentRow();
		rowCount = self.ui.characterList.count();
		enableOrNot = (currentRow > -1);
		
		# Up Button
		upEnable = (currentRow > 0 and rowCount > 1);
		self.ui.moveUp.setEnabled(upEnable);
		
		# Down Button
		downEnable = (-1 < currentRow < (rowCount - 1) and rowCount > 1);
		self.ui.moveDown.setEnabled(downEnable);
		
		# Edit Buttons
		self.ui.editPerson.setEnabled(enableOrNot);
		self.ui.actionEdit_Character.setEnabled(enableOrNot);
		
		# Remove Buttons
		self.ui.removePerson.setEnabled(enableOrNot);
		self.ui.actionRemove_Character.setEnabled(enableOrNot);
	# End of function

	def unlockSubmitCharacterBtn(this) -> None:
		self = this.self;
		self.characterUI.acceptForm.setDisabled(self.characterUI.name == "");
	# End of function

	def unlockEditRemoveRelationBtn(this) -> None:
		self = this.self;
		enableOrNot = (self.characterUI.relationTable.currentRow() > -1);
		self.characterUI.editRelation.setEnabled(enableOrNot);
		self.characterUI.removeRelation.setEnabled(enableOrNot);
	# End of function

	def unlockAcceptRelationBtn(this) -> None:
		self = this.self;
		if(self.addRelationUI.characterList.currentRow() > -1 and self.addRelationUI.relationType.currentRow() > -1):
			self.addRelationUI.accept.setEnabled(true);
	# End of function


	def populateList(this, table: QListWidget, type: str) -> None:
		"""
		Fills out a list with data

		Args:
			table (QListWidget): A list object
		"""
		self = this.self;
		prevRow = table.currentRow();
		table.clear();
		if(type == "characters"):
			for person in self.data[type]:
				title = this.titleConversion(person[2]);
				space = " " if(len(title) > 0) else "";
				newRow = table.count()
				table.insertItem(newRow, f"{title}{space}{person[1]}");
				if(person[6] == 1):
					table.item(newRow).setIcon(self.deathIcon);
		
		if(type == "world"):
			for item in self.data[type]:
				newRow = table.count();
				table.insertItem(newRow, item[0]);
		
		if(type == "relation"):
			for relation in self._characterRelations:
				
				converted = this.relationTupleConversion(relation);
				if(not converted[0]):
					continue; # The relationship came up empty
				
				spaces = (self.settings["longestRelation"] - len(converted[1])) * " ";
				fullRelation = converted[1] + spaces + " | " + converted[0];
				
				newRow = table.count();
				table.insertItem(newRow, fullRelation);

		table.setCurrentRow(prevRow);
	# End of function


	# Conversions
	def relationConversion(this, item: int | str) -> str | int:
		"""
		Function to convert a relationship to/from an int/ string

		Args:
			item (int | str): The item to be converted

		Returns:
			(str | int): The item in its converted state
		"""
		return relationDict[item];
	# End of function

	def maxRelationLength(this) -> int:
		maxValue = 0;
		for value in relationDict:
			item = relationDict[value];
			if(len(item) > maxValue):
				maxValue = len(item);
		
		return maxValue;
	# End of function


	def titleConversion(this, item: int | str | None) -> str | int:
		"""
		Function to convert a title to/from an int/ string

		Args:
			item (int | str | None): The item to be converted

		Returns:
			(str | int): The item in its converted state
		"""
		return titleDict[item];
	# End of function


	def relationTupleConversion(this, relationship: tuple) -> tuple | None:
		self = this.self;
		personID = relationship[0];
		personRelation = relationship[1];
		
		personName = None;
		for person in self.data["characters"]:
			if(person[0] == personID):
				personName = person[1];
		
		if(personName == None):
			return None;
		
		personRelationName = this.relationConversion(personRelation);
		return (personName, personRelationName);