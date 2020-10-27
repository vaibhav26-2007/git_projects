from tkinter import *

def result():
    Principal = int(principal.get())
    Rate = int(rate.get())
    Time = int(time.get())

    ans = (Principal*Rate*Time)/100
    print(ans)
    answer.set(ans)

def res():
    principal.set("")
    rate.set("")
    time.set("")
    answer.set("")
def Quit():
    root.destroy()


if __name__ == '__main__':
    root = Tk()
    root.geometry("900x700")
    root.title("Simple Interest Calculator")
    root.config(bg="#8B78E6",bd=30,relief=SUNKEN)

    principal = StringVar()
    rate = StringVar()
    time = StringVar()
    answer = StringVar()

    Label(root,text="Calculate Your Simple Interest!!!!",
          font="Algerian 28 bold",bg="black",fg="#01CBC6",
          bd=20,relief=GROOVE).pack(padx=10,pady=10)

    label_principle = Label(root,text="Enter The Principal Amount",
    font = "Verdana 16 bold", bg = "black", fg = "#01CBC6",
                                                  bd = 18,relief=RAISED)
    label_principle.place(x=25,y=100)

    label_rate = Label(root,text="Enter The Rate",
    font = "Verdana 16 bold", bg = "black", fg = "#01CBC6",
                                                  bd = 18,relief=RAISED)
    label_rate.place(x=25,y=200)

    label_time = Label(root,text="Enter The Time",
    font = "Verdana 16 bold", bg = "black", fg = "#01CBC6",
                                                  bd = 18,relief=RAISED)
    label_time.place(x=25,y=300)


    ent_principal = Entry(root,font="Calibri 20 bold",bd=12,
                      relief=SUNKEN,fg="#01CBC6",bg="black",justify=CENTER,textvariable=principal)
    ent_principal.place(y=102,x=400)

    ent_rate = Entry(root,font="Calibri 20 bold",bd=12,
                      relief=SUNKEN,fg="#01CBC6",bg="black",justify=CENTER,textvariable=rate)
    ent_rate.place(y=202,x=250)

    ent_time = Entry(root,font="Calibri 20 bold",bd=12,
                      relief=SUNKEN,fg="#01CBC6",bg="black",justify=CENTER,textvariable=time)
    ent_time.place(y=302,x=250)

    enter_button = Button(root,text="Enter!!",
                       font="Calibri 20 bold",bd=12,relief=SUNKEN,fg="#01CBC6",bg="black",command=result)
    enter_button.place(x=375,y=400)

    reset_button = Button(root,text="Reset!!",
                       font="Calibri 20 bold",bd=12,relief=SUNKEN,fg="#01CBC6",bg="black",command=res)
    reset_button.place(x=225,y=400)

    enter_button = Button(root,text="Quit!!!",
                       font="Calibri 20 bold",bd=12,relief=SUNKEN,fg="#01CBC6",bg="black",command=Quit)
    enter_button.place(x=525,y=400)


    label_answer = Label(root,text="Your Simple Interset",
    font = "Verdana 16 bold", bg = "black", fg = "#01CBC6",
                                                  bd = 18,relief=RAISED)
    label_answer.place(x=25,y=500)

    ent_answer = Entry(root,font="Calibri 20 bold",bd=12,
                      relief=SUNKEN,fg="#01CBC6",bg="black",justify=CENTER,textvariable=answer)
    ent_answer.place(y=502,x=325)













    root.mainloop()