import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QDialog, QMessageBox

from PyQt5 import QtCore, QtGui, QtWidgets
import json


import Editor


def calculate_font_size(font: QFont, button,minimum_font_size = 9):
    font_size = QtGui.QFontMetrics(font)
    target_width = button.maximumWidth() - 2  # add some padding
    k = font_size.width(button.text())

    if k < target_width:  # if this size of text already fits, don't change it
        return font.pointSize()
    else:
        ratio = k / target_width  # calculate how much bigger the text is compared to the button. E.g. if ratio = 1.2, it's 20% bigger
        size_correct = font.pointSize() / ratio
        if size_correct < minimum_font_size:
            size_correct = minimum_font_size  # make it readble and word wrap it instead of making it extra small
        return (size_correct)


def save_to_file(location: str):
    questionlist = Editor.question_list
    changes = {"response_code": 0}

    with open(location, "w") as file:
        changes["results"] = questionlist
        try:
            file_str = json.dumps(changes, indent=4)
            file.write(file_str)
            return 0
        except:
            file.write("The file saving process failed. Please try again through the editor, or contact the developer team")
            return -12

def confirm_popup():
    print("here?")
    popup = QtWidgets.QMessageBox()
    popup.setWindowTitle("Save changes to document")
    popup.setText("There are unsaved changes to your document")
    popup.setInformativeText("Do you want to save your changes?")
    popup.icon()
    popup.setDefaultButton(QMessageBox.Yes )
    popup.addButton(QMessageBox.Yes)
    popup.addButton(QMessageBox.No)
    ret = popup.exec_()
    if ret == QMessageBox.No:
        return False
    else:
        save_to_file(Editor.project_name)
        return True









