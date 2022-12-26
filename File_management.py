from pathvalidate import validate_filename, ValidationError
from jsonschema import validate
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
            file.close()


        except Exception as e:
            print("The file saving process failed. Please try again through the editor, or contact the developer team")
            print(e)



    return 0
# will need better defined schema later
def validate_file(filepath:str):
   with open(filepath,'r+',encoding='utf-8') as file, open('schema','r+',encoding='utf-8') as schema:
       try:
           questionlist = json.load(file)
           for question in questionlist['results']:
               validate(instance=question,schema=json.load(schema))

           #validate(instance=)
       except Exception:
           print("Validation currently doesnt work, please provide a valid schema")
   return True




def load_questions(filename : str):

    with open(filename, "r+",encoding='utf-8') as file:
        data = file.read()
        file_contents = json.loads(bytes(data,'utf-8'))
        try:
            Editor.question_list = file_contents['results']
        except:
            return False

        file.close()
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


def valid_filename(name:str):  #checks if the given string is compatible as a save file name for windows and UNIX systems
    try:
        validate_filename(name)
        return True
    except ValidationError as e:
        return False
        print("{}\n".format(e))




