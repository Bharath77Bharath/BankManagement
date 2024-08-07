#imports
from tkinter import *
import os
from PIL import ImageTk, Image
import tkinter.messagebox
import random
#account_number = str(random.randint(1200000,1200100))

#Main Vars
tran_type="----------"
curr_clock="-----------"
today="----------"

updated_balance="----------"

#Main Screen
master = Tk()
master.title('Banking App')

#Functions
def finish_reg():
    #Vars
    global account_no
    global acc_file
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    account_no = str(random.randint(1200000,1200100))
    
    if name == "" or age == "" or gender == "" or password == "":
        notif.config(fg="red",text="All fields requried!!! ")
        return

    for name_check in all_accounts:
        if name == name_check :
            notif.config(fg="red",text="Account already exists!!! Please try again")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(gender+'\n')
            new_file.write('0')
            acc_file = open(account_no,"w")
            acc_file.write(account_no+'\n')
            acc_file.write(age)
            acc_file.close()
            new_file.close()
            notif_acc.config(text="Your Account Number is "+account_no)
            notif.config(fg="green", text="Account has been created successfully")
def destroy_reg():
    register_screen.destroy()
    return
    

def register():
    #Vars
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    global notif_acc
    global register_screen
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    
    
    
    
    #Register Screen
    register_screen = Toplevel(master)
    register_screen.title('Register')

    #Labels
    Label(register_screen, text="Please enter your details below to register", font=('Bahnschrift SemiBold SemiConden',12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name", font=('Calibri',12)).grid(row=1,sticky=W)
    Label(register_screen, text="Age", font=('Calibri',12)).grid(row=2,sticky=W)
    Label(register_screen, text="Gender", font=('Calibri',12)).grid(row=3,sticky=W)
    Label(register_screen, text="Password", font=('Calibri',12)).grid(row=4,sticky=W)
    notif_acc = Label(register_screen, font=('Calibri',12))
    notif_acc.grid(row=7,sticky=N,pady=10)
    notif = Label(register_screen, font=('Calibri',12))
    notif.grid(row=8,sticky=N,pady=10)

    #Entries
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=0,padx=5,sticky=E)
    Entry(register_screen,textvariable=temp_age).grid(row=2,column=0,padx=5,sticky=E)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0,padx=5,sticky=E)
    Entry(register_screen,textvariable=temp_password,show="*").grid(row=4,column=0,padx=5,sticky=E)
    
    

    #Buttons
    Button(register_screen, text="Register", fg='green', command = finish_reg, width=15, font=('Bahnschrift SemiBold SemiConden',12)).grid(row=6,sticky=W,pady=5,padx=5)
    Button(register_screen, text="Close", fg='red', command = destroy_reg, width=15, font=('Bahnschrift SemiBold SemiConden',12)).grid(row=6,column=0,sticky=E,pady=5,padx=5)

def login_session():
    global login_name
    global login_account
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()
    login_account = temp_login_account.get()
    global account_dashboard
    for name in all_accounts:
        if name == login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password  = file_data[1]
            room = open(account_no,"r")
            room_data = room.read()
            room_data = room_data.split('\n')
            account = room_data[0]
            #Account Dashboard
            if login_account == account:
                if login_password == password:
                    login_screen.destroy()
                    account_dashboard = Toplevel(master)
                    account_dashboard.title('Dashboard')
                    #Labels
                    Label(account_dashboard, text="Account Dashboard", font=('Bahnschrift SemiBold SemiConden',20)).grid(row=0,sticky=N,pady=10)
                    Label(account_dashboard, text="Welcome "+name, font=('Bahnschrift SemiBold SemiConden',15)).grid(row=1,sticky=N,pady=5)
                    #Buttons
                    Button(account_dashboard, text="Personal Details",font=('Bahnschrift SemiBold SemiConden',12),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
                    Button(account_dashboard, text="Deposit",font=('Bahnschrift SemiBold SemiConden',12),width=30,command=deposit).grid(row=3,sticky=N,padx=10)
                    Button(account_dashboard, text="Withdraw",font=('Bahnschrift SemiBold SemiConden',12),width=30,command=withdraw).grid(row=4,sticky=N,padx=10)
                    Button(account_dashboard, text="Transaction Receipt",font=('Bahnschrift SemiBold SemiConden',12),width=30,command=transaction).grid(row=5,sticky=N,padx=10)
                    Button(account_dashboard, text="Exit", fg='red',font=('Bahnschrift SemiBold SemiConden',12),width=30,command=destroy).grid(row=6,sticky=N,padx=10)
                    Label(account_dashboard).grid(row=7,sticky=N,pady=10)
                    return
                else:
                    login_notif.config(fg="red", text="Incorrect Password!!")
                    return
            else:
                login_notif.config(fg="red", text="Incorrect Account Number!!")
                return
               
    login_notif.config(fg="red", text="No account found !!")


def destroy():
    account_dashboard.destroy()
    

#DESPOSIT FUNCTIONS

def deposit():
    #Vars
    global amount
    global deposit_notif
    global current_balance_label
    global date_time
    global tran_type
    global curr_clock
    global today
    global deposit_screen
    import time
    from datetime import date
    today=date.today()
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    amount = StringVar()
    file   = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[3]
    tran_type="Deposit"
    
    #Deposit Screen
    deposit_screen = Toplevel(master)
    deposit_screen.title('Deposit')
    #Label
    Label(deposit_screen, text="Deposit", font=('Bahnschrift SemiBold SemiConden',20)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(deposit_screen, text="Current Balance : Rs."+details_balance, font=('Calibri',12))
    current_balance_label.grid(row=1,column=0,sticky=W)
    Label(deposit_screen, text="Amount : ", font=('Calibri',12)).grid(row=2,column=0,sticky=W)
    deposit_notif = Label(deposit_screen,font=('Calibri',12))
    deposit_notif.grid(row=5, sticky=N,pady=5)
    #Entry
    Entry(deposit_screen, textvariable=amount).grid(row=2,column=1,sticky=E)
    
    #Button
    Button(deposit_screen,text="Finish", fg='green',font=('Bahnschrift SemiBold SemiConden',12),command=finish_deposit,width=15).grid(row=3,sticky=W,pady=5,padx=5)
    Button(deposit_screen,text="Close", fg='red',font=('Bahnschrift SemiBold SemiConden',12),command=destroy_deposit,width=15).grid(row=3,column=1,sticky=E,pady=5,padx=5)
   

def finish_deposit():
    #Vars
    global updated_balance
    if amount.get() == "":
        deposit_notif.config(text='Amount is required!',fg="red")
        return
    if float(amount.get()) <=0:
        deposit_notif.config(text='Negative currency is not accepted', fg='red')
        return

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[3]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : Rs."+str(updated_balance),fg="green")
    deposit_notif.config(text='Balance Updated', fg='green')

def destroy_deposit():
    deposit_screen.destroy()
    return


#WITHDRAW FUNCTIONS
 
def withdraw():
     #Vars
    global amount
    global withdraw_notif
    global current_balance_label
    global date_time
    global tran_type
    global curr_clock
    global today
    global withdraw_screen
    import time
    from datetime import date
    today=date.today()
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    amount = StringVar()
    file   = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[3]
    tran_type="Withdraw"
    
   
    #Deposit Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title('Withdraw')
    #Label
    Label(withdraw_screen, text="Withdraw", font=('Bahnschrift SemiBold SemiConden',20)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(withdraw_screen, text="Current Balance : Rs."+details_balance, font=('Calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(withdraw_screen, text="Amount : ", font=('Calibri',12)).grid(row=2,sticky=W)
    withdraw_notif = Label(withdraw_screen,font=('Calibri',12))
    withdraw_notif.grid(row=5, sticky=N,pady=5)
    #Entry
    Entry(withdraw_screen, textvariable=amount).grid(row=2,column=1)
    #Button
    Button(withdraw_screen,text="Finish", fg='green',font=('Bahnschrift SemiBold SemiConden',12),command=finish_withdraw,width=15).grid(row=3,sticky=W,pady=5,padx=5)
    Button(withdraw_screen,text="Close", fg='red',font=('Bahnschrift SemiBold SemiConden',12),command=destroy_withdraw,width=15).grid(row=3 ,column=1,sticky=E,pady=5,padx=5)

def finish_withdraw():
    #Vars
    global updated_balance
    if amount.get() == "":
        withdraw_notif.config(text='Amount is required!',fg="red")
        return
    if float(amount.get()) <=0:
        withdraw_notif.config(text='Negative currency is not accepted', fg='red')
        return

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[3]

    if float(amount.get()) >float(current_balance):
        withdraw_notif.config(text='Insufficient Funds!', fg='red')
        return

    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(amount.get())
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : Rs."+str(updated_balance),fg="green")
    withdraw_notif.config(text='Balance Updated', fg='green')

def destroy_withdraw():
    withdraw_screen.destroy()
    return


#PERSONAL DETAILS FUNCTIONS    

def personal_details():
    #Vars
    global personal_details_screen
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    room = open(login_account,"r")
    room_data = room.read()
    room_data = room_data.split('\n')
    details_account = room_data[0]
    details_name = user_details[0]
    details_age = room_data[1]
    details_gender = user_details[2]
    details_balance = user_details[3]
    
    
    #Personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    #Labels
    Label(personal_details_screen, text="Personal Details", font=('Bahnschrift SemiBold SemiConden',20)).grid(row=0,sticky=N,pady=10)
    Label(personal_details_screen, text="Name  :   "+details_name, font=('Calibri',12)).grid(row=1,sticky=W,pady=3)
    Label(personal_details_screen, text="Account Number  :   "+details_account, font=('Calibri',12)).grid(row=2,sticky=W,pady=3)
    Label(personal_details_screen, text="Age  :   "+details_age, font=('Calibri',12)).grid(row=3,sticky=W,pady=3)
    Label(personal_details_screen, text="Gender  :   "+details_gender, font=('Calibri',12)).grid(row=4,sticky=W,pady=3)
    Label(personal_details_screen, text="Balance  :   Rs."+details_balance, font=('Calibri',12)).grid(row=5,sticky=W,pady=3)
    
    #Buttons
    Button(personal_details_screen,text="Close", fg='red',font=('Bahnschrift SemiBold SemiConden',12),command=destroy_personal_details,width=15).grid(row=6,sticky=N,pady=5,padx=5)

def destroy_personal_details():
    personal_details_screen.destroy()
    return


#TRANSACTION RECEIPT FUNCTIONS


def transaction():
    global transaction_screen
    #Transaction Screen
    transaction_screen = Toplevel(master)
    transaction_screen.title("Transaction")
    

    #Lables
    Label(transaction_screen, text="Transaction Receipt",fg='green',font=('Bahnschrift SemiBold SemiConden',20)).grid(row=0,column=0,sticky=E,pady=20)
    Label(transaction_screen, text="Transaction Type",font=('Bahnschrift SemiBold SemiConden',14)).grid(row=1,column=0,sticky=W)
    Label(transaction_screen, text="Date",font=('Bahnschrift SemiBold SemiConden',14)).grid(row=1,column=1,sticky=W,padx=50)
    Label(transaction_screen, text="Time",font=('Bahnschrift SemiBold SemiConden',14)).grid(row=1,column=2,sticky=W,padx=50)
    Label(transaction_screen, text="Amount",font=('Bahnschrift SemiBold SemiConden',14)).grid(row=1,column=3,sticky=W,padx=50)
    Label(transaction_screen, text="Balance After Transaction",font=('Bahnschrift SemiBold SemiConden',14)).grid(row=1,column=4,sticky=W,padx=50)
    tran_type_label=Label(transaction_screen, text=tran_type,font=('Calibri',12))
    tran_type_label.grid(row=2,sticky=W,padx=25,pady=5)
    tran_date_label=Label(transaction_screen, text=today,font=('Calibri',12))
    tran_date_label.grid(row=2,column=1,sticky=N,padx=30,pady=5)
    tran_time_label=Label(transaction_screen, text=curr_clock,font=('Calibri',12))
    tran_time_label.grid(row=2,column=2,sticky=N,padx=40,pady=5)
    tran_balance_label=Label(transaction_screen, text="Rs."+str(updated_balance),font=('Calibri',12))
    tran_balance_label.grid(row=2,column=4,sticky=N,padx=50,pady=5)
    tran_balance_label=Label(transaction_screen, text="Rs."+str(updated_balance),font=('Calibri',12))
    tran_balance_label.grid(row=2,column=4,sticky=N,padx=50,pady=5)
    try:
        tran_amount_label=Label(transaction_screen, text="Rs."+amount.get(),font=('Calibri',12))
        tran_amount_label.grid(row=2,column=3,sticky=N,padx=50,pady=5)
    except:
        tran_amount_label=Label(transaction_screen, text="----------",font=('Calibri',12))
        tran_amount_label.grid(row=2,column=3,sticky=N,padx=50,pady=5)

    #Buttons
    Button(transaction_screen,text="Close", fg='red',font=('Bahnschrift SemiBold SemiConden',15),command=destroy_transaction,width=10).grid(row=3,column=2,sticky=N,pady=5)
    
    
def destroy_transaction():
    transaction_screen.destroy()
    return


def login():
    #Vars
    global temp_login_name
    global temp_login_password
    global temp_login_account
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    temp_login_account = StringVar()
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Login')
    #Labels
    Label(login_screen, text="Login to your account", font=('Bahnschrift SemiBold SemiConden',12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="Username", font=('Calibri',12)).grid(row=1,sticky=W,pady=5)
    Label(login_screen, text="Password", font=('Calibri',12)).grid(row=3,sticky=W,pady=5)
    Label(login_screen, text="Account Number", font=('Calibri',12)).grid(row=2,sticky=W,pady=5)
    login_notif = Label(login_screen, font=('Calibri',12))
    login_notif.grid(row=4,sticky=W)
    #Entry
    Entry(login_screen, textvariable=temp_login_name).grid(row=1,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_account).grid(row=2,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_password,show="*").grid(row=3,column=1,padx=5)
    #Button
    Button(login_screen, text="Login", fg='green', command=login_session, width=15,font=('Bahnschrift SemiBold SemiConden',12)).grid(row=5,sticky=W,pady=5,padx=5)
    Button(login_screen, text="Close", fg='red', command=destroy_login, width=15,font=('Bahnschrift SemiBold SemiConden',12)).grid(row=5,column=1,sticky=W,pady=5,padx=5)
def destroy_login():
    login_screen.destroy()
    return


def iexit():
    iexit=tkinter.messagebox.askyesno ("Bank management system","Are you sure want to Exit")
    if iexit >0:
        master.destroy()
        return


    
#Image import
img = Image.open('secure.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#Labels
Label(master, text = "WELCOME TO STARK BANK", font=('Algerian',14)).grid(row=0,sticky=N,pady=10)
Label(master, text = "The most secure bank you've probably used", font=('Bahnschrift SemiBold SemiConden',12)).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2,sticky=N,pady=15)

#Buttons
Button(master, text="Register", font=('Bahnschrift SemiBold SemiConden',12),width=20,command=register).grid(row=3,sticky=N)
Button(master, text="Login", font=('Bahnschrift SemiBold SemiConden',12),width=20,command=login).grid(row=4,sticky=N,pady=5)
Button(master, text="Exit", fg='red', font=('Bahnschrift SemiBold SemiConden',12),width=20,command=iexit).grid(row=5,sticky=N,pady=2)

master.mainloop()
