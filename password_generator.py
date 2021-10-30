from tkinter import *
from random import randint

def newrand():
    
    #clear
    pw_entry.delete(0, END)
    #get value from entry/length
    pw_length = int(my_entry.get())
   
    my_password= ' '

    #random character using ascii values
    for x in range(pw_length): 
        my_password += chr(randint(33,126))

    pw_entry.insert(0,my_password) #insert password into entry
    # pass

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get()) #add a pop uo to show password copied
    popupwindow= Toplevel(root)
    popupwindow.title("Alert")
    popupwindow.geometry("200x100")
    popupwindow.iconbitmap('E:/projects/password_generator/alert.ico')
    alert=Label(popupwindow,text="Password successfully copied")
    button1=Button(popupwindow,text="ok",command=popupwindow.destroy)
    
    alert.pack(pady=15)
    button1.pack()

root= Tk()
root.title("Strong Password Generator")
root.iconbitmap("E:/projects/password_generator/key.ico")
root.geometry("500x300")
root.config(bg='#F5C736')


lf= LabelFrame(root, font='Arial', text="CHOOSE LENGTH OF PASSWORD",bg='#F55636',fg='white')
lf.pack(pady=20)

#Entry box for password length
my_entry=Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20,padx=20)

#entry box for return password
pw_entry= Entry(root,text='',font=("Helvetica", 24),bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

#Frame for buttons
my_frame= Frame(root)
my_frame.pack(pady=20)
my_frame.config(bg='#F5C736')
#Button for generating password

my_button= Button(my_frame, text="Generate Password", command=newrand)
my_button.grid(row=0, column=0, padx=10)

clip_button= Button(my_frame, text="Copy to Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)



root.mainloop()