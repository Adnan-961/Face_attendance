import os
import pickle
import tkinter as tk        
from tkinter import ttk
from tkinter import messagebox
import cv2
from student import *
import mysql.connector


#####################################  MYSQL ########################
mydb = mysql.connector.connect(                                     #
    host="localhost",                                               #
    user="root",                                                    #
    password="",                                                    #
    database="student_db"                                           #
)                                                                   #
mycursor = mydb.cursor()                                            #
#####################################################################




with open("studentlist.dat", "rb") as fp:
        SavedList = pickle.load(fp)


def log(text, color='green'):       #creating a method to show text in the bottom window
    

    if color == 'green':                #refer to this https://gist.github.com/vratiu/9780109
        print(f'\033[1;32m{text}\033[0m') #format the text and color it green
    elif color == 'red':
        print(f'\033[1;31m{text}\033[0m')  #format the text and color it red
    elif color == 'yellow':
        print(f'\033[1;33m{text}\033[0m')   #format the text and color it yellow
    elif color == 'blue':
        print(f'\033[1;34m{text}\033[0m')   #format the text and color it blue
    else:
        print('text')

    if messages_text is not None:       #if messages box is not empty
        messages_text.insert('end', text + "\n", color) #insert the text


# ---
def disable_event():
    pass

def login_window():         #login window + auth checking
    #TODO: convert it to class (and maybe put in separated file)
    """Show login window"""

    def check():                    # check if auth is correct
        username = username_login_entry.get()   #get the user written
        password = password__login_entry.get()  #get the password written

        if username == "admin" and password =="123":
            print("access granted")
            log("[INFO] access granted", 'blue')    #send a text to the bottom window with blue color
            login_screen.destroy()                  #after logging in , remove the login window

    login_screen = tk.Tk()                          #initialaize the login window and start it
    login_screen.protocol("WM_DELETE_WINDOW", disable_event)    #disable the X to prevent quitting [ there was a bug ] 

    login_screen.title("Login")                             #Name of the window

    tk.Label(login_screen, text="Please enter login details").pack(pady=(20,0), padx=20)    #text+ style

    tk.Label(login_screen, text="Username").pack(pady=(20,0), padx=20)                  #text + style

    username_login_entry = tk.Entry(login_screen, textvariable="username", bg='white')  #Entry box
    username_login_entry.pack()                                                         #put the box in the window

    tk.Label(login_screen, text="Password").pack(pady=(20,0), padx=20)              #text

    password__login_entry = tk.Entry(login_screen, textvariable="password", show='*', bg='white')       #Entry box + style
    password__login_entry.pack()                                                                   #put the box in the window 

    tk.Button(login_screen, text="Login", command=check, width=10).pack(pady=20, padx=20) #add a button

    login_screen.mainloop()                                                 #start the login window

# ----

def read_data():                                        #method to read the data
    log("[DEBUG] read_data(): read data from file", 'yellow')   #send this text to the bottom window as yellow color

    with open("studentlist.dat", "rb") as fp:       #oppening the student list .dat
         SavedList = pickle.load(fp)                # as savedList
    return SavedList    


def save_data(SavedList):                               #method for saving the new list after adding/removing a student                         
    log("[DEBUG] save_data(): save data in file", 'yellow')

    with open("studentlist.dat", "wb") as fp:       #open the list
         pickle.dump(SavedList, fp)             # and save it


def register_student():                         #method for registering a student
    """Validation to Register a new student"""

    first = first_name_var.get()                  # getting the data written in the input boxes
    last  = last_name_var.get()
    major      = major_var.get()
    id  = id1_var.get()
    username = first+" "+last                   # creating the username
    #query to add the student to the database
    query = "INSERT INTO `students`(`id`, `first_name`, `last_name`, `major`, `username`, `passcode`) VALUES ( "+str(id)+ ",'"+first+"','"+last+"','"+major+"','"+username+"','123')"

    if first and last and major and id > 0: #if all input boxes are not empty
    
        found = False       #checking if the student exists
        
        for item in students:   #loop all students to check for ids 
            if item.id == id:   #if any student have the same id you wrote , it wont register him
                found = True    #found a duplicate
                break           # stops the registration
                
        if found:               #if found a duplicate sends a text
            log("[ERROR] register_student(): ID already exists in database", 'red')
        else:   #else , register the student
            try:
                item = Student(id, first, last, major) #creating the student object 
                students.append(item)       #add the new student to the list above
                save_data(students)         #save the new list
                mycursor.execute(query)     # excute the query and insert him to the database
                mydb.commit()               # commit the changes
                log(str(mycursor.rowcount) + " row inserted")   #send a text to the shell/bottom window
            except Exception as ex:                         # error handeling   
                log("[ERROR] register_student(): " + str(ex), 'red')    #sending error text with its details
    else:
        log("[ERROR] register_student(): wrong values", 'red')
    
    
def take_picture():     # method to take an image and save it to the images folder
    """Take an image and save it to PATH"""

    video = cv2.VideoCapture(0)         # initialize the camera

    while True:                         # loop the video
        check, frame = video.read() 
        if check is True:
            cv2.imshow("Capturing", frame)      # show the video feed in a window
            key = cv2.waitKey(1)                   #wait for a key to be pressed
            if key == ord('q'):                     # if the key is pressed
                filename = '{} {}.jpg'.format(first_name_var.get(), last_name_var.get())    # save the image as firstname+last.jpg {barack obama.jpg}
                fullpath = os.path.join(PATH , filename)    #move the image to the path (images)
                cv2.imwrite(fullpath, frame)        #write the image
                break   #quit

    cv2.destroyAllWindows()#quit all windows
    video.release()#stop the camera feed


def list_students():    # method to list all students
    """List the students along with their information"""

    if not students:    # if list is empty
        print("List is empty !")
        # create label at start and here only change text
        messages_text.insert('end', "List is empty\n")

    for item in students:           #for each student list his info
        print(item.allinfo())


def delete_all_students():          #method to delete all students
    """Deletes all students"""
    query = "DELETE FROM students"
    mycursor.execute(query)
    mydb.commit()
    students.clear()        # clear students list
    save_data(students) # save the list

    log("[INFO] delete_all_students(): Students deleted", 'blue')# send a text


def list_all_students():                # create a new window to show listed students
    """Creates a window onclick"""
    
    window = tk.Toplevel(tkWindow) # create a new window
    

    if not students:        # if student list is empty
        label = tk.Label(window, text="No students", bg='red')
        label.grid(row=0, column=0, ipadx=50, ipady=20, sticky='news')  # ipad = internal pad
        log("[INFO] list_all_student(): No students", 'blue')   # send text 
    else:
        for i, item in enumerate(students): # loop arround all the students [enumerate helps counting the students ]
            label = tk.Label(window, text=item.allinfo())   #create a label to list the current student [ after clicking list all students info]
            label.grid(row=i, column=0) #go to next line 
        log("[INFO] list_all_student(): students " + str(len(students)), 'blue')#sends text + number of students


def delete_student():   #method to delete a specific student
    """Deletes a specific student"""
    id_number = id2_var.get()
    query = "DELETE FROM `students` WHERE id="+str(id_number)
    
    found = False   # if student doesnt exist , shows error

    for item in students:       
        if item.id == id_number:#
            students.remove(item)
            try:
                mycursor.execute(query)
                mydb.commit()
            except Exception as ex:
                log("[ERROR] start: " + str(ex), 'red')
            found = True
            break

    if found:#delete the student then save the list
        save_data(students)
        log("[INFO] delete_student(): Student deleted", 'blue')
    else:
        log("[ERROR] delete_student(): Student not found", 'red')

# --- main ---

messages_text = None

login_window()  #starts the login window

# - constants - (UPPER_CASE_NAMES)

PATH = 'images'  # Folder to store student's images

# - variables -

#num = 1

# - rest -

try:
    students = read_data() #read the data from the student list.dat
except Exception as ex:
    log("[ERROR] start: " + str(ex), 'red')
    log("[DEBUG] start: create empty list of students", 'yellow')
    students = []

# - window -

tkWindow = tk.Tk() # create the window after the login
#tkWindow.geometry('400x180')
tkWindow.title('Student Management System')

# - variables which has to be created after `tk.Tk()` -
id1_var = tk.IntVar()
id2_var = tk.IntVar()
first_name_var = tk.StringVar()
last_name_var = tk.StringVar()
major_var = tk.StringVar()

# - widgets -

# - widgets - add student -

frame_add = tk.LabelFrame(tkWindow, text="Add Student")
frame_add.pack(fill="both", expand=True, padx=10, pady=10)

frame_add.columnconfigure(1, weight=1)

label = tk.Label(frame_add, text="Student ID : ", anchor="e", width=20)
label.grid(row=0, column=0, sticky='we', pady=(0,5))

entry = tk.Entry(frame_add, textvariable=id1_var, bg='white')
entry.grid(row=0, column=1, sticky='we', columnspan=2, padx=(0,5), pady=(0,5))

label = tk.Label(frame_add, text="Student First Name : ", anchor="e", width=20)
label.grid(row=1, column=0, sticky='we', pady=(0,5))

entry = tk.Entry(frame_add, textvariable=first_name_var, bg='white')
entry.grid(row=1, column=1, sticky='we', columnspan=2, padx=(0,5), pady=(0,5))

label = tk.Label(frame_add, text="Student Last Name : ", anchor="e", width=20)
label.grid(row=3, column=0, sticky='we', pady=(0,5))

entry = tk.Entry(frame_add, textvariable=last_name_var, bg='white')
entry.grid(row=3, column=1, sticky='we', columnspan=2, padx=(0,5), pady=(0,5))

label = tk.Label(frame_add, text="Student Major : ", anchor="e", width=20)
label.grid(row=4, column=0, sticky='we', pady=(0,5))

entry = tk.Entry(frame_add, textvariable=major_var, bg='white')
entry.grid(row=4, column=1, sticky='we', columnspan=2, padx=(0,5), pady=(0,5))

button = tk.Button(frame_add, text="Take picture", command=take_picture, width=12)
button.grid(row=5, column=2, sticky='we', padx=(0,5), pady=(0,5))

button = tk.Button(frame_add, text="Add Student", command=register_student, width=12)
button.grid(row=6, column=2, sticky='we', padx=(0,5), pady=(0,5))


# - widgets - delete student -

frame_delete = tk.LabelFrame(tkWindow, text="Delete Student")
frame_delete.pack(fill="both", expand=True, padx=10, pady=10)

frame_delete.columnconfigure(1, weight=1)

label = tk.Label(frame_delete, text="Student ID : ", anchor="e", width=20)
label.grid(row=0, column=0, sticky='we', pady=(0,5))

entry = tk.Entry(frame_delete, textvariable=id2_var, bg='white')
entry.grid(row=0, column=1, sticky='we', columnspan=2, padx=(0,5), pady=(0,5))

button = tk.Button(frame_delete, text="Delete ", command=delete_student, width=12)
button.grid(row=1, column=2, sticky='we', padx=(0,5), pady=(0,5))

# - widgets - other -

frame_other = tk.LabelFrame(tkWindow, text="Other Functions")
frame_other.pack(fill="both", expand=True, padx=10, pady=10)

button = tk.Button(frame_other, text="List Students", command=list_all_students)
button.grid(row=0, column=0, sticky='we', padx=(5,0), pady=(5,5))

button = tk.Button(frame_other, text="Delete All Students", command=delete_all_students)
button.grid(row=0, column=1, sticky='we', padx=(5,5), pady=(5,5))

# - widgets - messages -

frame_message = tk.LabelFrame(tkWindow, text="Messages")
frame_message.pack(fill="both", expand=True, padx=10, pady=10)

messages_text = tk.Text(frame_message, height=10, bg='black')
messages_text.pack()
for color in ['red', 'green', 'yellow', 'blue']:
    messages_text.tag_config(color, foreground=color)

# - start -

tkWindow.mainloop()# starts the window or keep it alive