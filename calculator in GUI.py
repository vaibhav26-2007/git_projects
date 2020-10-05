from tkinter import *


def value(numbers):
    global input_
    input_=input_+ str(numbers)
    text_input.set(input_)

def clear():
    global input_
    input_=""
    text_input.set("")

def equals_to():
    global input_
    result=str(eval(input_))
    text_input.set(result)

root=Tk()
root.title("Calculator---by vaibhav singh")
input_=""
text_input=StringVar()

main_entry=Entry(root,bd=30,bg="black",fg="white",font="arial 15 bold",textvariable=text_input
                 ,insertwidth=5,justify=RIGHT,relief=SUNKEN).grid(columnspan=5)





button7=Button(root,text="7",bg="cyan",fg="black",font="arial 17 bold",bd=8,padx=16,pady=16,
               command=lambda:value(7),highlightcolor="yellow")\
    .grid(row=1,column=0)

button8=Button(root,text="8",bg="cyan",fg="black",font="arial 17 bold",bd=8,padx=16,pady=16,
               command=lambda:value(8)).grid(row=1,column=1)
button9=Button(root,text="9",bg="cyan",fg="black",font="arial 17 bold",bd=8,padx=16,pady=16,
               command=lambda:value(9)).grid(row=1,column=2)
button_add=Button(root,text="+",bg="light grey",fg="black",font="arial 17 bold",bd=8,padx=16,pady=16,
               command=lambda:value('+')).grid(row=1,column=3)

#===========================================================================================================
button4=Button(root,text="4",bg="cyan",fg="black",font="arial 17 bold",bd=8,padx=16,pady=16,
               command=lambda:value(4))\
    .grid(row=2,column=0)

button5=Button(root,text="5",bg="cyan",fg="black",font="arial 17 bold",bd=8,padx=16,pady=16,
               command=lambda:value(5)).grid(row=2,column=1)
button6=Button(root,text="6",bg="cyan",fg="black",font="arial 17 bold",bd=8,padx=16,pady=16,
               command=lambda:value(6)).grid(row=2,column=2)
button_sub=Button(root,text="-",bg="light grey",fg="black",font="arial 17 bold",bd=8,padx=16,pady=16,
               command=lambda:value('-')).grid(row=2,column=3)
#================================================================================================================
button1=Button(root,text="1",bg="cyan",fg="black",font="arial 17 bold",bd=8,padx=16,pady=16,
               command=lambda:value(1))\
    .grid(row=3,column=0)

button2=Button(root,text="2",bg="cyan",fg="black",font="arial 17 bold",bd=8,padx=16,pady=16,
               command=lambda:value(2)).grid(row=3,column=1)
button3=Button(root,text="3",bg="cyan",fg="black",font="arial 17 bold",bd=8,padx=16,pady=16,
               command=lambda:value(3)).grid(row=3,column=2)
button_multiply=Button(root,text="*",bg="light grey",fg="black",font="arial 17 bold",bd=8,padx=16,pady=16,
               command=lambda:value('*')).grid(row=3,column=3)

#=============================================================================================================
button0=Button(root,text="0",bg="cyan",fg="black",font="arial 17 bold",bd=8,padx=16,pady=16,
               command=lambda:value(0))\
    .grid(row=4,column=0)

buttonequals=Button(root,text="=",bg="grey",fg="black",font="arial 17 bold",bd=8,padx=16,pady=16,command=equals_to)\
    .grid(row=4,column=1)
buttonC=Button(root,text="C",bg="grey",fg="black",font="arial 17 bold",bd=8,padx=16,pady=16,command=clear)\
    .grid(row=4,column=2)

button_divide=Button(root,text="/",bg="light grey",fg="black",font="arial 17 bold",bd=8,padx=16,pady=16,
               command=lambda:value('/')).grid(row=4,column=3)



root.mainloop()