_QLineEdit		= "QLineEdit {\n	background: rgb(64, 68, 75);\n	color: rgb(255, 255, 255);\n	border: 1px solid rgb(50, 50, 50);\n	border-radius:5px;\n	padding-left: 3px;\n	padding-right: 3px;\n}"
_QPushButton	= "QPushButton {\n    background: rgb(64, 68, 75);\n    color: rgb(255, 255, 255);\n}\n\nQPushButton:hover {\n	background: rgb(79, 83, 89);\n	color: rgb(255, 255, 255);\n}\n\nQPushButton:disabled {\n	background: rgb(54, 57, 63);\n	color: rgb(126, 126, 126);\n}"
_QTitleLabel	= 'QLabel {\n	background: transparent;\n	font: font "Fira Code";\n}'
_QListWidget	= "QListWidget{\n	color: rgb(255, 255, 255);\n	background: rgb(64, 68, 75);\n	border: 1px solid rgb(50, 50, 50);\n	border-radius:5px;\n	outline: 0;\n}\n\nQListWidget:item{\n	color: rgb(255, 255, 255);\n	padding: 3px;\n	border: 1px solid transparent;\n	border-radius: 5px;\n}\n\nQListWidget:item:hover{\n	padding-left: 3px;\n	padding-right: 3px;\n	background: rgb(74, 76, 79);\n	border: 1px solid rgb(64, 66, 75);\n}\n\nQListWidget:item:selected{\n	padding-left: 3px;\n	padding-right: 3px;\n	background: rgb(93, 94, 97);\n	border: 1px solid rgb(74, 76, 79);\n}"
_QComboBox		= "QComboBox {\n	background: rgb(64, 68, 75);\n	border: 1px solid rgb(50, 50, 50);\n	border-radius:5px;\n	padding-left: 3px;\n}"
_QTextEdit		= "QTextEdit {\n	background: rgb(64, 68, 75);\n	color:rgb(255, 255, 255);\n	border: 1px solid rgb(50, 50, 50);\n	border-radius:5px;\n	padding: 3px;\n}"
_window			= "background: rgb(54, 57, 63);\ncolor: rgb(255, 255, 255);"



mainWindow			= _window
tabWidget			= "QTabWidget {\n	background: rgb(54, 57, 63);\n	color: rgb(255, 255, 255);\n}\n\nQTabWidget::tab-bar {\n	left: 305px;\n	top: 62px;\n}\n\nQTabBar::tab {\n	background: rgb(64, 68, 75);\n}\n\nQTabBar::tab:hover {\n	background: rgb(79, 83, 89);\n	color: rgb(255, 255, 255);\n}\n\nQTabBar::tab:selected {\n	background: rgb(89, 93, 99);\n	color: rgb(255, 255, 255);\n}"

addPerson			= _QPushButton
ageSlider			= "QSlider {\n	background: transparent;\n}"
ageSliderCount		= _QTitleLabel
characterList		= _QListWidget
characterSearch		= _QLineEdit
characterLabel		= _QTitleLabel
editPerson			= _QPushButton
moveDown			= _QPushButton
moveUp				= _QPushButton
removePerson		= _QPushButton
selectionDetails	= "QListWidget{\n	color: rgb(255, 255, 255);\n	background: rgb(64, 68, 75);\n	border: 1px solid rgb(50, 50, 50);\n	border-radius:5px;\n	outline: 0;\n}\n\nQListWidget:item{\n	padding: 3px;\n	background: rgb(64, 68, 75);\n}"

worldBuildingAdd	= _QPushButton
worldBuildingEdit	= _QPushButton
worldBuildingLabel	= _QTitleLabel
worldBuildingList	= "QListWidget{\n	color: rgb(255, 255, 255);\n	background: rgb(64, 68, 75);\n	border: 1px solid rgb(50, 50, 50);\n	border-radius:5px;\n	outline: 0;\n}\n\nQListWidget:item{\n	color: rgb(255, 255, 255);\n	padding-left: 3px;\n	padding-right: 3px;\n	border: 1px solid transparent;\n	padding-top: 5px;\n	padding-bottom: 5px;\n	border-radius: 5px;\n}\n\nQListWidget:item:hover{\n	background: rgb(74, 76, 79);\n	border: 1px solid rgb(64, 66, 75);\n}\n\nQListWidget:item:selected{\n	background: rgb(93, 94, 97);\n	border: 1px solid rgb(74, 76, 79);\n}"
worldBuildingRemove	= _QPushButton
worldBuildingSearch	= _QLineEdit

menubar 			= "QMenuBar {\n	background: rgb(41, 43, 47);\n	color: rgb(255, 255, 255);\n}\n\nQMenuBar::item {\n	background: rgb(41, 43, 47);\n	color: rgb(255, 255, 255);\n}\n\nQMenuBar::item:selected {\n	background: rgb(64, 68, 74);\n	color: rgb(255, 255, 255);\n}"
menubarTab 			= "QMenu {\n	background: rgb(41, 43, 47);\n	color: rgb(255, 255, 255);\n}\n\nQMenu::item {\n	background: rgb(41, 43, 47);\n	color: rgb(255, 255, 255);\n}\n\nQMenu::item:selected {\n	background: rgb(64, 68, 74);\n	color: rgb(255, 255, 255);\n}\n\nQMenu::item:disabled {\n	background: rgb(41, 43, 47);\n	color: rgb(126, 126, 126);\n}\n\nQMenu::separator {\n	color: rgb(0, 0, 0);\n	padding-top: 4px;\n}"