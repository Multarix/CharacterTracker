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
from PyQt5.QtWidgets import *


# Fixing python to not be shit
true = True;
false = False;


class fileManager():
	def __init__(self, ui) -> None:
		self._version = "1.1";
		self._fileName = None;
		self._database = None;
		
		self.data: dataLayout;
		self.data = {
			"characters": [],
			"world": []
		};

	
	def new(self) -> None:
		# Gonna just wipe everything, close window and re-open?
		# Also ask to confirm
		pass
	# End of function
	
	
	def _saveAs(self, ui: startProgram) -> bool | str:
		"""
		Extra function to save a file with a specific filename

		Returns:
			bool | str: Returns false if there were no errors, otherwise returns the error code
		"""
		# Get the new save location
		fileLocation = QFileDialog.getSaveFileUrl(ui, "Save File", QtCore.QUrl(""), "Character Tracker (*.chtr)", "Character Tracker (*.chtr)");
		
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
			
			self._fielName = filePath; # Assuming nothing went wrong, we can now set our fileName variable
			return false; # Return false, cause there were no errors
		except:
			return errorCode; # Something went wrong, so we return the code
	# End of function
	
				
	def save(self, ui: startProgram, saveAs: bool, data: dataLayout) -> None:
		"""
		Function to save a file

		Args:
			saveAs (bool): Whether or not to call _saveAs()
			data (dataLayout): The data to save
		"""
		
		if(not self._fileName or saveAs): # If the fileName has not been set, or saveAs is true
			errorCode = self._saveAs(ui); # We go through 'Save As'
			
			if(errorCode): # If there was an error
				if(errorCode == 1):
					return;
				else:
					print(f"An error occured: {errorCode})");
					return self._errorMessage(ui, f"An error occured while saving the file (Error code: {errorCode})");
		
		print("Saving Changes...");
		errorCode = "SAV102" # Error code for record deletion
		self._deleteRecords(ui); # Delete everything from our database
		
		errorCode = "SAV103"; # Error code for post deletion, pre character data - if you get this your data is fucked
		try:
			for person in data["characters"]:
				sql = self._database.cursor();
				sql.execute("INSERT INTO characters (id, name, title, age, gender, species, isdead, information, relationships) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", person);
				self._database.commit();
			
			errorCode = "SAV104"; # Error code for post character data, pre world data
			for worldItem in data["world"]:
				sql = self._database.cursor();
				sql.execute("INSERT INTO worldBuilding (text, notUsed) VALUES (?, ?)", worldItem);
				self._database.commit();
			
			return print("Save Complete!"); # Console message for saving success
		except:
			print(f"An error occured: {errorCode})");
			return self._errorMessage(ui, f"An error occured while saving the file (Error code: {errorCode})");	
	# End of function


	def _deleteRecords(self, ui: startProgram) -> None:
		try:
			sql = self._database.cursor();
			sql.execute("DELETE FROM characters");
			self._database.commit();
			
			sql.execute("DELETE FROM worldBuilding");
			self._database.commit();
		except:
			self._errorMessage(ui, "An error occured while saving the file (Error code: SAV000)"); # Error Code for during deleting data
	# End of function
	

	def open(self, ui: startProgram):
		"""
		Opens an sqlite database

		Args:
			file (str): The URL to the file
		"""
		fileName = QFileDialog.getOpenFileName(ui, "Choose File", "", "Character Tracker (*.chtr);;All Files (*)")[0];
		
		if(not fileName): # If the user clicked cancel/ closed the dialog
			return;
		
		code = "OPN000"; # Not valid SQL
		try:
			self._database = sqlite3.connect(fileName);
			sql = self._database.cursor();
			
			code = "OPN001"; # No version table
			sql.execute("SELECT * from version");
			versionData = sql.fetchall();
			if(versionData[0][0] < self._version):
				self._updateSchema()
			
			code = "OPN002"; # No characters table
			sql.execute("SELECT * FROM characters");
			self.data["characters"] = sql.fetchall();
			# self.populateList(self.ui.characterList, "characters"); # This won't work here
			
			code = "OPN003"; # No worldbuilding table
			sql.execute("SELECT * FROM worldBuilding");
			self.data["world"] =  sql.fetchall();
			# self.populateList(self.ui.worldBuildingList, "world"); # This won't work here
			
			self._fielName = fileName;
		except:
			self._errorMessage(ui, f"An error occured while opening the file (Error code: {code}");
	# End of function
		

	def _createSchema(self):
		"""
		Creates the tables required in the sql spreadsheet
		"""
		if(not self._database):
			return;
		
		# Data storage
		sql = self._database.cursor();
		sql.execute('CREATE TABLE "characters" ("id" INTEGER, "name" TEXT, "title" INTEGER, "age" INTEGER, "gender" INTEGER, "species" TEXT, "isdead" INTEGER, "information" TEXT, "relationships" TEXT)');
		self._database.commit();
		
		sql.execute('CREATE TABLE "worldBuilding" ("text" TEXT, "notUsed" INTEGER);');
		self._database.commit();
		
		# Versioning control system
		sql.execute('CREATE TABLE "version" ("currentVersion TEXT, "notUsed", INTEGER)');
		self._database.commit();
		sql.execute('INSERT INTO version (currentVersion, notUsed) VALUES (?, ?)', (self._version, 0));
		self._database.commit();
	# End of function
	

	def _updateSchema(self):
		pass;
	# End of function


	def _errorMessage(self, ui: startProgram, message: str):
		QMessageBox.critical(ui, "Error", message);
	# End of function
