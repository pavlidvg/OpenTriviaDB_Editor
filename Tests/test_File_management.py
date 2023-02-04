import json
import time

import pytest

import File_management,Editor
import filecmp
TEST_CACHE_FILENAME = "TESTCACHE"

"""tests whether or not the files are loaded with the correct amount of questions in the memory"""
save_test_data = [("nonexistent",0),("input_files/checksize.oq", 102),
                  ("input_files/emptyfile.txt", 0),("input_files/avg_case_test.oq", 3),("input_files/yousuck.json",11)]  # each file, along with its number of questions
@pytest.mark.parametrize("input_data, expected_out", save_test_data)
def test_load_from_file(input_data,expected_out):
    """Tests how the program loads a file a single question list, how it saves it and whether any changes are made during the file saving process.
    The test  scenario is as follows:
    Files are loaded from the Tests/input_files directory, the files should create a question list with as many objects as there are questions in each file.
    Then, they are saved to a different file and reloaded, and the question list should remain unchanged"""
    File_management.load_questions(input_data)
    assert len(Editor.question_list) == expected_out

    loaded_quetsions = Editor.question_list

    #if the lists are of the correct size, check if they can be reloaded back into the files
    File_management.save_to_file("test_save_out") #file should be created within the function if not existent
    if expected_out != 0: # only test non-empty files
        Editor.question_list = [] # empty out the list
        File_management.load_questions("test_save_out")
        assert Editor.question_list == loaded_quetsions





