_QLineEdit		= "QLineEdit {\n	background: rgb(255, 255, 255);\n	color: rgb(0, 0, 0);\n	border: 1px solid rgb(200, 200, 200);\n	border-radius:5px;\n	padding-left: 3px;\n	padding-right: 3px;\n}"
_QPushButton	= "QPushButton {\n    background: rgb(230, 230, 230);\n    color: rgb(0, 0, 0);\n}\n\nQPushButton:hover {\n	background: rgb(220, 220, 220);\n	color: rgb(0, 0, 0);\n}\n\nQPushButton:disabled {\n	background: rgb(240, 240, 240);\n	color: rgb(126, 126, 126);\n}"
_QTitleLabel	= 'QLabel {\n	background: transparent;\n	font: font "Fira Code";\n}'
_QListWidget	= "QListWidget{\n	color: rgb(0, 0, 0);\n	background: rgb(255, 255, 255);\n	border: 1px solid rgb(200, 200, 200);\n	border-radius:5px;\n	outline: 0;\n}\n\nQListWidget:item{\n	color: rgb(0, 0, 0);\n	padding: 3px;\n	border: 1px solid transparent;\n	border-radius: 5px;\n}\n\nQListWidget:item:hover{\n	padding-left: 3px;\n	padding-right: 3px;\n	background: rgb(250, 250, 250);\n	border: 1px solid rgb(210, 210, 210);\n}\n\nQListWidget:item:selected{\n	padding-left: 3px;\n	padding-right: 3px;\n	background: rgb(240, 240, 240);\n	border: 1px solid rgb(200, 200, 200);\n}"
_window			= "background: rgb(240, 240, 240);\ncolor: rgb(0, 0, 0);"


relationWindow	= _window
accept			= _QPushButton
cancel			= _QPushButton
characterList	= _QListWidget
label1			= _QTitleLabel
relationType	= _QListWidget
search			= _QLineEdit
searchRelation	= _QLineEdit