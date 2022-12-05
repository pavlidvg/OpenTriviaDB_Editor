import Editor
import  json
import os
from PyQt5.QtWidgets import QFileDialog
def save_to_file(location: str):
    questionlist = Editor.question_list
    changes = {"response_code": 0}

    with open(location, "w") as file:
        changes["results"] = questionlist
        try:
            file_str = json.dumps(changes, indent=4)
            file.write(file_str)
            Editor.MainWindow.setWindowTitle("OpenQuiz - " + os.path.basename(location))
            Editor.changes = False  # updates the changes flag, since there are now no changes in the document

            return 0
        except:
            print("The file saving process failed. Please try again through the editor, or contact the developer team")
            return -5

def load_questions(filename : str):
    print("will now load questions")
    with open(filename, "r+") as file:
        data = file.read()
        file_contents = json.loads(data)

        Editor.question_list = file_contents['results']
        return os.path.basename(filename)

