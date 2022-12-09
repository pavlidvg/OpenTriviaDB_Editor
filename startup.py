from tkinter import *
from tkinter import filedialog
import Editor

from win32gui import FindWindow, GetWindowRect

import File_management


def edit_clicked():
    folder_selected = filedialog.askopenfile(
        mode = 'r+',
        title='Choose the OpenQuiz File you want to edit',
        filetypes= (("OpenQuiz Files","*.oq"),("JSON Files","*.json"),("all files","*.*"))
            )
    if folder_selected is not None:  # if user closes the file dialog, this does not execute
        window.destroy()
        Editor.load_ui(folder_selected.name, False)





def name_new_file_menu():
    name_win = Toplevel(window)
   #dimensions
    x = 380
    y = 150

    name_win.geometry("%dx%d" %(x,y))
    name_win.title("Create a quiz - Name your quiz")
    name_win.configure(bg="#2f3136")
    name_win.grab_set()  # keeps the window in focus
    window_handle = FindWindow(None, window.title())
    window_rect = GetWindowRect(window_handle)  # tuple with x,y and dimensions

    # center the popup around the middle of the screen
    popup_x = (window_rect[0] + window_rect[2]) / 2 - y
    print(name_win.winfo_width())
    popup_y = (window_rect[1] + window_rect[3]) / 2 - y

    name_win.geometry("+%d+%d" % (popup_x, popup_y))
    name_win.attributes("-topmost", True)

#method after button click
    def create_project():
        proj_name = name.get()
        if not File_management.valid_filename(proj_name):
            return
        filename = proj_name+ ".oq"
        if filename == ".oq":
            filename = "Untitled quiz.oq"
        name_win.destroy()
        name_win.master.destroy()
        Editor.load_ui(filename,new =True)



    canvas2 = Canvas(
        name_win,
        bg="#2f3136",
        height=150,
        width=380,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas2.place(x=0, y=0)

    canvas2.create_text(
        189.5, 30.0,
        text="Name your New Project",
        fill="#ffffff",
        font=("Inter-Bold", int(20.0)))

    img = PhotoImage(file=f"create_button.png")
    b = Button(name_win,
        image=img,
        borderwidth=0,
        highlightthickness=0,
        command=create_project,
        relief="flat")

    b.place(
        x=153, y=106,
        width=73,
        height=29)

    entry0_img = PhotoImage(file=f"create_textbox.png")
    entry0_bg = canvas2.create_image(
        189.5, 79.0,
        image=entry0_img)

    name = StringVar()
    entry0 = Entry(name_win,
        bd=0,
        bg="#969eae",
        highlightthickness=0,
                   textvariable = name)

    entry0.place(
        x=79.0, y=61,
        width=221.0,
        height=34)
    name_win.resizable(False, False)
    name_win.mainloop()


#
def new_button():
    print("new quiz")
    project_name = name_new_file_menu()


window = Tk()

window.geometry("1600x900")
window.configure(bg = "#2f3136")
canvas = Canvas(
    window,
    bg = "#2f3136",
    height = 900,
    width = 1600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text(
    799.5, 117.0,
    text = "Open Quiz [DEMO]",
    fill = "#ffffff",
    font = ("InriaSans-Regular", int(72.0)))

canvas.create_text(
    197.5, 867.0,
    text = "Powered by special.nobodies",
    fill = "#ffffff",
    font = ("None", int(20.0)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = edit_clicked,
    relief = "flat")

b0.place(
    x = 250, y = 350,
    width = 220,
    height = 200)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = new_button,
    relief = "flat")

b1.place(
    x = 1100, y = 350,
    width = 220,
    height = 200)

window.resizable(False, False)
window.mainloop()
