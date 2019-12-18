# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import os

#title bar name of the program
program_name = "Text Editor GUI"
#initializing a NULL file name
file_name = None

def new_file(event = None):
    root.title("Untitled")
    global file_name
    file_name = None
    text_box.delete(1.0, tk.END)
    #on_content_changed()

def open_file(event = None):
    #opening the file dialogue box
    txt_file = tk.filedialog.askopenfilename(title = "Open the File", defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])
    if txt_file:
        #setting the title of the window to the current saved file name
        global file_name
        file_name = txt_file
        root.title("{} - {}".format(os.path.basename(file_name), program_name))
        text_box.delete(1.0, tk.END)

        # Open file and put text in the text area
        with open(txt_file) as _file:
            text_box.insert(1.0, _file.read())
            # Update the text area
            root.update_idletasks()

def saveas_file(event = None):
    # Opening the save as dialog box
    file_save = tk.filedialog.asksaveasfilename(title ="Save As File",defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file_save != None:
        global file_name
        file_name = file_save
        write_to_file(file_name)
        root.title("{} - {}".format(os.path.basename(file_name), program_name))
        return "break"

def save_file(event = None):
    global file_name
    if not file_name:
        #if you're saving an untitled file, then save as function will be called
        saveas_file()
    else:
        #if the file is already saved, and if you just want to save the changes...
        write_to_file(file_name)

def write_to_file(event = None):
    try:
        context = text_box.get('1.0', tk.END)
        with open(file_name, 'w') as the_file:
            the_file.write(context)
    except IOError:
        tk.messagebox.showwarning("Save", "Could not save this file!")

def exit_question():
    global file_name
    if file_name == None:
        #i.e. if it is an empty file, then it will close directly
        root.destroy()
    else:
        #it some contexts are there in the file, then it'll give the warning message
        answer = tk.messagebox.askquestion("Exit", "Do you want to Quit?")
        if answer == "yes":
            root.destroy()

def undo_option(event = None):
    text_box.event_generate("<<Undo>>")
    return "break"

def redo_option(event = None):
    text_box.event_generate("<<Redo>>")
    return "break"

def cut_option(event = None):
    text_box.event_generate("<<Cut>>")
    return "break"

def copy_option(event = None):
    text_box.event_generate("<<Copy>>")
    return "break"

def paste_option(event = None):
    text_box.event_generate("<<Paste>>")
    return "break"

def about(event = None):
    tk.messagebox.showinfo("About", "{} \nThis Text Editor is developed by Devvrat and Himani".format(program_name))

root = tk.Tk()

#displaying the name of the text editor on the title bar
root.title(program_name)

#setting the geometry of the window
root.geometry('600x500')
#setting the frame in which will contain our text area
frame = tk.Frame(root, height = 600, width = 500)
#setting up the scroll bar on the right hand side of the pg
scroll_bar = tk.Scrollbar(frame)
#setting up text area along with scroll bar which is on the right hand side of the screen
text_box = tk.Text(frame, width = 600, height = 550, yscrollcommand = scroll_bar.set, padx = 10, pady = 10)
scroll_bar.config(command = text_box.yview)
scroll_bar.pack(side = "right", fill = "y")
text_box.pack(side = "left", fill = "both", expand = True)
frame.pack()

my_menu = tk.Menu(root)
root.config(menu = my_menu)

#file menu
file_menu = tk.Menu(my_menu)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", compound = "left", command = new_file)
file_menu.add_command(label = "Open", compound = "left", command = open_file)
file_menu.add_command(label = "Save", compound = "left", command = save_file)
file_menu.add_command(label = "Save As", compound = "left", command = saveas_file)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = exit_question)

#edit menu
edit_menu = tk.Menu(my_menu)
my_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Undo", command = undo_option)
edit_menu.add_command(label = "Redo", command = redo_option)
edit_menu.add_separator()
edit_menu.add_command(label = "Cut", command = cut_option)
edit_menu.add_command(label = "Copy", command = copy_option)
edit_menu.add_command(label = "Paste", command = paste_option)

#help menu
about_menu = tk.Menu(my_menu)
my_menu.add_cascade(label = "About", menu = about_menu)
about_menu.add_command(label = "About this Text Editor!", command = about)

root.mainloop()