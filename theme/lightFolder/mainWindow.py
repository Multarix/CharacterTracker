_QLineEdit		= "QLineEdit {\n	background: rgb(255, 255, 255);\n	color: rgb(0, 0, 0);\n	border: 1px solid rgb(200, 200, 200);\n	border-radius:5px;\n	padding-left: 3px;\n	padding-right: 3px;\n}"
_QPushButton	= "QPushButton {\n    background: rgb(230, 230, 230);\n    color: rgb(0, 0, 0);\n}\n\nQPushButton:hover {\n	background: rgb(220, 220, 220);\n	color: rgb(0, 0, 0);\n}\n\nQPushButton:disabled {\n	background: rgb(240, 240, 240);\n	color: rgb(126, 126, 126);\n}"
_QTitleLabel	= 'QLabel {\n	background: transparent;\n	font: font "Fira Code";\n}'
_QListWidget	= "QListWidget{\n	color: rgb(0, 0, 0);\n	background: rgb(255, 255, 255);\n	border: 1px solid rgb(200, 200, 200);\n	border-radius:5px;\n	outline: 0;\n}\n\nQListWidget:item{\n	color: rgb(0, 0, 0);\n	padding: 3px;\n	border: 1px solid transparent;\n	border-radius: 5px;\n}\n\nQListWidget:item:hover{\n	padding-left: 3px;\n	padding-right: 3px;\n	background: rgb(250, 250, 250);\n	border: 1px solid rgb(210, 210, 210);\n}\n\nQListWidget:item:selected{\n	padding-left: 3px;\n	padding-right: 3px;\n	background: rgb(240, 240, 240);\n	border: 1px solid rgb(200, 200, 200);\n}"
_QComboBox		= "QComboBox {\n	background: rgb(255, 255, 255);\n	border: 1px solid rgb(200, 200, 200);\n	border-radius:5px;\n	padding-left: 3px;\n}"
_QTextEdit		= "QTextEdit {\n	background: rgb(255, 255, 255);\n	color:rgb(0, 0, 0);\n	border: 1px solid rgb(200, 200, 200);\n	border-radius:5px;\n	padding: 3px;\n}"
_window			= "background: rgb(240, 240, 240);\ncolor: rgb(0, 0, 0);"


mainWindow			= _window
tabWidget			= "QTabWidget {\n	background: rgb(240, 240, 240);\n	color: rgb(0, 0, 0);\n}\n\nQTabWidget::tab-bar {\n	left: 305px;\n	top: 62px;\n}\n\nQTabBar::tab {\n	background: rgb(230, 230, 230);\n}\n\nQTabBar::tab:hover {\n	background: rgb(220, 220, 220);\n	color: rgb(0, 0, 0);\n}\n\nQTabBar::tab:selected {\n	background: rgb(210, 210, 210);\n	color: rgb(0, 0, 0);\n}"

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
selectionDetails	= "QListWidget{\n	color: rgb(0, 0, 0);\n	background: rgb(255, 255, 255);\n	border: 1px solid rgb(200, 200, 200);\n	border-radius:5px;\n	outline: 0;\n}\n\nQListWidget:item{\n	padding: 3px;\n	background: rgb(255, 255, 255);\n}"

worldBuildingAdd	= _QPushButton
worldBuildingEdit	= _QPushButton
worldBuildingLabel	= _QTitleLabel
worldBuildingList	= "QListWidget {\n	color: rgb(0, 0, 0);\n	background: rgb(255, 255, 255);\n	border: 1px solid rgb(200, 200, 200);\n	border-radius: 5px;\n	outline: 0;\n}\n\nQListWidget:item {\n	color: rgb(0, 0, 0);\n	padding-left: 3px;\n	padding-right: 3px;\n	border: 1px solid transparent;\n	padding-top: 5px;\n	padding-bottom: 5px;\n	border-radius: 5px;\n}\n\nQListWidget:item:hover {\n	background: rgb(250, 250, 250);\n	border: 1px solid rgb(210, 210, 210);\n}\n\nQListWidget:item:selected {\n	background: rgb(240, 240, 240);\n	border: 1px solid rgb(200, 200, 200);\n}"
worldBuildingRemove	= _QPushButton
worldBuildingSearch	= _QLineEdit

menubar 			= "QMenuBar {\n	background: rgb(255, 255, 255);\n	color: rgb(0, 0, 0);\n}\n\nQMenuBar::item {\n	background: rgb(255, 255, 255);\n	color: rgb(0, 0, 0);\n}\n\nQMenuBar::item:selected {\n	background: rgb(230, 230, 230);\n	color: rgb(0, 0, 0);\n}"
menubarTab 			= "QMenu {\n	background: rgb(240, 240, 240);\n	color: rgb(0, 0, 0);\n}\n\nQMenu::item {\n	background: rgb(240, 240, 240);\n	color: rgb(0, 0, 0);\n}\n\nQMenu::item:selected {\n	background: rgb(220, 220, 220);\n	color: rgb(0, 0, 0);\n}\n\nQMenu::item:disabled {\n	background: rgb(240, 240, 240);\n	color: rgb(126, 126, 126);\n}\n\nQMenu::separator {\n	color: rgb(0, 0, 0);\n	padding-top: 4px;\n}"