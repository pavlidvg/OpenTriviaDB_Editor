from pathvalidate import validate_filename, ValidationError
from jsonschema import validate
import Editor
import json
import os
import html
import codecs

CACHE_LOCATION = "cache" # location where the contents of a non saved project are saved before a crash
CACHE_FILE_INFO = "cached_file_info" # location of the field containing information on the cached project
def update_cache():
    """Updates the Cache file with the information on the current project name(e.g. project name)."""
    try:

        save_to_file(CACHE_LOCATION,cache=True)
        with open(CACHE_FILE_INFO,'w') as info_file:
            file_str = json.dumps({"project_name": Editor.project_name})
            info_file.write(file_str)


        return True
    except:
        return False
    return False
def flush_cache():
    """Empties out the files that keep cached information. This function is called whenever  changes are saved to the project"""
    open(CACHE_LOCATION,'w').close()
    open(CACHE_FILE_INFO,'w').close()

def save_to_file(location: str,cache: bool=False):
    """Saves current project info to a target file. Used to save to a system file if a user selects the 'save' or 'save as' options,
    as well as for saving a project to a cache for internal crash protection.

    @:param location is the string of  the target file location we want to save to. will be created if not existent
     @:param cache= False is a boolean set to indicate if the save will be done to a file that we have labeled as cache"""
    changes = {"response_code": 0}

    with codecs.open(location, "w",'utf-8') as file:  # contents are read as utf-8 characters
        changes["results"] = decode_unicode(Editor.question_list)
        try:
            file_str = json.dumps(changes,ensure_ascii=False, indent=4)
            file.write(file_str)
            if not cache:
                Editor.MainWindow.setWindowTitle("OpenQuiz - " + os.path.basename(location))
                Editor.changes = False  # updates the changes flag, since there are now no changes in the document
                flush_cache()  # no need to keep a backup of an already saved file
            else:
                pass

            file.close()



        except Exception as e:
            print("The file saving process failed. Please try again through the editor, or contact the developer team")
            print(e)



    return 0
# will need better defined schema later
def validate_file_schema(filepath:str):
   """Validates that a given file  contains a valid schema according to the OpenTrivia Database API. Currently does not work """
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
    """Loads the JSON objects from a file onto the program. Assumes all the questions are stored in the 'results ' """
    with open(filename, "r+",encoding='utf-8') as file:  # contents are read as utf-8 characters
        data = file.read()
        file_contents = json.loads(bytes(data,'utf-8'))
        try:
            Editor.question_list = file_contents['results']
        except:
            return False

        file.close()
    return os.path.basename(filename)

def decode_unicode(question_list):
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




