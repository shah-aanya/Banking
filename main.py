import tkinter as tk
from tkinter import messagebox
import json
import time
from tkinter import ttk

# Function to set up the initial window
def setup():
    global root, bg_color, canvas
    bg_color = '#a2a2d0'
    root = tk.Tk()
    root.title("Aanya's Bank")
    canvas = tk.Canvas(root, bg=bg_color, height=600, width=900)
    canvas.pack()

# Function to read user database from JSON file
def read_database():
    global main_dict
    try:
        handle = open(r'/Users/aanyashah/python-coding/projects/banking/database.json', 'r')
        main_dict = json.load(handle)
        handle.close()
    except:
        handle = open(r'/Users/aanyashah/python-coding/projects/banking/database.json', 'w')
        json.dump({}, handle)
        handle.close()

# Function to write user data to JSON file
def write_database(main_dict):
    handle = open(r'/Users/aanyashah/python-coding/projects/banking/database.json', 'w')
    json.dump(main_dict, handle, indent= 4)
    handle.close()

# Function to validate password
def is_valid_password(password):
    # Password must have uppercase, lowercase, number, and special symbol
    return any(ch.isupper() for ch in password) and any(ch.islower() for ch in password) \
           and any(ch.isdigit() for ch in password) and any(ch in '!@#$%^&*()~' for ch in password) \
           and len(password) >= 8

# Function to validate username
def validate_user(username):
    # Username must have at least 8 alphanumeric characters
    val = set()
    if len(username) >= 8 and username.isalnum():
        return True
    else:
        return False

# Function to handle user registration
def register_user(username_signup, password_entry, passconf_sui,):
    if validate_user(username_signup):
        if is_valid_password(password_entry):
            if passconf_sui == password_entry:
                messagebox.showinfo('Succsses Message','Registration Successful')
                personaldetails_ui()
            else:
                messagebox.showerror('Error Message','Registration Unsuccessful: Passwords do not match')
        else:
            messagebox.showerror('Error Message','Registration Unsuccessful: Invalid Password')
    else:
        messagebox.showerror('Error Message','Registration Unsuccessful: Invalid Username')
    
# Function to extract registration details and initiate registration process
def extract_registration_details():
    global confirm_password_entry, password_entry, username_entry, username_signup, password_entry
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    register_user(username, password, confirm_password)


# Function to handle the signup process
def signup():
    global confirm_password_entry, password_entry, username_entry, toplevel_sui
    toplevel_sui = tk.Toplevel(root, bg = bg_color, height = 600, width = 900)
    label_sui = tk.Label(toplevel_sui, text = "Sign-Up Page", bg = bg_color,fg = 'white', font = ('brown sugar',30) )
    label_sui.place(relx = 0.35, rely = 0.05, relheight= 0.1, relwidth= 0.3)

    user_label_signup = tk.Label(toplevel_sui, text = "Username", bg = bg_color ,fg = 'white', font = ('lora',30) )
    user_label_signup.place(relx = 0.2, rely = 0.3, relheight= 0.1, relwidth= 0.3)

    username_entry = tk.Entry(toplevel_sui, fg = 'white', font = ('lora',20),  bg = bg_color )
    username_entry.place(relx = 0.5, rely = 0.3, relheight= 0.1, relwidth= 0.3)

    password_label_signup = tk.Label(toplevel_sui, text = "Password", bg = bg_color ,fg = 'white', font = ('lora',30) )
    password_label_signup.place(relx = 0.2, rely = 0.45, relheight= 0.1, relwidth= 0.3)

    password_entry = tk.Entry(toplevel_sui, fg = 'white', font = ('lora',20), bg = bg_color )
    password_entry.place(relx = 0.5, rely = 0.45, relheight= 0.1, relwidth= 0.3)

    password_confirm_signup = tk.Label(toplevel_sui, text = "Confirm \n Password", bg = bg_color,fg = 'white', font = ('lora',30) )
    password_confirm_signup.place(relx = 0.2, rely = 0.6, relheight= 0.1, relwidth= 0.3)

    confirm_password_entry = tk.Entry(toplevel_sui, fg = 'white', font = ('lora',20), bg = bg_color )
    confirm_password_entry.place(relx = 0.5, rely = 0.6, relheight= 0.1, relwidth= 0.3)

    button_signup = tk.Button(toplevel_sui, bg = bg_color, fg  = bg_color, font = ('lora',20), text = 'Sign- Up', command= extract_registration_details)
    button_signup.place(relx = 0.4, rely = 0.8, relheight= 0.1, relwidth= 0.2)

# Function to handle personal details entry
def personal_details_ui():
    global entries, main_dict, password_entry, username_signup
    keys = ['First Name', 'Last Name', 'Phone Number', 'Email']
    subdict = {}
    for i in range(4):
        key = keys[i]
        value = entries[i].get()
        subdict[key] = value
    subdict["Password"] = password_entry
    subdict["Balance"] = 0
    subdict["History"] = []
    main_dict[username_signup] = subdict
    write_database(main_dict)
    messagebox.showinfo('Succsses Message','Your account has been created :)')

    toplevel_pui.destroy()

def personaldetails_ui():
    global entries, toplevel_sui, toplevel_pui
    toplevel_sui.destroy()
    toplevel_pui = tk.Toplevel(root, bg = bg_color, height = 600, width = 650)
    label_pui = tk.Label(toplevel_pui, text = "Personal Information", bg = bg_color,fg = 'white', font = ('brown sugar',27) )
    label_pui.place(relx = 0.05, rely = 0.05, relheight= 0.05, relwidth= 0.9)

    namelabel_pui = tk.Label(toplevel_pui, text = "First Name: ", bg = bg_color,fg = 'white', font = ('lora',25) )
    namelabel_pui.place(relx = 0.2, rely = 0.2, relheight= 0.1, relwidth= 0.3)

    nameentry_pui = tk.Entry(toplevel_pui, fg = 'white', font = ('lora',20),  bg = bg_color )
    nameentry_pui.place(relx = 0.5, rely = 0.2, relheight= 0.1, relwidth= 0.3)

    lnamelabel_pui = tk.Label(toplevel_pui, text = "Last Name: ", bg = bg_color,fg = 'white', font = ('lora',25) )
    lnamelabel_pui.place(relx = 0.2, rely = 0.35, relheight= 0.1, relwidth= 0.3)

    lnameentry_pui = tk.Entry(toplevel_pui, fg = 'white', font = ('lora',20),  bg = bg_color )
    lnameentry_pui.place(relx = 0.5, rely = 0.35, relheight= 0.1, relwidth= 0.3)

    phonelabel_pui = tk.Label(toplevel_pui, text = "Phone Number: ", bg = bg_color,fg = 'white', font = ('lora',25) )
    phonelabel_pui.place(relx = 0.2, rely = 0.5, relheight= 0.1, relwidth= 0.3)

    phoneentry_pui = tk.Entry(toplevel_pui, fg = 'white', font = ('lora',20),  bg = bg_color )
    phoneentry_pui.place(relx = 0.5, rely = 0.5, relheight= 0.1, relwidth= 0.3)

    emaillabel_pui = tk.Label(toplevel_pui, text = "Email: ", bg = bg_color,fg = 'white', font = ('lora',25) )
    emaillabel_pui.place(relx = 0.2, rely = 0.65, relheight= 0.1, relwidth= 0.3)

    emailentry_pui = tk.Entry(toplevel_pui, fg = 'white' , font = ('lora',20),  bg = bg_color )
    emailentry_pui.place(relx = 0.5, rely = 0.65, relheight= 0.1, relwidth= 0.3)

    entries = [nameentry_pui, lnameentry_pui, phoneentry_pui, emailentry_pui]

    button_signup = tk.Button(toplevel_pui, bg = 'white', fg  = bg_color, font = ('lora',20), text = 'Submit', command= personal_details_ui)
    button_signup.place(relx = 0.4, rely = 0.8, relheight= 0.1, relwidth= 0.2)

def login_bl():
    global main_dict, userentry_lui, pasentry_lui, username_lbl
    username_lbl = userentry_lui.get()
    password_lbl = pasentry_lui.get()
    if username_lbl in main_dict.keys() and  password_lbl == main_dict[username_lbl]['Password']:
        messagebox.showinfo('Succsses Message: ', 'Login Succssesful')
        homepage_ui()
    else:
        messagebox.showerror('Error Message: ', 'Login Unsuccssesful')

def logout_Bl():
    login_ui()

def homepage_ui():
    frame_main = tk.Frame(canva, bg = bg_color)
    frame_main.place(relheight= 1, relwidth= 1)
    label_h = tk.Label(canva, text = "Home Page", bg = bg_color ,fg = 'white', font = ('brown sugar',50) )
    label_h.place(relx = 0.3, rely = 0.05, relheight= 0.1, relwidth= 0.4)

    button_banking = tk.Button(canva, bg = 'white', fg  = bg_color, font = ('lora',25), text = 'Banking', command=  banking_ui)
    button_banking.place(relx = 0.15, rely = 0.2, relheight= 0.3, relwidth= 0.3)

    button_a = tk.Button(canva, bg = 'white', fg  = bg_color, font = ('lora',25), text = 'Profile', command= profile_UI)
    button_a.place(relx = 0.55, rely = 0.2, relheight= 0.3, relwidth= 0.3)

    button_ha = tk.Button(canva, bg = 'white', fg  = bg_color, font = ('lora',25), text = 'Email Statment')
    button_ha.place(relx = 0.15, rely = 0.65, relheight= 0.3, relwidth= 0.3)

    button_hp = tk.Button(canva, bg = 'white', fg  = bg_color, font = ('lora',25), text = ' Log-out', command= logout_Bl)
    button_hp.place(relx = 0.55, rely = 0.65, relheight= 0.3, relwidth= 0.3)

def profile_UI():
    global userdetails, toplevel_pui

    userdetails = main_dict[username_lbl]
    toplevel_pui = tk.Toplevel(root, bg = bg_color, height = 600, width = 650)
    label_pui = tk.Label(toplevel_pui, text = "Your Account", bg = bg_color,fg = 'white', font = ('brown sugar',35) )
    label_pui.place(relx = 0.05, rely = 0.05, relheight= 0.05, relwidth= 0.9)

    namelabel_pui = tk.Label(toplevel_pui, text = "First Name: ", bg = bg_color,fg = 'black', font = ('lora',20) )
    namelabel_pui.place(relx = 0.2, rely = 0.2, relheight= 0.1, relwidth= 0.3)

    nameentry_pui = tk.Label(toplevel_pui, text = userdetails["First Name"], bg = bg_color,fg = 'white', font = ('lora',20) )
    nameentry_pui.place(relx = 0.5, rely = 0.2, relheight= 0.1, relwidth= 0.3)

    lnamelabel_pui = tk.Label(toplevel_pui, text = "Last Name: ", bg = bg_color,fg = 'black', font = ('lora',20) )
    lnamelabel_pui.place(relx = 0.2, rely = 0.35, relheight= 0.1, relwidth= 0.3)

    lnameentry_pui = tk.Label(toplevel_pui, text = userdetails["Last Name"], bg = bg_color,fg = 'white', font = ('lora',20) )
    lnameentry_pui.place(relx = 0.5, rely = 0.35, relheight= 0.1, relwidth= 0.3)

    phonelabel_pui = tk.Label(toplevel_pui, text = "Phone Number: ", bg = bg_color,fg = 'black', font = ('lora',20) )
    phonelabel_pui.place(relx = 0.2, rely = 0.5, relheight= 0.1, relwidth= 0.3)

    phoneentry_pui = tk.Label(toplevel_pui, text = userdetails["Phone Number"], bg = bg_color,fg = 'white', font = ('lora',20) )
    phoneentry_pui.place(relx = 0.5, rely = 0.5, relheight= 0.1, relwidth= 0.3)

    emaillabel_pui = tk.Label(toplevel_pui, text = "Email: ", bg = bg_color,fg = 'black', font = ('lora',20) )
    emaillabel_pui.place(relx = 0.2, rely = 0.65, relheight= 0.1, relwidth= 0.3)

    emailentry_pui = tk.Label(toplevel_pui, text = userdetails["Email"], bg = bg_color,fg = 'white', font = ('lora',20) )
    emailentry_pui.place(relx = 0.5, rely = 0.65, relheight= 0.1, relwidth= 0.3)

    button_signup = tk.Button(toplevel_pui, bg = 'white', fg  = bg_color, font = ('lora',20), text = 'Edit', command= profile_BL)
    button_signup.place(relx = 0.4, rely = 0.8, relheight= 0.1, relwidth= 0.2)

def profile_BL():
    global entries_pbl
    nameentry_pui = tk.Entry(toplevel_pui,  bg = bg_color,fg = 'white', font = ('lora',20) )
    nameentry_pui.place(relx = 0.5, rely = 0.2, relheight= 0.1, relwidth= 0.3)
    nameentry_pui.insert(0, userdetails["First Name"])

    lnameentry_pui = tk.Entry(toplevel_pui, bg = bg_color,fg = 'white', font = ('lora',20) )
    lnameentry_pui.place(relx = 0.5, rely = 0.35, relheight= 0.1, relwidth= 0.3)
    lnameentry_pui.insert(0,userdetails["Last Name"]) 

    phoneentry_pui = tk.Entry(toplevel_pui, text = userdetails["Phone Number"], bg = bg_color,fg = 'white', font = ('lora',20) )
    phoneentry_pui.place(relx = 0.5, rely = 0.5, relheight= 0.1, relwidth= 0.3)
    phoneentry_pui.insert(0,userdetails["Phone Number"]) 

    emailentry_pui = tk.Entry(toplevel_pui, text = userdetails["Email"], bg = bg_color,fg = 'white', font = ('lora',20) )
    emailentry_pui.place(relx = 0.5, rely = 0.65, relheight= 0.1, relwidth= 0.3)
    emailentry_pui.insert(0,userdetails["Email"]) 

    entries_pbl= [nameentry_pui, lnameentry_pui, phoneentry_pui, emailentry_pui]

    button_signup = tk.Button(toplevel_pui, bg = 'white', fg  = bg_color, font = ('lora',20), text = 'Update', command= updateprofile_data)
    button_signup.place(relx = 0.4, rely = 0.8, relheight= 0.1, relwidth= 0.2)


def updateprofile_data():
    texts = []
    for entry in entries_pbl:
        texts.append(entry.get())
    if "" not in texts:
        main_dict[username_lbl]["First Name"]= entries_pbl[0].get()
        main_dict[username_lbl]["Last Name"]= entries_pbl[1].get()
        main_dict[username_lbl]["Phone Number"]= entries_pbl[2].get()
        main_dict[username_lbl]["Email"]= entries_pbl[3].get()
        
        write_database(main_dict)
        messagebox.showinfo('Succsses Message: ', 'Update Succssesful')
        toplevel_pui.destroy()
    else:
        messagebox.showerror('Error Message: ', 'Update Unsuccssesful- please write in all the boxes')

   

def in_transaction():
    global tr_num
    trans = main_dict[username_lbl]["History"]
    if len(trans) == 0:
        tr_num = 0
    else:
        row = trans[-1]
        row = row.split()
        tr_num = int(row[0])

def deposit():
    global avilbalance, tr_num
    amount = entry_dep.get()
    amount = int(amount)
    avilbalance = main_dict[username_lbl]["Balance"] 
    avilbalance += amount
    main_dict[username_lbl]["Balance"] = avilbalance
    tr_num += 1
    tr_entry = str(tr_num).ljust(20) + str(amount).ljust(20) + '-'.ljust(20) + str(avilbalance).ljust(20)
    main_dict[username_lbl]["History"].append(tr_entry)
    write_database(main_dict)
    updatebalance(avilbalance)


def withdraw():
    global avilbalance, tr_num
    w_amount = entry_wd.get()
    w_amount = int( w_amount)
    avilbalance = main_dict[username_lbl]["Balance"]
    if w_amount < avilbalance:
        avilbalance -=  w_amount
        main_dict[username_lbl]["Balance"] = avilbalance
        tr_num += 1
        tr_entry = str(tr_num).ljust(20) + '-'.ljust(20) + str( w_amount).ljust(20) + str(avilbalance).ljust(20)
        main_dict[username_lbl]["History"].append(tr_entry)
        write_database(main_dict)
        updatebalance(avilbalance)
    else:
        messagebox.showerror('Error Message: ', 'Insifficiant Balance')


def updatebalance(avilbalance):
    labelamt_dep.configure(text= '$' + str(avilbalance))
    labelamt_wd.configure(text= '$' + str(avilbalance))
    show_transaction()

#Function to display transaction history
def show_transaction():
    global labelFrame_cb
    list_trans = main_dict[username_lbl]["History"][-5:]
    title = 'Tr num'.ljust(15)+ 'Deposit'.ljust(15)+'Withdraw'.ljust(15)+ 'Total Balance'.ljust(15)
    labelent = tk.Label(labelFrame_cb, text = title, bg = bg_color  ,fg = 'black', font = ('brown sugar',15) )
    labelent.place(relx = 0.1, rely = 0, relheight= 0.1, relwidth= 0.8)
    spacing = 0.1
    for i in range(len(list_trans)):
        labelent = tk.Label(labelFrame_cb, text = list_trans[i] ,bg = bg_color, fg = 'black', font = ('brown sugar',15) )
        labelent.place(relx = 0.1, rely = spacing, relheight= 0.1, relwidth= 0.8)
        spacing = spacing + 0.15

def banking_ui():
    global entry_dep, entry_wd,labelamt_dep, labelamt_wd, avilbalance, labelFrame_cb
    # intilazing transaction number
    in_transaction()
    avilbalance = main_dict[username_lbl]["Balance"]
    toplevel_banking = tk.Toplevel(root, bg = bg_color, height=600, width= 900 )
    toplevel_banking.title('Banking')
    nb_banking = ttk.Notebook(toplevel_banking)
    nb_banking.pack()
    # frames
    frame_deposit = ttk.Frame(nb_banking, height= 600, width = 900)
    frame_deposit.pack()
    nb_banking.add(frame_deposit, text = 'Deposit')

    frame_withdraw = ttk.Frame(nb_banking, height= 600, width = 900)
    frame_withdraw.pack()
    nb_banking.add(frame_withdraw, text = 'With Draw')

    frame_checkbal = ttk.Frame(nb_banking, height= 600, width = 900)
    frame_checkbal.pack()
    nb_banking.add(frame_checkbal, text = 'Transaction History')

    # deposit ui
    frame_dep = tk.Label(frame_deposit, bg = bg_color)
    frame_dep.place(relx = 0, rely = 0, relheight= 1, relwidth= 1)

    label1_dep = tk.Label(frame_deposit, text = "Deposit Amount: ", bg = bg_color ,fg = 'black', font = ('brown sugar',35),  justify= 'left' )
    label1_dep.place(relx = 0.1, rely = 0.2, relheight= 0.1, relwidth= 0.35)

    entry_dep = tk.Entry(frame_deposit, fg = 'white', font = ('lora',15), bg = bg_color)
    entry_dep.place(relx = 0.1, rely = 0.4, relheight= 0.1, relwidth= 0.4)

    button_dep = tk.Button(frame_deposit, fg = 'black', font = ('lora',20), text = 'Deposit', command= deposit)
    button_dep.place(relx = 0.1, rely = 0.6, relheight= 0.1, relwidth= 0.2)

    labelFrame_dep = tk.LabelFrame(frame_deposit, text = "Current Balance: ", bg = 'white' ,fg = 'black', font = ('brown sugar',25), labelanchor= 'n')
    labelFrame_dep.place(relx = 0.55, rely = 0.05, relheight= 0.9, relwidth= 0.4)

    labelamt_dep = tk.Label(labelFrame_dep, text = '$'+str(avilbalance) , bg = 'white' ,fg = 'black', font = ('brown sugar',50) )
    labelamt_dep.place(relx = 0.1, rely = 0.3, relheight= 0.4, relwidth= 0.8)

    # withdraw ui
    frame_wd = tk.Label(frame_withdraw, bg = bg_color)
    frame_wd.place(relx = 0, rely = 0, relheight= 1, relwidth= 1)

    label1_wd = tk.Label(frame_withdraw, text = "Withdraw Amount: ", bg = bg_color ,fg = 'black', font = ('brown sugar',35), justify = 'left'  )
    label1_wd.place(relx = 0.1, rely = 0.2, relheight= 0.1, relwidth= 0.4)

    entry_wd = tk.Entry(frame_withdraw, fg = 'black', font = ('lora',20), bg = bg_color)
    entry_wd.place(relx = 0.1, rely = 0.4, relheight= 0.1, relwidth= 0.4)

    button_wd = tk.Button(frame_withdraw, fg = bg_color, font = ('lora',20), text = 'withdraw', command = withdraw)
    button_wd.place(relx = 0.1, rely = 0.6, relheight= 0.1, relwidth= 0.2)

    labelFrame_wd = tk.LabelFrame(frame_withdraw, text = "Current Balance: ", bg = 'white' ,fg = 'black', font = ('brown sugar',25), labelanchor= 'n')
    labelFrame_wd.place(relx = 0.55, rely = 0.05, relheight= 0.9, relwidth= 0.4)

    labelamt_wd = tk.Label(labelFrame_wd, text = '$'+str(avilbalance) , bg = 'white' ,fg = 'black', font = ('brown sugar',50) )
    labelamt_wd.place(relx = 0.1, rely = 0.3, relheight= 0.4, relwidth= 0.8)

    # check balance ui
    frame_wd = tk.Label(frame_checkbal, bg = bg_color)
    frame_wd.place(relx = 0, rely = 0, relheight= 1, relwidth= 1)

    labelFrame_cb = tk.LabelFrame(frame_checkbal, text = "Recent Transactions: ", bg = bg_color ,fg = 'black', font = ('times',20), labelanchor= 'nw')
    labelFrame_cb.place(relx = 0.1, rely = 0.05, relheight= 0.9, relwidth= 0.8)

    show_transaction()


def login_ui():
    global userentry_lui, pasentry_lui, canva
    canva = tk.Canvas(root, bg = bg_color, height=600, width= 900)
    canva.place(relheight=1,relwidth=1)
    label_lui = tk.Label(canva, text = "Log-in Page", bg = bg_color ,fg = 'white', font = ('brown sugar',30) )
    label_lui.place(relx = 0.3, rely = 0.05, relheight= 0.1, relwidth= 0.4)

    userlabel_lui = tk.Label(canva, text = "Username: ", bg = bg_color,fg = 'white', font = ('lora',25) )
    userlabel_lui.place(relx = 0.15, rely = 0.2, relheight= 0.1, relwidth= 0.35)

    userentry_lui = tk.Entry(canva, fg = 'white', font = ('lora',15),  bg = bg_color )
    userentry_lui.place(relx = 0.2, rely = 0.3, relheight= 0.05, relwidth= 0.3)

    paslabel_lui = tk.Label(canva, text = "Password: ", bg = bg_color, fg = 'white', font = ('lora',25) )
    paslabel_lui.place(relx = 0.15, rely = 0.4, relheight= 0.1, relwidth= 0.3)

    pasentry_lui = tk.Entry(canva, fg = 'white', font = ('lora',15), bg = bg_color, show= "*")
    pasentry_lui.place(relx = 0.2, rely = 0.5, relheight= 0.05, relwidth= 0.3)

    button_lui = tk.Button(canva, bg = bg_color, fg  = bg_color, font = ('lora',20, 'bold'), text = 'Login', command= login_bl)
    button_lui.place(relx = 0.2, rely = 0.6, relheight= 0.05, relwidth= 0.2)
    # img = ImageTk.PhotoImage(Image.open("/Users/aanyashah/Desktop/Python Codes/projects/banking/Aanya's.png"))

    # label = tk.Label(canva, image = img)
    # label.place(relx=0.5, rely=0.2, relheight= 0.4, relwidth= 0.4)

    linklabel_lui = tk.Label(canva, text = "New user? Click here to sign-up", bg = bg_color,fg = 'white', font = ('lora',15,'underline') )
    linklabel_lui.place(relx = 0, rely = 0.7, relheight= 0.05, relwidth= 0.8)
    linklabel_lui.bind("<Button-1>", signup)

setup()
read_database()
login_ui()
root.mainloop()