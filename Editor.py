import time

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog, QStyleFactory, QAction

import File_management
import Utilities
import scroll_test
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,json
import html.parser


#KINDA GLOBAL LISTS. USES CAREFULLY
question_list = []
file_contents = {}
project_name = "sample.oq" # badcode here :(
sample_q = {
      "category": "Sports",
      "type": "multiple",
      "difficulty": "easy",
      "question": "In baseball, how many fouls are an out?",
      "correct_answer": "4",
      "incorrect_answers": [
        "5",
        "3",
        "2"
      ]
}

last_question_selected = -1  # index of the current question we're editing
last_button = -1  # Last button pressed
changes = False  # flag for whether the file has been changed since last save

width = 0
height = 0  # screen dimensions

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
app.setStyle(QStyleFactory.create('Fusion'))




def add_buttons(gui, question):
    layout = gui.frame.layout()
    layout_items = len(layout) #how many widgets are currently displayed on this frame

    new_button = QtWidgets.QToolButton(gui.frame)
    new_button.setText(question['question'])

    new_button.setMaximumWidth(450)
    # new_button.setFixedWidth(gui.QList_frame.width())
    font_used = QFont('Consolas',12,weight = 75)
    font_used.setPointSize(Utilities.calculate_font_size(font_used,new_button))
    font_used.setBold(True)
    new_button.setFont(font_used)
    new_button.setStyleSheet("""background-color:#48608f;
                            height: 30px;
                             color:#FFFFFF
                             """

                             )

    #isnert the button
    new_button.clicked.connect(lambda: question_selected(gui, new_button))
    layout.insertWidget(layout_items - 1, new_button)

#adds a new button for every new question we want to add, also updates the list of question to include a new one
def add_new_question(gui):
    global question_list,changes
    layout = gui.frame.layout()
    layout_items = len(layout)  # how many widgets are currently displayed on this frame
    new_button = QtWidgets.QPushButton(gui.frame)

    new_button.setText(sample_q['question'])

    new_button.setStyleSheet("""background-color:#48608f;
                            height: 30px;
                             color:#FFFFFF
                             """)
    new_button.setMaximumWidth(450)
    font_used = QFont('Consolas', 12,weight=75)

    font_used.setPointSize(Utilities.calculate_font_size(font_used, new_button))
    if font_used.pointSize() < 9:
        font_used.setPointSize(9)  # make it readable and word wrap it instead of making tiny
    font_used.setBold(True)
    new_button.setFont(font_used)

    # insert the button
    new_button.clicked.connect(lambda: question_selected(gui, new_button))
    layout.insertWidget(layout_items - 1, new_button)

    if not changes:
        MainWindow.setWindowTitle(MainWindow.windowTitle() + " (UNSAVED CHANGES)")
    changes = True


    # make a JSON object to encapsulate the question
    new_q = {}
    new_q["category"] = sample_q["category"]  # can make it a one liner, but it's more organized that way
    new_q["type"] = sample_q["type"]
    new_q["question"] = sample_q["question"]
    new_q["difficulty"] = sample_q["difficulty"]
    new_q["correct_answer"] = sample_q["correct_answer"]
    new_q["incorrect_answers"] = sample_q["incorrect_answers"]


    # add the question to the json object, by appending it on the 'results' list
    question_list.append(new_q)


def clear_fields(gui):
    gui.question_input.setText("")
    gui.category_input.setText("")
    gui.correct_answer_input.setText("")
    gui.comboBox.setCurrentIndex(0)
    gui.textEdit.setText("")


def load_ui(filename,new):
    global question_list, project_name
    if not new:
        project_name = File_management.load_questions(filename)

    else:
        project_name = filename
        question_list = []

    # loads up the UI
    gui = scroll_test.Ui_MainWindow()
    print("loaded up the gui?")
    gui.setupUi(MainWindow)
    print("set up the gui?")
    MainWindow.setWindowTitle("OpenQuiz - " + project_name)

    # refactor elsewhere sometime later
    for i in question_list:
        i['question'] = html.unescape(i['question'])
        add_buttons(gui, i)

    gui.scrollArea.setFixedWidth(gui.scrollAreaWidgetContents.maximumWidth())

    #key mappings
    gui.pushButton.clicked.connect(lambda : add_new_question(gui))
    gui.delete_button.clicked.connect(lambda: delete_q(gui,last_question_selected))
    gui.EditButton.clicked.connect(lambda: save_changes(gui,last_question_selected))
    print("we're on file:"+filename)
    gui.actionSave.triggered.connect(lambda: File_management.save_to_file(filename))
    gui.actionSave_as.triggered.connect(save_file_as)
    gui.actionOpen.triggered.connect(lambda: open_new_file(filename,gui))

    MainWindow.show()

    sys.exit(app.exec_())



# deletes the current question, doesnt  store any backups
def save_changes(gui,index):
    global changes
    if last_question_selected == -1:
        return

    indextodict = {0: "easy", 1: "medium", 2: "hard"}


    question_list[index]['category'] = gui.category_input.text()
    print(question_list[index]['category'])
    question_list[index]['type'] = "multiple" #fix this later



    if gui.comboBox.currentIndex()== 2:
        question_list[index]['difficulty'] = 'hard'
    elif gui.comboBox.currentIndex() == 1:
        question_list[index]['difficulty'] = 'medium'
    else:
        question_list[index]['difficulty'] = 'easy'


    question_list[index]['question'] = gui.question_input.toPlainText()
    question_list[index]['correct_answer'] = gui.correct_answer_input.text()




    try:
        question_list[index]['incorrect_answers'] = gui.textEdit.toPlainText().split(",")
    except:
        print("error when parsing incorrect, make it more user friendly later")
        question_list[index]['incorrect_answers'] = gui.textEdit.toPlainText()

    last_button.setText(question_list[index]['question'])

    #reccalibrate new font size, after changing the question
    last_button.setFont(QFont('Consolas',Utilities.calculate_font_size(QFont('Consoals',12),last_button),weight=75))


    if not changes:
        MainWindow.setWindowTitle(MainWindow.windowTitle() + " (UNSAVED CHANGES)")
    changes = True

def clear_gui(gui: scroll_test.Ui_MainWindow):

    layout = gui.frame.layout()
    num_of_buttons = layout.count() - 1  # ignore the invisible vertical spacer
    for i in range(num_of_buttons):
        layout.itemAt(0).widget().setParent(None)  # delete all buttons


def delete_q(gui,index):
    global last_question_selected,changes
    if index == -1 or last_button is None:
        return
    question_list.pop(index)  # actually deletes the loaded question from RAM

    layout = gui.frame.layout()
    layout.itemAt(index).widget().setParent(None) #deletes the button
    last_question_selected = -1
    clear_fields(gui)

    if not changes:
        MainWindow.setWindowTitle(MainWindow.windowTitle() + " (UNSAVED CHANGES)")
    changes = True


#might need refactoring later if varible names change
def question_selected(gui,button):
    global last_question_selected,last_button

    if last_button != -1:

        last_button.setStyleSheet("""background-color:#48608f;
                            height: 30px;
                             color:#FFFFFF
                             """

                             )

    question_index = gui.frame.layout().indexOf(button)
    question = question_list[question_index]
    last_button = button
    last_question_selected = question_index #
    last_button.setStyleSheet("""background-color:#48208f;
                            height: 30px;
                             color:#FFFFFF
                             """

                             )


    #update the UI to automatically show the fields

    gui.question_input.setText(question['question'])
    gui.category_input.setText(question['category'])
    gui.correct_answer_input.setText(question['correct_answer'])
    if question['difficulty'] == 'hard':
        gui.comboBox.setCurrentIndex(2)
    elif question['difficulty'] == 'medium':
        gui.comboBox.setCurrentIndex(1)
    else:
        gui.comboBox.setCurrentIndex(0)

    incorrect =""
    length = len(question['incorrect_answers'])

    #append all options for the "worng answers" category, putting commas where needed.Reverse split basically
    for i in range(length-1):
        incorrect += str(question['incorrect_answers'][i])
        #(question['incorrect_answers'])
        incorrect += ","

    incorrect += str(question['incorrect_answers'][length-1])
    gui.textEdit.setText(incorrect)

def save_file_as():
    global project_name
    file_options = ["OQ Files (*.oq)","JSON Files (*.json)"]
    dialog = QFileDialog()
    filename = dialog.getSaveFileName(caption="Save Quiz File as",filter="OQ Files (*.oq);;JSON Files (*.json);;All Files")
    print(filename)
    try:
        File_management.save_to_file(filename[0])
        project_name = filename[0]
    except FileNotFoundError:
        print("File not found, most likely because no file was selected maybe inform user")


def open_new_file(current_file,gui):
    global changes
    save_before_opening = False
    if changes:
        save_before_opening = Utilities.confirm_popup()
    if save_before_opening:
        print("now saving on:"+current_file)
        Utilities.save_to_file(current_file)
    # Open the QDialog to get new project opened
    file_options = ["OQ Files (*.oq)", "JSON Files (*.json)"]
    dialog = QFileDialog()
    filename = dialog.getOpenFileName(caption="Open your OQ Project",
                                      filter="OQ Files (*.oq);;JSON Files (*.json);;All Files")
    if not filename[0]:
        return
    clear_gui(gui)

    clear_fields(gui)
    changes = False
    print(filename[0])
    reload_ui(filename[0], False, gui)



def reload_ui(filename: str, new: bool, gui: scroll_test.Ui_MainWindow):
    global question_list, project_name
    if not new:
        project_name = File_management.load_questions(filename)
    else:
        question_list = []

    print("will now print list")
    print(question_list)

    #
    MainWindow.setWindowTitle("OpenQuiz - " + project_name)
    print("from now on were saving at:"+filename)
    gui.actionSave.triggered.connect(lambda: File_management.save_to_file(filename))   # override old save state

    # refactor elsewhere sometime later
    for i in question_list:
        i['question'] = html.unescape(i['question'])
        add_buttons(gui, i)








