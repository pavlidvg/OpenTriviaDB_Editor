import Editor
import json
import os
import html
import codecs
def save_to_file(location: str):
    changes = {"response_code": 0}

    with codecs.open(location, "w",'utf-8') as file:
        changes["results"] = decode_unicode(Editor.question_list)
        try:
            file_str = json.dumps(changes,ensure_ascii=False, indent=4)
            file.write(file_str)
            Editor.MainWindow.setWindowTitle("OpenQuiz - " + os.path.basename(location))
            Editor.changes = False  # updates the changes flag, since there are now no changes in the document

            return 0
        except Exception as e:
            print("The file saving process failed. Please try again through the editor, or contact the developer team")
            print(e)

            return -5

def load_questions(filename : str):
    print("will now load questions")
    with open(filename, "r+") as file:
        data = file.read()
        file_contents = json.loads(data)

        Editor.question_list = file_contents['results']
        return os.path.basename(filename)

def decode_unicode(question_list): # input is a byte array I THINK?
    for i in question_list:
        i['question'] = html.unescape(i['question'])
        i['category'] = html.unescape(i['category'])
        i['difficulty'] = html.unescape(i['difficulty'])
        i['type'] = html.unescape(i['type'])
        i['correct_answer'] = html.unescape(i['correct_answer'])
        i['incorrect_answers'] = html.unescape(i['incorrect_answers'])
        print(i)

    return question_list


