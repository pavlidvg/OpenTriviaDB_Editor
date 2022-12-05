from PyQt5 import QtCore, QtGui, QtWidgets
import Editor


class Ui_MainWindow(object):

#should not ever be needed
    def add_question_ui(self,button):

        layout = self.frame.layout()

        layout_length = len(layout)
        #
        new_button = QtWidgets.QPushButton(self.frame)


        new_button.setStyleSheet("height: 50%\n"
                                          "")
        layout.insertWidget(layout_length-1,new_button)
        print("added widget:through ui)")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 784)
        self.main_layout = QtWidgets.QWidget(MainWindow)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_layout)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.QList_frame = QtWidgets.QFrame(self.main_layout)
        self.QList_frame.setStyleSheet("\n"
"background-color:rgba(217, 217, 217, 1);")
        self.QList_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.QList_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.QList_frame.setObjectName("QList_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.QList_frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(95, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.newButtton = QtWidgets.QPushButton(self.QList_frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.newButtton.setFont(font)
        self.newButtton.setStyleSheet("background-color: rgb(72, 96, 143);\n"
"color: rgb(255, 255, 255);\n"
"height:35px;\n"
"width:120px;\n"
"margin-top:5px;\n"
"/* new round stuff,copy pasted*/\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"")
        self.newButtton.setObjectName("newButtton")
        #self.newButtton.clicked.connect(self.add_question_ui)

        self.gridLayout.addWidget(self.newButtton, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.QList_frame)
        self.frame.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")

        spacerItem1 = QtWidgets.QSpacerItem(20, 606, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 2)
        self.horizontalLayout.addWidget(self.QList_frame)
        self.Editor_Frame = QtWidgets.QFrame(self.main_layout)
        self.Editor_Frame.setStyleSheet("\n"
"background-color: rgb(47, 49, 54);\n"
"height:50px;")
        self.Editor_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Editor_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Editor_Frame.setObjectName("Editor_Frame")
        self.grid_Trivia_edit = QtWidgets.QGridLayout(self.Editor_Frame)
        self.grid_Trivia_edit.setContentsMargins(-1, 50, -1, 20)
        self.grid_Trivia_edit.setObjectName("grid_Trivia_edit")
        self.incorrect_label = QtWidgets.QLabel(self.Editor_Frame)
        self.incorrect_label.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.incorrect_label.setFont(font)
        self.incorrect_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.incorrect_label.setTextFormat(QtCore.Qt.RichText)
        self.incorrect_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.incorrect_label.setWordWrap(True)
        self.incorrect_label.setObjectName("incorrect_label")
        self.grid_Trivia_edit.addWidget(self.incorrect_label, 5, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.Editor_Frame)
        self.textEdit.setStyleSheet("background-color: rgba(223, 222, 222, 1);\n"
"padding: 8px 5px;\n"
"/* new round stuff,copy pasted*/\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.grid_Trivia_edit.addWidget(self.textEdit, 5, 1, 1, 1)
        self.diff_label = QtWidgets.QLabel(self.Editor_Frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.diff_label.setFont(font)
        self.diff_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.diff_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.diff_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.diff_label.setObjectName("diff_label")
        self.grid_Trivia_edit.addWidget(self.diff_label, 2, 0, 1, 1)
        self.correct_label = QtWidgets.QLabel(self.Editor_Frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.correct_label.setFont(font)
        self.correct_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding: 8px 5px;\n"
"  margin: 15px 0;")
        self.correct_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.correct_label.setObjectName("correct_label")
        self.grid_Trivia_edit.addWidget(self.correct_label, 4, 0, 1, 1)
        self.category_input = QtWidgets.QLineEdit(self.Editor_Frame)
        self.category_input.setStyleSheet("background-color: rgba(223, 222, 222, 1);\n"
"padding: 8px 5px;\n"
"  margin: 15px 0;\n"
"  box-sizing: border-box;\n"
"/* new round stuff,copy pasted*/\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"")
        self.category_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.category_input.setObjectName("category_input")
        self.grid_Trivia_edit.addWidget(self.category_input, 3, 1, 1, 1)
        self.category_label = QtWidgets.QLabel(self.Editor_Frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.category_label.setFont(font)
        self.category_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding: 8px 5px;\n"
"  margin: 15px 0;")
        self.category_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.category_label.setObjectName("category_label")
        self.grid_Trivia_edit.addWidget(self.category_label, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.Editor_Frame)
        self.lineEdit_4.setStyleSheet("background-color: rgba(223, 222, 222, 1);\n"
"padding: 8px 5px;\n"
"  margin: 15px 0;\n"
"  box-sizing: border-box;\n"
"/* new round stuff,copy pasted*/\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.grid_Trivia_edit.addWidget(self.lineEdit_4, 4, 1, 1, 1)
        self.Question_label = QtWidgets.QLineEdit(self.Editor_Frame)
        self.Question_label.setEnabled(True)
        self.Question_label.setStyleSheet("background-color: rgba(223, 222, 222, 1);\n"
"padding: 8px 5px;\n"
"  margin: 40px 0;\n"
"  box-sizing: border-box;\n"
"\n"
"/* new round stuff,copy pasted*/\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"\n"
"")
        self.Question_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Question_label.setObjectName("Question_label")
        self.grid_Trivia_edit.addWidget(self.Question_label, 1, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.Editor_Frame)
        self.comboBox.setStyleSheet("background-color: rgba(223, 222, 222, 1);\n"
"height:33px;\n"
"  margin: 8px 0;\n"
"  /* new round stuff,copy pasted*/\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"")
        self.comboBox.setIconSize(QtCore.QSize(20, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.grid_Trivia_edit.addWidget(self.comboBox, 2, 1, 1, 1)
        self.title_label_2 = QtWidgets.QLabel(self.Editor_Frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.title_label_2.setFont(font)
        self.title_label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.title_label_2.setObjectName("title_label_2")
        self.grid_Trivia_edit.addWidget(self.title_label_2, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.title_label = QtWidgets.QLabel(self.Editor_Frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding: 8px 5px;\n"
"  margin: 25px 0;")
        self.title_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.title_label.setObjectName("title_label")
        self.grid_Trivia_edit.addWidget(self.title_label, 1, 0, 1, 1)
        self.EditButton = QtWidgets.QPushButton(self.Editor_Frame)
        self.EditButton.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.EditButton.setFont(font)
        self.EditButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.EditButton.setStyleSheet("background-color: rgb(72, 96, 143);\n"
"color: rgb(255, 255, 255);\n"
"/* new round stuff,copy pasted*/\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"")
        self.EditButton.setObjectName("EditButton")
        self.grid_Trivia_edit.addWidget(self.EditButton, 6, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.grid_Trivia_edit.addItem(spacerItem2, 1, 2, 1, 1)
        self.delete_button = QtWidgets.QPushButton(self.Editor_Frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet("background-color: rgb(72, 96, 143);\n"
"color: rgb(255, 255, 255);\n"
"/* new round stuff,copy pasted*/\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"")
        self.delete_button.setObjectName("delete_button")
        self.grid_Trivia_edit.addWidget(self.delete_button, 6, 0, 1, 1)
        self.grid_Trivia_edit.setRowStretch(0, 1)
        self.grid_Trivia_edit.setRowStretch(1, 2)
        self.grid_Trivia_edit.setRowStretch(2, 2)
        self.grid_Trivia_edit.setRowStretch(3, 2)
        self.grid_Trivia_edit.setRowStretch(4, 2)
        self.grid_Trivia_edit.setRowStretch(5, 2)
        self.horizontalLayout.addWidget(self.Editor_Frame)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        MainWindow.setCentralWidget(self.main_layout)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHelp_2 = QtWidgets.QMenu(self.menubar)
        self.menuHelp_2.setObjectName("menuHelp_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionHelp_site = QtWidgets.QAction(MainWindow)
        self.actionHelp_site.setObjectName("actionHelp_site")
        self.actionGet_OpenQuiz_for_Desktop = QtWidgets.QAction(MainWindow)
        self.actionGet_OpenQuiz_for_Desktop.setObjectName("actionGet_OpenQuiz_for_Desktop")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuSettings.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionHelp_site)
        self.menuHelp.addAction(self.actionGet_OpenQuiz_for_Desktop)
        self.menuHelp_2.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuHelp_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.newButtton.setText(_translate("MainWindow", "New Question"))
        #self.QuestionButton.setText(_translate("MainWindow", "PushButton"))
        self.incorrect_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Incorrect Answers</span></p><p>(comma seperated,add as many as you\'d like)</p><p><br/></p></body></html>"))
        self.diff_label.setText(_translate("MainWindow", "Difficulty"))
        self.correct_label.setText(_translate("MainWindow", "Correct Answer"))
        self.category_label.setText(_translate("MainWindow", "Category"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Easy"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Easy"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Medium"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Hard"))
        self.title_label_2.setText(_translate("MainWindow", "Edit your Question"))
        self.title_label.setText(_translate("MainWindow", "Question"))
        self.EditButton.setText(_translate("MainWindow", "Save Changes"))
        self.delete_button.setText(_translate("MainWindow", "Delete Question"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Play"))
        self.menuHelp_2.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionHelp_site.setText(_translate("MainWindow", "Play on the web"))
        self.actionGet_OpenQuiz_for_Desktop.setText(_translate("MainWindow", "Get OpenQuiz for Desktop"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())