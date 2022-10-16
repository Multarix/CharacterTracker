#	 ███╗░░░███╗██╗░██████╗░█████╗░    ███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
#	 ████╗░████║██║██╔════╝██╔══██╗    ██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
#	 ██╔████╔██║██║╚█████╗░██║░░╚═╝    █████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
#	 ██║╚██╔╝██║██║░╚═══██╗██║░░██╗    ██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
#	 ██║░╚═╝░██║██║██████╔╝╚█████╔╝    ██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
#	 ╚═╝░░░░░╚═╝╚═╝╚═════╝░░╚════╝░    ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░

from __future__ import annotations

import os, sys, re
from PyQt5.QtWidgets import *			# type: ignore
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
			if(person[5] == 1):
				gender = "Male";
			elif (person[5] == 2):
				gender = "Female";
				
			title = this.titleConversion(person[3]);
			if(title == ""):
				title = "None";
				
			lastName = f" {person[2]}" if(person[2]) else "";
			
			self.ui.selectionDetails.insertItem(0, f"Title   ::  {title}");
			self.ui.selectionDetails.insertItem(1, f"Name    ::  {person[1]}{lastName}");
			self.ui.selectionDetails.insertItem(2, f"Sex     ::  {gender}");
			self.ui.selectionDetails.insertItem(3, f"Age     ::  {person[4]}");
			self.ui.selectionDetails.insertItem(4, f"Species ::  {person[6]}");
			self.ui.selectionDetails.insertItem(5, f"Status  ::  {'Alive' if(person[7] == 0) else 'Dead'}");
			
			charInfoArray = person[8].split("│");
			charInfo = "\n".join(charInfoArray);
			self.ui.selectionDetails.insertItem(6, f"\n{charInfo}");
			self.ui.selectionDetails.insertItem(7, "");
	# End of function
	
	
	def searchBar(this, searchBar: QLineEdit, listToSearch: QListWidget) -> None:
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
	
	def unlockEditRemoveEventBtns(this) -> None:
		self = this.self;
		enableOrNot = (self.ui.eventList.currentRow() > -1);
		self.ui.eventEdit.setEnabled(enableOrNot);
		self.ui.eventRemove.setEnabled(enableOrNot);
	
	def unlockAddEventsAcceptBtn(this):
		self = this.self;
		self.eventUI.accept.setDisabled(self.eventUI.eventName.text() == "");
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
		self.ui.action_Edit_Character.setEnabled(enableOrNot);
		
		# Remove Buttons
		self.ui.removePerson.setEnabled(enableOrNot);
		self.ui.action_Remove_Character.setEnabled(enableOrNot);
	# End of function

	def unlockSubmitCharacterBtn(this) -> None:
		self = this.self;
		self.characterUI.acceptForm.setDisabled(self.characterUI.firstName == "");
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
		
		match type:
			case "characters":
				for person in self.data[type]:
					title = this.titleConversion(person[3]);
					space = " " if(len(title) > 0) else "";
					newRow = table.count()
					table.insertItem(newRow, f"{title}{space}{person[1]} {person[2]}");
					if(person[7] == 1):
						table.item(newRow).setIcon(self.deathIcon);		# type: ignore
				# No Fallthrough
				
			case "world":
				for item in self.data[type]:
					newRow = table.count();
					table.insertItem(newRow, this.addLinebreaks(item[0]));
				# No Fallthrough
					
			case "relation":
				for relation in self._characterRelations:
				
					converted = this.relationTupleConversion(relation);
					if(not converted):
						continue; # The relationship came up empty (sounds just like my life)
					
					spaces = (self.settings["longestRelation"] - len(converted[1])) * " ";
					fullRelation = converted[1] + spaces + " | " + converted[0];
					
					newRow = table.count();
					table.insertItem(newRow, fullRelation);
				# No Fallthrough
				
			case "events":
				self.data["events"] = this.orderEventsChronologically();
				for evt in self.data["events"]:
				
					yearOfEvent = evt[0];
					monthOfEvent = evt[1];
					
					eventName = evt[3];
					eventDescription = evt[4];
					
					eventData = f"- Year {yearOfEvent}, Month {monthOfEvent}\n{eventName}\n\n{this.addLinebreaks(eventDescription)}\n\u200b";
					
					newRow = table.count();
					table.insertItem(newRow, eventData);
				
				# Add an extra row and and disable it
				# newRow = table.count()
				# table.insertItem(newRow, "");
				# it = table.item(newRow)
				# it.setFlags(Qt.NoItemFlags);
				# No Fallthrough
				
			case _: # Default Case
				return;

		table.setCurrentRow(prevRow);
	# End of function


	# Conversions
	def relationConversion(this, item: int | str) -> str:
		"""
		Function to convert a relationship to/from an int/ string

		Args:
			item (int | str): The item to be converted

		Returns:
			(str | int): The item in its converted state
		"""
		return relationDict[item];
	# End of function


	def titleConversion(this, item: int | str | None) -> str:
		"""
		Function to convert a title to/from an int/ string

		Args:
			item (int | str | None): The item to be converted

		Returns:
			(str | int): The item in its converted state
		"""
		if(item == None):
			item = 0;
		return titleDict[item];
	# End of function


	def maxRelationLength(this) -> int:
		maxValue = 0;
		for value in relationDict:
			item = relationDict[value];
			if(len(item) > maxValue):
				maxValue = len(item);
		
		return maxValue;
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
	# End of function
	
	
	def removeLinebreaks(this, text: str) -> str:
		"""
		Removes the weird Qt Formatting for linebreaks

		Args:
			text (str): The text to be fixed

		Returns:
			(str): The fixed text
		"""
		textArray = re.split("(\n|\r|\n\r|\r\n)", f"{text}");
		textArrayFixed = [];
		for item in textArray:
			if(item == "\n" or item == "\r" or item == "\n\r" or item == "\r\n"):
				continue;
			textArrayFixed.append(item);
		fixedText = "│".join(textArrayFixed);
		
		return fixedText;
	# End of function
	
	
	def addLinebreaks(this, text: str) -> str:
		"""
		Adds in correct linebreaks that were removed via removeLinebreaks

		Args:
			text (str): The text to be fixed

		Returns:
			(str): The fixed text
		"""
		textWithLinebreaks = text.replace("│", "\n");
		return textWithLinebreaks;
	# End of function
	
	
	def getNextID(this, type: str) -> int:
		self = this.self;
		if(len(self.data[type]) == 0):
			return 0;
		
		highestID = 0;
		for item in self.data[type]:
			if(item[0] > highestID):
				highestID = item[0];
		
		return highestID + 1;
	# End of function
		
	
	def orderEventsChronologically(this) -> list[tuple[int, int, int, str, str]]:
		self = this.self;
		events = self.data["events"];
		
		dateObject: dict[int, dict[int, list[tuple[int, int, int, str, str]]]];
		dateObject = {};
		
		for event in events:
			year = event[0];
			
			if(year not in dateObject):
				dateObject[year] = {};
			
			month = event[1];
			if(month not in dateObject[year]):
				dateObject[year][month] = [];
			
			dateObject[year][month].append(event);
			
		orderedEvents = [];
		
		sort = this._bubbleSort
		for year in sort(list(dateObject.keys())):
			for month in sort(list(dateObject[year].keys())):
				for item in dateObject[year][month]:
					orderedEvents.append(item);
		
		return orderedEvents;
	# End of function


	def _bubbleSort(this, array: list) -> list:
		for element in array:
			sorted = true;
			lastSort = 1;
				
			for i in range(len(array) - lastSort):

				itemA = array[i];
				itemB = array[i + 1];
				
				if(itemA <= itemB):
					continue;

				array[i] = itemB;
				array[i + 1] = itemA;
				
				if(sorted):
					sorted = false;
				
			if(sorted):
				break;
				
			lastSort += 1;
			
		return array;
	# End of function