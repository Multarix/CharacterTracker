#	 ██████╗░██╗░░░██╗████████╗████████╗░█████╗░███╗░░██╗    ███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
#	 ██╔══██╗██║░░░██║╚══██╔══╝╚══██╔══╝██╔══██╗████╗░██║    ██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
#	 ██████╦╝██║░░░██║░░░██║░░░░░░██║░░░██║░░██║██╔██╗██║    █████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
#	 ██╔══██╗██║░░░██║░░░██║░░░░░░██║░░░██║░░██║██║╚████║    ██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
#	 ██████╦╝╚██████╔╝░░░██║░░░░░░██║░░░╚█████╔╝██║░╚███║    ██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
#	 ╚═════╝░░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░░╚════╝░╚═╝░░╚══╝    ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░
from __future__ import annotations			# Type hinting

import re

from PyQt5.QtWidgets import *				# type: ignore

from typehinting import startProgram, settingsLayout
from miscFunctions import miscFunctions

class buttonFunctions():
	def __init__(this, self: startProgram) -> None:
		this.self = self;
		this.functions = miscFunctions(self);
	
	# Character stuff
	def acceptCharacterBtn(this, newChar: bool):
		"""
		Function to run when the accept button is pressed on the editCharacterUI

		Args:
			newChar (bool): Whether a character is new or not
		"""
		self = this.self;
		ui = self.characterUI;
				
		charID = ui.characterID.value();
		if(newChar and len(self.data["characters"]) >=1):
			charID = self.data["characters"][-1][0] + 1;
				
		name = ui.firstName.text();
		lastName = ui.lastName.text();
		title = ui.titleSelector.currentIndex();
		age = ui.age.value();
		species = ui.species.text();
		
		# Because QT is fuckin weird with text boxes, we gonna fix it up
		infoArray = re.split("(\n|\r|\n\r|\r\n)", f"{ui.textEdit.toPlainText()}");
		infoArrayFixed = [];
		for item in infoArray:
			if(item == "\n" or item == "\r" or item == "\n\r" or item == "\r\n"):
				continue
			infoArrayFixed.append(item);
		info = "│".join(infoArrayFixed);

		
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
			self.data["characters"].append((int(charID), name, lastName, int(title), int(age), int(gender), species, int(isDead), info, relationString));
						
		else: # Not new character, find the character and overwrite it
			for i in range(len(self.data["characters"])):
				if(self.data["characters"][i][0] == charID):
					self.data["characters"][i] = (int(charID), name, lastName, int(title), int(age), int(gender), species, int(isDead), info, relationString);
					break;
		
		# Update the current list
		self.ui.characterList.clear();
		this.functions.populateList(self.ui.characterList, "characters");
		this.functions.searchBar(self.ui.characterSearch, self.ui.characterList);
	# End of function
	

	def removeCharacterBtn(this) -> None:
		"""
		Function to run when pressing the remove button on the mainWindowUI
		"""
		self = this.self;
		ui = self.ui;
		indexOfItem = ui.characterList.currentRow();
		ui.characterList.takeItem(ui.characterList.currentRow());
		del self.data["characters"][indexOfItem];

		this.functions.unlockEditRemoveCharacterBtns();
	# End of function
	

	# Relation stuff
	def addRelationToListBtn(this, existing: bool) -> None:
		"""
		Function to run when pressing the accept button on the addRelationUI
		"""
		self = this.self;
		
		# Person Information
		selectedPerson = self.addRelationUI.characterList.currentRow();
		personData = self.data["characters"][selectedPerson];
		
		# Relationship
		selectedRelation = self.addRelationUI.relationType.currentRow();
		relationship = this.functions.relationConversion(selectedRelation);
		spaces = (self.settings["longestRelation"] - len(relationship)) * " ";
		relationship = relationship + spaces +  " | ";
		
		if(existing):
			itemRow = self.characterUI.relationTable.currentRow();
			self._characterRelations[itemRow] = (personData[0], selectedRelation);
		else:
			# Add to the internal relationship list
			self._characterRelations.append((personData[0], selectedRelation));
			# Adding to the table
		
		self.characterUI.relationTable.clear();
		this.functions.populateList(self.characterUI.relationTable, "relation");
		self.addRelationWindow.close(); # Finally closing the UI
	# End of function
	

	def removeRelationBtn(this) -> None:
		"""
		Function to run when the remove button is pressed on the editCharacterUI
		"""
		self = this.self;
		currRow = self.characterUI.relationTable.currentRow();
		if(currRow > -1):
			self.characterUI.relationTable.takeItem(currRow);
			del self._characterRelations[currRow];
	# End of function
	

	# World Buidling Stuff
	def addWorldBuildingToListBtn(this, newDetail: bool) -> None:
		"""
		Function to run when clicking the accept button on the worldBuildingUI

		Args:
			newDetail (bool): Whether or not it's a new detail
		"""
		self = this.self;
	
		text = this.functions.removeLinebreaks(self.worldBuildingUI.textEditor.toPlainText());
		
		if(newDetail):
			self.data["world"].append((text, 0));
		else:
			itemRow = self.ui.worldBuildingList.currentRow();
			self.data["world"][itemRow] = (text, 0);
		
		self.ui.worldBuildingList.clear();
		this.functions.populateList(self.ui.worldBuildingList, "world");
		this.functions.searchBar(self.ui.worldBuildingSearch, self.ui.worldBuildingList);
		self.worldBuildingWindow.close();
	# End of function
	
	
	def removeWorldBuilding(this) -> None:
		"""
		Function to run when clicking the remove button on the mainWindowUI
		"""
		self = this.self;
		currRow = self.ui.worldBuildingList.currentRow();
		if(currRow > -1):
			self.ui.worldBuildingList.takeItem(currRow);
			del self.data["world"][currRow];
	# End of function
	
	
	def addEventToListBtn(this, newEvent: bool) -> None:
		"""
		Function to run when clicking the accept button on the eventUI

		Args:
			newEvent (bool): Whether or not it's a new event
		"""
		self = this.self;
		description = this.functions.removeLinebreaks(self.eventUI.textEditor.toPlainText());
		name = self.eventUI.eventName.text();
		yearOfEvent = self.eventUI.yearSpin.value();
		monthOfEvent = self.eventUI.monthSpin.value();
		onTimeline = 1 if(self.eventUI.addToTimeline.isChecked()) else 0;
		
		if(newEvent):
			self.data["events"].append((yearOfEvent, monthOfEvent, onTimeline, name, description));
		else:
			itemRow = self.ui.eventList.currentRow();
			self.data["events"][itemRow] = (yearOfEvent, monthOfEvent, onTimeline, name, description);
			
		self.ui.eventList.clear();
		this.functions.populateList(self.ui.eventList, "events");
		this.functions.searchBar(self.ui.eventSearch, self.ui.eventList);
		self.eventWindow.close();
	# End of function
	
	
	def removeEventBtn(this) -> None:
		"""
		Function to run when clicking the remove button on the mainWindowUI
		"""
		self = this.self;
		currRow = self.ui.eventList.currentRow();
		if(currRow > -1):
			self.ui.eventList.takeItem(currRow);
			del self.data["events"][currRow];
	# End of function
	
	
	def moveRow(this, upDown: int):
		"""
		Function to move a list item up or down

		Args:
			upDown (int): 1 for down, -1 for up
		"""
		self = this.self;
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
	# End of function
	
	
	def setConfig(this, globalSettings: list[tuple[str, int]], databaseSettings: settingsLayout):
		self = this.self;
		
		theme = self.settings["theme"];
		lang = self.settings["lang"];
		
		# Set the Global Settings
		for setting in globalSettings:
			self.settings[setting[0]] = setting[1];
		
		# If the theme changed, change the theme
		if(theme != self.settings["theme"]):
			self.themeManager.setTheme(self, "main");
			
		# Set the database settings
		self.data["settings"] = databaseSettings;
		
		self.ui.timelineSlider.setMaximum(self.data["settings"]["timelineLength"] * self.data["settings"]["timelineScale"]);
			
		# Close the window
		self.optionsWindow.close();
		this.functions.populateList(self.ui.characterList, "characters");