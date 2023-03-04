class OpenTDBEditor:
    project_title = "untitled project"
    project_file = ""

    #-----not sure if needed
    last_question_selected = -1  # index of the current question we're editing
    last_button = -1  # Last button pressed
    changes = False  # flag for whether the file has been changed since last save
    #-------
    def __init__(self,question_list: list,sample_q: dict):
        self.question_list = question_list
        self.sample_q = sample_q
