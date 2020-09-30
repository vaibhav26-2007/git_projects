from  tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Students Record Form")

def getvalues():
    import time
    print("Uploading....")
    time.sleep(3)
    print("uploaded")
    with open("Stu Records.txt", "a") as f:
        f.write(f"{namevalue.get(),roll_novalue.get(),phone_novalue.get(),class_divvalue.get(),emailvalue.get()}\n")
        a.bind('<Button-1>',quit)
        a.bind('<Double-1>')

def rate():
    value=tmsg.askquestion("Your Experience??","How Was Your Experience Using This Form\n"
                                         "Was it Good???")
    if value=="yes":
        message=("Great!!! Thank You For Using Us")

    else:
        message=("Thank You For Your Feedback\n"
                 "We Will Make Sure The Problem is Resolved")
    tmsg.showinfo("Thanks for your feedback",message)



def help():
    tmsg.showinfo("basic info","we will be helping you in submitting form\n"
                 "to submit the form you need to fill the detail\n"
                 "if any thing went wrong you can use Clear Button\n"
                 "to submit form Double click the Submit Button\n"
                 "and you want to submit it twice Single Click the Submit Button")

        #print(f"{namevalue.get(),roll_novalue.get(),phone_novalue.get(),class_divvalue.get(),emailvalue.get()}")

root.geometry("650x600")

Label(root,text="Welcome to student detail form",font=("verdana",20,"bold"),borderwidth=10,relief=SUNKEN)\
    .grid(row=0,column=3,pady=20)
#making of all the labels
name=Label(root,text="Name",font=("Arial",12,"bold"))
roll_no=Label(root,text="roll_no",font=("Arial",12,"bold"))
phone_no=Label(root,text="phone_no",font=("Arial",12,"bold"))
class_div=Label(root,text="class_div",font=("Arial",12,"bold"))

#packing all the labels
name.grid(row=1,column=2)
roll_no.grid(row=2,column=2)
phone_no.grid(row=3,column=2)
class_div.grid(row=4,column=2)

namevalue = StringVar()
roll_novalue = StringVar()
phone_novalue = StringVar()
class_divvalue = StringVar()
emailvalue = IntVar()

nameentry=Entry(root,textvariable=namevalue)
roll_noentry=Entry(root,textvariable=roll_novalue)
class_diventry=Entry(root,textvariable=class_divvalue)
phone_noentry=Entry(root,textvariable=phone_novalue)

nameentry.grid(row=1,column=3)
roll_noentry.grid(row=2,column=3)
phone_noentry.grid(row=3,column=3)
class_diventry.grid(row=4,column=3)

email=Checkbutton(text="have a personal email??",variable=emailvalue)
email.grid(row=5,column=3,pady=10)

b=Label(root,text="Double click to submit the Form only once \n"
                  "and single click to submit the form two times ",font="Arial 12 bold",pady=10)
b.grid(row=6,column=3)
a=Button(text="submit",command=getvalues,font="verdana 15 bold")
a.grid(row=7,column=3)

main_menu=Menu(root)
m1=Menu(main_menu)
m1.add_command(label="Help",command=help)
m1.add_command(label="Rate Us",command=rate)


main_menu.add_cascade(label='Basic info',menu=m1)

root.config(menu=main_menu)

def removeValue(event):
    nameentry.delete(0, 'end')
    roll_noentry.delete(0, 'end')
    phone_noentry.delete(0, 'end')
    class_diventry.delete(0, 'end')
    return None

button = Button(root, text="clear",font="verdana 10 bold")
button.grid(row=8,column=3,pady=20,padx=10)
button.bind('<Button-1>',removeValue)


root.mainloop()
