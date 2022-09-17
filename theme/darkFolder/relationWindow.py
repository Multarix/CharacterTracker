_QLineEdit		= "QLineEdit {\n	background: rgb(64, 68, 75);\n	color: rgb(255, 255, 255);\n	border: 1px solid rgb(50, 50, 50);\n	border-radius:5px;\n	padding-left: 3px;\n	padding-right: 3px;\n}"
_QPushButton	= "QPushButton {\n    background: rgb(64, 68, 75);\n    color: rgb(255, 255, 255);\n}\n\nQPushButton:hover {\n	background: rgb(79, 83, 89);\n	color: rgb(255, 255, 255);\n}\n\nQPushButton:disabled {\n	background: rgb(54, 57, 63);\n	color: rgb(126, 126, 126);\n}"
_QTitleLabel	= 'QLabel {\n	background: transparent;\n	font: font "Fira Code";\n}'
_QListWidget	= "QListWidget{\n	color: rgb(255, 255, 255);\n	background: rgb(64, 68, 75);\n	border: 1px solid rgb(50, 50, 50);\n	border-radius:5px;\n	outline: 0;\n}\n\nQListWidget:item{\n	color: rgb(255, 255, 255);\n	padding: 3px;\n	border: 1px solid transparent;\n	border-radius: 5px;\n}\n\nQListWidget:item:hover{\n	padding-left: 3px;\n	padding-right: 3px;\n	background: rgb(74, 76, 79);\n	border: 1px solid rgb(64, 66, 75);\n}\n\nQListWidget:item:selected{\n	padding-left: 3px;\n	padding-right: 3px;\n	background: rgb(93, 94, 97);\n	border: 1px solid rgb(74, 76, 79);\n}"
_window			= "background: rgb(54, 57, 63);\ncolor: rgb(255, 255, 255);"


relationWindow	= _window
accept			= _QPushButton
cancel			= _QPushButton
characterList	= _QListWidget
label1			= _QTitleLabel
relationType	= _QListWidget
search			= _QLineEdit
searchRelation	= _QLineEdit