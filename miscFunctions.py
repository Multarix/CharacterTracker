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
	"0" : "Father",
	"1" : "Mother",
	"2" : "Son",
	"3" : "Daughter",
	"4" : "Brother",
	"5" : "Sister",
	"6" : "Uncle",
	"7" : "Aunt",
	"8" : "Nephew",
	"9" : "Niece",
	"10": "Boyfriend",
	"11": "Girlfriend",
	"12": "Fiancé",
	"13": "Husband",
	"14": "Wife"
}

titleDict = {
	"Male": {
		"0": "",
		"1": "Mr",
		"2": "Sir",
		"3": "Lord",
		"4": "Baronet",
		"5": "Baron",
		"6": "Viscount",
		"7": "Earl",
		"8": "Count",
		"9": "Marquess",
		"10": "Duke",
		"11": "Prince",
		"12": "King",
		"13": "Emperor",
		"14": "God"
	},
	
	"Female": {
		"0": "",
		"1": "Ms",
		"2": "Miss",
		"3": "Mrs",
		"4": "Madam",
		"5": "Lady",
		"6": "Baronetess",
		"7": "Baroness",
		"8": "Viscountess",
		"9": "Countess",
		"10": "Marchioness",
		"11": "Duchess",
		"12": "Princess",
		"13": "Queen",
		"14": "Empress",
		"15": "Goddess"
	},
	
	"None": {
		"0": "",					# Both
		"1": "Mr",					# Male
		"2": "Ms",					# Female
		"3": "Miss",				# Female
		"4": "Mrs",					# Female
		"5": "Sir",					# Male
		"6": "Madam",				# Female
		"7": "Lord",				# Male
		"8": "Lady",				# Female
		"9": "Baronet",				# Male
		"10": "Baronetess",			# Female
		"11": "Baron",				# Male
		"12": "Baroness",			# Female
		"13": "Viscount",			# Male
		"14": "Viscountess",		# Female
		"15": "Earl",				# Male
		"16": "Count",				# Male
		"17": "Countess",			# Female
		"18": "Marquess",			# Male
		"19": "Marchioness",		# Female
		"20": "Duke",				# Male
		"21": "Duchess",			# Female
		"22": "Prince",				# Male
		"23": "Princess",			# Female
		"24": "King",				# Male
		"25": "Queen",				# Female
		"26": "Emperor",			# Male
		"27": "Empress",			# Female
		"28": "God",				# Male
		"29": "Goddess"				# Female
	},
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
	
	
	def charListSelectionChange(this) -> None:
		this.showDetails();
		this.unlockEditRemoveCharacterBtns();
	
	def showDetails(this) -> None:
		self = this.self;
		self.ui.selectionDetails.clear();
		
		if(self.ui.characterList.currentRow() > -1):
			
			if(self.ui.characterList.currentRow() > len(self.data["characters"])):
				return;
				
			person = self.data["characters"][self.ui.characterList.currentRow()];
	
			gender = this._getGender(person[5]);
				
			title = this.titleConversion(gender, person[3]);
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
					
					gender = this._getGender(person[5]);
						
					title = this.titleConversion(gender, person[3]);
					space = " " if(len(title) > 0) else "";
					newRow = table.count()
					table.insertItem(newRow, f"{title}{space}{person[1]} {person[2]}");
					if(person[7] == 1):
						table.item(newRow).setIcon(self.deathIcon);		# type: ignore
					else:
						table.item(newRow).setIcon(self.aliveIcon);		# type: ignore
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

		table.setCurrentRow(-1);

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
		return relationDict[str(item)];
	# End of function


	def titleConversion(this, gender: str,  item: int | str | None) -> str:
		"""
		Function to convert a title to/from an int/ string

		Args:
			item (int | str | None): The item to be converted

		Returns:
			(str | int): The item in its converted state
		"""
		if(item == None):
			item = "0";
		return titleDict[gender][str(item)];
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
	
	
	def genderSelectorTitleChange(this) -> None:
		self = this.self;
		genderIndex = self.characterUI.genderSelector.currentIndex();
		
		self.characterUI.titleSelector.clear()
		gender = this._getGender(genderIndex);
		
		# Add the appropriate rows
		self.characterUI.titleSelector.addItem("(None)");
		for item in titleDict[gender]:
			if(item == "0"):
				continue;
			self.characterUI.titleSelector.addItem(titleDict[gender][item]);
		
		self.characterUI.titleSelector.setCurrentIndex(0);
	# End of function


	def _getGender(this, g: str | int) -> str:
		gender = "None";
		if(f"{g}" == "1"):
			gender = "Male";
		elif (f"{g}" == "2"):
			gender = "Female";
		
		return gender;
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