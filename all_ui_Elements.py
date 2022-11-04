#	 ██╗░░░██╗██╗    ███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
#	 ██║░░░██║██║    ██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
#	 ██║░░░██║██║    █████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
#	 ██║░░░██║██║    ██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
#	 ╚██████╔╝██║    ██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
#	 ░╚═════╝░╚═╝    ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░

from __future__ import annotations					# Type hinting

from typehinting import startProgram

from PyQt5 import QtWidgets
from PyQt5.QtGui import *							# type: ignore

from ui_editPersonWindow import Ui_editPersonWindow as editPersonWindow
from ui_addRelationWindow import Ui_addRelationWindow as addRelationWindow
from ui_worldBuildingWindow import Ui_worldBuildingWindow as worldBuildingWindow
from ui_optionsWindow import Ui_optionsWindow as optionsWindow
from ui_infoWindow import Ui_creditsWindow as creditsWindow
from ui_eventWindow import Ui_eventWindow as eventWindow

from miscFunctions import miscFunctions
from buttonFunctions import buttonFunctions

# Fixing python to not be shit
true = True;
false = False;


class windows():
	def __init__(this, self: startProgram) -> None:
		this.self = self;
		this.functions = miscFunctions(self);
		this.buttons = buttonFunctions(self);


	def openCreditsWindow(this) -> None:
		self = this.self;
		self.creditsWindow = QtWidgets.QWidget();
		self.creditsUI = creditsWindow();
		self.creditsUI.setupUi(self.creditsWindow);
		self.themeManager.setTheme(self, "credits");
		self.creditsWindow.show();
	# End of function
	
	
	def openOptionsWindow(this) -> None:
		self = this.self;
		self.optionsWindow = QtWidgets.QWidget();
		self.optionsUI = optionsWindow();
		self.optionsUI.setupUi(self.optionsWindow);
		self.themeManager.setTheme(self, "options");
		
		self.optionsUI.themeBox.setCurrentIndex(self.settings["theme"]);
		self.optionsUI.langBox.setCurrentIndex(self.settings["lang"]);
		self.optionsUI.timelineLength_spin.setValue(self.data["settings"]["timelineLength"]);
		self.optionsUI.timelineScale_spin.setValue(self.data["settings"]["timelineScale"]);
		self.optionsUI.startYear_spin.setValue(self.data["settings"]["startYear"]);
		
		self.optionsUI.accept.clicked.connect(lambda: this.buttons.setConfig([("theme", self.optionsUI.themeBox.currentIndex()), ("lang", self.optionsUI.langBox.currentIndex())], {"timelineLength": self.optionsUI.timelineLength_spin.value(), "timelineScale": self.optionsUI.timelineScale_spin.value(), "startYear": self.optionsUI.startYear_spin.value()}))
		self.optionsWindow.show();
	# End of function
	
	
	def openEditCharacterWindow(this, newChar: bool) -> None:
		"""
		Function to open the editCharacterUI when pressing the add or edit button on the mainWindowUI

		Args:
			newChar (bool): Whether a character is new or not
		"""
		self = this.self;
		self.editCharacterWindow = QtWidgets.QWidget();
		self.characterUI = editPersonWindow();
		self.characterUI.setupUi(self.editCharacterWindow);
		self.themeManager.setTheme(self, "person");
		self.characterUI.characterID.hide(); 				# People don't need to see this, it's only for data tracking purposes
		self.characterUI.birthOnTimeline.hide();			# Disabled for now
				
		self._characterRelations.clear();
		self.characterUI.genderSelector.currentIndexChanged.connect(this.functions.genderSelectorTitleChange);
		
		# Buttons
		# Add
		self.characterUI.addRelation.clicked.connect(lambda: this.openAddRelationWindow(false));
		
		# Edit
		self.characterUI.editRelation.clicked.connect(lambda: this.openAddRelationWindow(true));
		self.characterUI.relationTable.currentRowChanged.connect(this.functions.unlockEditRemoveRelationBtn)
		
		# Remove
		self.characterUI.removeRelation.clicked.connect(this.buttons.removeRelationBtn);
				
		# Accept
		self.characterUI.acceptForm.setDisabled(newChar);
		self.characterUI.firstName.textEdited.connect(this.functions.unlockSubmitCharacterBtn);
		self.characterUI.acceptForm.clicked.connect(lambda: this.buttons.acceptCharacterBtn(newChar));

		if(not newChar):
			currSelected = self.ui.characterList.currentRow();
			charData = self.data["characters"][currSelected];
			# id, firstName, lastName, title, age, gender (0=None, 1=Male, 2=Female), species, isdead (0=Alive), information, relations
			# 0   1          2         3      4    5                                  6        7                 8            9
			
			self.characterUI.characterID.setValue(charData[0]);								# ID
			self.characterUI.firstName.setText(charData[1]);								# First Name
			self.characterUI.lastName.setText(charData[2]);									# Last Name			# Title
			self.characterUI.age.setValue(charData[4]);										# Age
			self.characterUI.genderSelector.setCurrentIndex(charData[5]);					# Gender
			self.characterUI.species.setText(charData[6]);									# Species
			
			self.characterUI.titleSelector.setCurrentIndex(int(charData[3]));
			
			if(charData[7] == 1):
				self.characterUI.dead.setChecked(true);										# Is Dead
			
			charInfoArray = charData[8].split("│");
			charInfo = "\n".join(charInfoArray);
			self.characterUI.textEdit.setText(charInfo);									# Character Information

			relations = charData[9];
			if(relations):
				relationsArray = relations.split(", ");										# Each relationship is seperated by ", "
				
				for relation in relationsArray:
					rel = relation.split("|"); 												# Each side of the relation is seperated by a "|", rel[0] is the person, rel[1] is the type of relationship
					self._characterRelations.append((int(rel[0]), int(rel[1])));			# Add the item to the internal list, for later
				
				this.functions.populateList(self.characterUI.relationTable, "relation");	# Relations
		
		else:
			self.characterUI.characterID.setValue(this.functions.getNextID("characters"));
			
		self.editCharacterWindow.show();
	# End of function
	

	def openAddRelationWindow(this, existing: bool) -> None:
		"""
		Function to open the addRelationUI when pressing the add button on the editCharacterUI
		"""
		self = this.self;
		self.addRelationWindow = QtWidgets.QWidget();
		self.addRelationUI = addRelationWindow();
		self.addRelationUI.setupUi(self.addRelationWindow);
		self.themeManager.setTheme(self, "relation");
		
		this.functions.populateList(self.addRelationUI.characterList, "characters");
	
		# --Connections--
		self.addRelationUI.accept.clicked.connect(lambda: this.buttons.addRelationToListBtn(existing));
		self.addRelationUI.characterList.itemSelectionChanged.connect(this.functions.unlockAcceptRelationBtn);
		self.addRelationUI.relationType.itemSelectionChanged.connect(this.functions.unlockAcceptRelationBtn);
		
		# Search bars
		self.addRelationUI.search.textEdited.connect(lambda: this.functions.searchBar(self.addRelationUI.search, self.addRelationUI.characterList));
		self.addRelationUI.searchRelation.textEdited.connect(lambda: this.functions.searchBar(self.addRelationUI.searchRelation, self.addRelationUI.relationType));
		

		
		if(existing): # Existing relationship
			relationIndex = self.characterUI.relationTable.currentRow();
			relationship = self._characterRelations[relationIndex];
			personID = relationship[0];
			relationTypeIndex = relationship[1];
			
			for i in range(len(self.data["characters"])):
				person = self.data["characters"][i];
				if(personID == person[0]):
					self.addRelationUI.characterList.setCurrentRow(i);
					self.addRelationUI.relationType.setCurrentRow(relationTypeIndex);
					break;

		self.addRelationWindow.show();
	# End of function
	
	
	def openWorldBuildingWindow(this, newDetail: bool) -> None:
		self = this.self;
		self.worldBuildingWindow = QtWidgets.QWidget();
		self.worldBuildingUI = worldBuildingWindow();
		self.worldBuildingUI.setupUi(self.worldBuildingWindow);
		self.themeManager.setTheme(self, "world");
		
		# Accept button
		self.worldBuildingUI.accept.setDisabled(newDetail);
		self.worldBuildingUI.textEditor.textChanged.connect(this.functions.unlockWorldBuildingAcceptBtn);
		self.worldBuildingUI.accept.clicked.connect(lambda: this.buttons.addWorldBuildingToListBtn(newDetail));
		
		if(not newDetail):
			currRow = self.ui.worldBuildingList.currentRow();
					
			text = this.functions.addLinebreaks(self.data["world"][currRow][0]);
			self.worldBuildingUI.textEditor.setText(text);

		self.worldBuildingWindow.show();
	# End of function
	
	
	def openEventWindow(this, newDetail: bool) -> None:
		self = this.self;
		self.eventWindow = QtWidgets.QWidget();
		self.eventUI = eventWindow();
		self.eventUI.setupUi(self.eventWindow);
		self.themeManager.setTheme(self, "events");
		
		self.eventUI.addToTimeline.hide();				# Hide for now
		
		# Offsets
		settings = self.data["settings"];
		self.eventUI.yearSpin.setRange(settings["startYear"], settings["startYear"] + settings["timelineLength"]);
		self.eventUI.monthSpin.setMaximum(settings["timelineScale"]);
		
		# Accept button
		self.eventUI.accept.setDisabled(newDetail);
		self.eventUI.eventName.textChanged.connect(this.functions.unlockAddEventsAcceptBtn);
		self.eventUI.accept.clicked.connect(lambda: this.buttons.addEventToListBtn(newDetail));
		
		if(not newDetail):
			currRow = self.ui.eventList.currentRow();
			self.eventUI.yearSpin.setValue(self.data["events"][currRow][0]);
			self.eventUI.monthSpin.setValue(self.data["events"][currRow][1]);
			
			onTimeline = true if self.data["events"][currRow][2] == 1 else false;
			self.eventUI.addToTimeline.setChecked(onTimeline);
			
			self.eventUI.eventName.setText(self.data["events"][currRow][3]);
			
			text = this.functions.addLinebreaks(self.data["events"][currRow][4]);
			self.eventUI.textEditor.setText(text);
		
		self.eventWindow.show();
	# End of function