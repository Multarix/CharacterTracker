#	 ███████╗██╗██╗░░░░░███████╗  ███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗███╗░░░███╗███████╗███╗░░██╗████████╗
#	 ██╔════╝██║██║░░░░░██╔════╝  ████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝████╗░████║██╔════╝████╗░██║╚══██╔══╝
#	 █████╗░░██║██║░░░░░█████╗░░  ██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░
#	 ██╔══╝░░██║██║░░░░░██╔══╝░░  ██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░
#	 ██║░░░░░██║███████╗███████╗  ██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░
#	 ╚═╝░░░░░╚═╝╚══════╝╚══════╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░


from __future__ import annotations					# Type Hinting
from typehinting import startProgram, dataLayout	# Type Hinting

import sqlite3
import os

from PyQt5 import QtCore
from PyQt5.QtWidgets import *						# type: ignore

from miscFunctions import miscFunctions

# Fixing python to not be shit
true = True;
false = False;


class fileManager():
	def __init__(self, this: startProgram) -> None:
		self.this = this
		self.functions = miscFunctions(this);
		
		self._version = 2;
		self._fileName = None;
		
		self._database = None;
		
		self.data: dataLayout;
		self.data = {
			"characters": [],
			"world": [],
			"events": [],
			"settings": {
				"timelineLength": 10,
				"timelineScale": 1,
				"startYear": 2022,
			}
		};

	
	def new(self) -> None:
		this = self.this;

		# "Any unsaved changed will be lost, continue?"
		
		if(true):
			return
		
		# If yes, remove everything
		self._fileName = None;
		self._database = None;
		self.data = {
			"characters": [],
			"world": [],
			"events": [],
			"settings": {
				"timelineLength": 10,
				"timelineScale": 1,
				"startYear": 2022,
			}
		};
		this.data = this.data;
		
		this.ui.characterList.clear();
		this.ui.characterSearch.clear();
		this.ui.selectionDetails.clear();
		this.ui.worldBuildingList.clear();
		this.ui.worldBuildingSearch.clear();
		this._characterRelations.clear();
	# End of function
	
	
	def _saveAs(self) -> bool | str | int:
		"""
		Extra function to save a file with a specific filename

		Returns:
			bool | str: Returns false if there were no errors, otherwise returns the error code
		"""
		# Get the new save location
		fileLocation = QFileDialog.getSaveFileUrl(self.this, "Save File", QtCore.QUrl(""), "Character Tracker (*.chtr)", "Character Tracker (*.chtr)");	# type: ignore
		
		if(fileLocation[0].toString() != ''): # If the user clicked cancel/ closed the dialog
			fileLocation = fileLocation[0].toString();
		else:
			return 1;
		
		fileLocation = fileLocation.replace("file:///", ""); # Remove the file related weirdness from QT
		fileArray = fileLocation.split("/");
		fileName = fileArray.pop(); # Get the filename from the last item in the array
		pathToFile = "/".join(fileArray); # Rejoin the path to file
		filePath = os.path.join(pathToFile, fileName); # Get the OS's version of the path to the file
		
		errorCode = "SAV000"; # Error code for making directory
		try:
			if(not os.path.exists(pathToFile)): # If the path to the given directory doesn't exist
				os.makedirs(pathToFile); # We make the path a thing
			
			errorCode = "SAV001"; # Error code for creating/ opening/ saving file
			file = open(filePath, "w"); # Create or open a file
			file.write(""); # Overwrite everything in the file to be empty
			file.close(); # And then save it
			
			errorCode = "SQL000"; # Error code for connecting to the SQL
			self._database = sqlite3.connect(filePath); # Now we turn it into a database
			
			errorCode = "SQL001"; # Error code for creating the SQL Schema
			self._createSchema(); # And create the SQL Schema
			
			self._fileName = filePath; # Assuming nothing went wrong, we can now set our fileName variable
			return false; # Return false, cause there were no errors
		except:
			return errorCode; # Something went wrong, so we return the code
	# End of function
	
	
	def saveOrSaveAs(self, saveAs: bool, data: dataLayout) -> None:
		"""
		Saves the current file, or if there is no current file, it saves as a new file
		"""
		if(not self._database or not self._fileName or saveAs): # If the fileName has not been set, or saveAs is true
			errorCode = self._saveAs(); # We go through 'Save As'
			
			if(not errorCode):
				return self.save(data);

			if(errorCode == 1):
				return;
		
			print(f"An error occured: {errorCode})");
			return self._errorMessage(f"An error occured while saving the file (Error code: {errorCode})");
	
				
	def save(self, data: dataLayout) -> None:
		"""
		Function to save a file

		Args:
			saveAs (bool): Whether or not to call _saveAs()
			data (dataLayout): The data to save
		"""
		
		if(not self._fileName):
			return;

		self._database = sqlite3.connect(self._fileName);
		
		print("Saving Changes...");
		errorCode = "SAV102"; # Error code for record deletion
		
		self._deleteRecords(); # Delete everything from the database
		
		errorCode = "SAV103"; # Error code for post deletion, pre character data - if you get this your data is probably fucked
		try:
			sql = self._database.cursor();
			for person in data["characters"]:
				sql.execute("INSERT INTO characters (id, firstName, lastName, title, age, gender, species, isdead, information, relationships) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", person);
				self._database.commit();
			
			errorCode = "SAV104"; # Error code for post character data, pre world data
			for worldItem in data["world"]:
				sql.execute("INSERT INTO worldBuilding (text, notUsed) VALUES (?, ?)", worldItem);
				self._database.commit();
			
			errorCode = "SAV105"; # Error code for post world data, pre event data
			for eventItem in data["events"]:
				sql.execute("INSERT INTO events (yearOfEvent, monthOfEvent, onTimeline, eventName, eventDescription) VALUES (?, ?, ?, ?, ?)", eventItem);
				self._database.commit();
			
			errorCode = "SAV106"; # Error code for post event data, pre config data
			configData = (data["settings"]["timelineLength"], data["settings"]["timelineScale"], data["settings"]["startYear"]);
			sql.execute(f"UPDATE config SET timelineLength = ?, timelineScale = ?, startYear = ?", configData);
			
			return print("Save Complete!"); # Console message for saving success
		except:
			print(f"An error occured: {errorCode}");
			return self._errorMessage(f"An error occured while saving the file (Error code: {errorCode})");
	# End of function


	def _deleteRecords(self) -> None:
		if(not self._database):
			return;

		try:
			sql = self._database.cursor();
			sql.execute("DELETE FROM characters");
			self._database.commit();
			
			sql.execute("DELETE FROM worldBuilding");
			self._database.commit();
			
			sql.execute("DELETE FROM events");
			self._database.commit();
		except:
			self._errorMessage("An error occured while saving the file (Error code: SAV000)"); # Error Code for during deleting data
	# End of function
	

	def open(self) -> None:
		"""
		Opens an sqlite database

		Args:
			file (str): The URL to the file
		"""
		this = self.this;
		fileName = QFileDialog.getOpenFileName(this, "Choose File", "", "Character Tracker (*.chtr);;All Files (*)")[0];	# type: ignore
		
		if(not fileName): # If the user clicked cancel/ closed the dialog
			return;
		
		code = "OPN000"; # Not valid SQL
		try:
			self._database = sqlite3.connect(fileName);
			sql = self._database.cursor();
			
			code = "OPN001"; # Cannot find the version
			versionData = None;
			
			sql.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="version"');
			table = sql.fetchall();
			
			tableName = table[0][0] if(table) else "config";
			sql.execute(f"SELECT * FROM {tableName}");
			
			versionData = sql.fetchall();
			
			if(not versionData or versionData[0][0] != self._version):
				self._updateSchema(versionData[0][0]);
			
			code = "OPN002"; # No characters table
			sql.execute("SELECT * FROM characters");
			self.data["characters"] = sql.fetchall();
			# self.functions.populateList(this.ui.characterList, "characters");
			
			code = "OPN003"; # No worldbuilding table
			sql.execute("SELECT * FROM worldBuilding");
			self.data["world"] =  sql.fetchall();
			# self.functions.populateList(this.ui.worldBuildingList, "world");
			
			code = "OPN004"; # No events table
			sql.execute("SELECT * FROM events");
			self.data["events"] =  sql.fetchall();
			# self.functions.populateList(this.ui.eventsList, "events");
			
			code = "OPN005"; # No config table... honestly how tf did you get this error?
			sql.execute("SELECT * FROM config");
			configData = sql.fetchall();
			configData = configData[0];
			self.data["settings"] = {
				"timelineLength": configData[1],
				"timelineScale": configData[2],
				"startYear": configData[3]
			}
			
			self._fileName = fileName;
		except:
			self._errorMessage(f"An error occured while opening the file (Error code: {code}");
		
		this.data = self.data;
		self.functions.populateList(this.ui.characterList, "characters");
		self.functions.populateList(this.ui.worldBuildingList, "world");
		self.functions.populateList(this.ui.eventList, "events");
		self.this.ui.timelineSlider.setMaximum(self.data["settings"]["timelineLength"] * self.data["settings"]["timelineScale"]);
	# End of function
		

	def _createSchema(self) -> None:
		"""
		Creates the tables required in the sql spreadsheet
		"""
		if(not self._database):
			return;
		
		# Data storage
		sql = self._database.cursor();
		sql.execute('CREATE TABLE "characters" ("id" INTEGER, "firstName" TEXT, "lastName" TEXT, "title" INTEGER, "age" INTEGER, "gender" INTEGER, "species" TEXT, "isdead" INTEGER, "information" TEXT, "relationships" TEXT)');
		self._database.commit();
		
		sql.execute('CREATE TABLE "worldBuilding" ("text" TEXT, "notUsed" INTEGER);');
		self._database.commit();
		
		self._v2Schema();
	# End of function
	

	def _v2Schema(self) -> None:
		"""
		Adds data relevant to version 2 of the schema
		"""
		if(not self._database):
			return;

		sql = self._database.cursor();
		
		# Create config and events
		sql.execute('CREATE TABLE "config" ("version" INTEGER, "timelineLength" INTEGER, "timelineScale" INTEGER, "startYear" INTEGER)');
		self._database.commit();
		
		sql.execute('CREATE TABLE "events" ("yearOfEvent" INTEGER, "monthOfEvent" INTEGER, "onTimeline" INTEGER, "eventName" TEXT, "eventDescription" TEXT)');
		self._database.commit();
		
		defaultSettings = (2, 10, 12, 2000);	# (Version, timelineLength, monthsPerYear, startYear)
		sql.execute('INSERT INTO config (version, timelineLength, timelineScale, startYear) VALUES (?, ?, ?, ?)', defaultSettings);
		self._database.commit();
	# End of function


	def _updateSchema(self, version) -> None:
		"""
		Update the database to the latest format

		Args:
			version (str | int): The version of the database
		"""
		
		if(not self._database):
			return;
		
		if(version == "1.1"):
			sql = self._database.cursor();
			
			sql.execute('DROP TABLE version');
			self._database.commit();
			
			# Move character data to a new table format
			sql.execute('SELECT * FROM characters');
			oldDataFormat = sql.fetchall();
		
			sql.execute('DROP TABLE characters');
			self._database.commit();
			sql.execute('CREATE TABLE "characters" ("id" INTEGER, "firstName" TEXT, "lastName" TEXT, "title" INTEGER, "age" INTEGER, "gender" INTEGER, "species" TEXT, "isdead" INTEGER, "information" TEXT, "relationships" TEXT)');
			self._database.commit();
		
			for character in oldDataFormat:
				sql.execute('INSERT INTO characters (id, firstName, lastName, title, age, gender, species, isdead, information, relationships) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (character[0], character[1], "", character[2], character[3], character[4], character[5], character[6], character[7], character[8]));
				self._database.commit();
			
			self._v2Schema();

	# End of function
	
	

	def _errorMessage(self, message: str) -> None:
		QMessageBox.critical(self.this, "Error", message);	# type: ignore
	# End of function