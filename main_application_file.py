from tkinter import *
from tkinter.ttk import Style
from tkinter.messagebox import *
import random
from db import DBConnect
from listComp import ListComp
import back

#Public log in
def complaint_management():
    # root.destroy()  
    conn = DBConnect()
    root1 = Tk()
    root1.geometry('600x325')
    root1.title('Complaint Management System')
    root1.configure(background='light blue')

    #Style
    style = Style()
    style.theme_use('classic')
    for elem in ['TLabel', 'TButton', 'TRadioutton']:
    	style.configure(elem, background='lightblue')

    #Gridx1353
    labels = ['Full Name:','Gender:','Phone No.:','Adhar No.:', 'Complaint:']
    for i in range(5):
    	Label(root1, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)

    BuList = Button(root1, text='List Complaints')
    BuList.grid(row=6, column=1)
    BuSubmit = Button(root1, text='Submit Now')
    BuSubmit.grid(row=6, column=2)


    #Entries
    fullname = Entry(root1, width=40, font=('Arial', 14))
    fullname.grid(row=0, column=1, columnspan=2)
    SpanGender = StringVar()
    Radiobutton(root1, text='Male', value='male', variable=SpanGender).grid(row=1, column=1)
    Radiobutton(root1, text='Female', value='female', variable=SpanGender).grid(row=1, column=2)

    #Phone and Adhar Addition...jump in sequence with tab key
    phone_entry = Entry(root1, width=20, font=('Arial', 14))
    phone_entry.grid(row=2, column=1)
    # phone_button = Button(root1, text='Verify')
    # phone_button.grid(row=2, column=2)
    adhar_entry = Entry(root1, width=20, font=('Arial', 14))
    adhar_entry.grid(row=3, column=1)
    # adhar_button = Button(root1, text='Verify')
    # adhar_button.grid(row=3, column=2)

# comment = Text(root1, width=35, height=3, font=('Arial', 14))
# comment.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

    Complaint = Text(root1, width=35,height=3,font=('Arial', 14))
    Complaint.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
    #Unable to add placeholder in text area of complaint
    # Complaint.insert(0,"Enter your complete information including occupation and addreess followed by complaint.")
    # Complaint.configure(state=DISABLED)
    def SaveData():
    	msg = conn.Add(fullname.get(), SpanGender.get(),phone_entry.get(),adhar_entry.get(),Complaint.get(1.0, 'end'))
    	fullname.delete(0, 'end')
    	phone_entry.delete(0,'end') #Delete text after submission
    	adhar_entry.delete(0,'end')
    	Complaint.delete(1.0, 'end')
    	showinfo(title='Add Info', message=msg)

    def ShowList():
    	listrequest = ListComp()


    BuSubmit.config(command=SaveData)
    BuList.config(command=ShowList)

    root1.mainloop()

#official log in 
def click():
    text_entry=textentry.get()
    if text_entry == "123" :
        print("Login Approved")
        root.destroy()
        # import os
        # os.system('front.py')
        window=Tk()
        pic=PhotoImage(file="logo.gif")
        label2=Label(window,image=pic).grid(row=0,column=4,rowspan=7,columnspan=5)
        def viewcommand():
            list1.delete(0,END)
            for crime_record in back.view():
                list1.insert(END,crime_record)

        def searchcommand():
            list1.delete(0,END)
            for crime_record in back.search(Criminal_id_text.get(),Name_text.get(),Gender_text.get(),Nationality_text.get(),Age_text.get(),Height_text.get(),Weight_text.get(),Crime_Committed_text.get()):
                list1.insert(END,crime_record)

        def insertcommand():
            back.insert(Criminal_id_text.get(),Name_text.get(),Gender_text.get(),Nationality_text.get(),Age_text.get(),Height_text.get(),Weight_text.get(),Crime_Committed_text.get())
            list1.delete(0,END)
            list1.insert(END,(Criminal_id_text.get(),Name_text.get(),Gender_text.get(),Nationality_text.get(),Age_text.get(),Height_text.get(),Weight_text.get(),Crime_Committed_text.get()))

        def get_selected_row(event):
            try:
                global selected_tuple
                index=list1.curselection()[0]
                selected_tuple=list1.get(index)
                e1.delete(0,END)
                e1.insert(END,selected_tuple[0])
                e2.delete(0,END)
                e2.insert(END,selected_tuple[1])
                e3.delete(0,END)
                e3.insert(END,selected_tuple[2])
                e4.delete(0,END)
                e4.insert(END,selected_tuple[3])
                e5.delete(0, END)
                e5.insert(END, selected_tuple[4])
                e6.delete(0, END)
                e6.insert(END, selected_tuple[5])
                e7.delete(0, END)
                e7.insert(END, selected_tuple[6])
                e8.delete(0, END)
                e8.insert(END, selected_tuple[7])
            except IndexError:
                pass

        def deletecommand():
            back.delete(selected_tuple[0])
            viewcommand()

        def updatecommand():
            back.update( Criminal_id_text.get(), Name_text.get(), Gender_text.get(), Nationality_text.get(),Age_text.get(),Height_text.get(),Weight_text.get(),Crime_Committed_text.get() )
            searchcommand()

        window.wm_title("CRIMINAL RECORD DATABASE")

        l1=Label(window,text="Criminal_ID")
        l1.grid(row=0,column=0)

        l2=Label(window,text="Name")
        l2.grid(row=0,column=2)

        l3=Label(window,text="Gender")
        l3.grid(row=1,column=0)

        l4=Label(window,text="Nationality")
        l4.grid(row=1,column=2)

        l5=Label(window,text="Age")
        l5.grid(row=2,column=0)

        l6=Label(window,text="Height(foot)")
        l6.grid(row=2,column=2)

        l7=Label(window,text="Weight(kg)")
        l7.grid(row=3,column=0)

        l8=Label(window,text="Crime_Committed")
        l8.grid(row=3,column=2)

        Criminal_id_text=StringVar()
        e1=Entry(window,textvariable=Criminal_id_text)
        e1.grid(row=0,column=1)

        Name_text=StringVar()
        e2=Entry(window,textvariable=Name_text)
        e2.grid(row=0,column=3)

        Gender_text=StringVar()
        e3=Entry(window,textvariable=Gender_text)
        e3.grid(row=1,column=1)

        Nationality_text=StringVar()
        e4=Entry(window,textvariable=Nationality_text)
        e4.grid(row=1,column=3)

        Age_text=StringVar()
        e5=Entry(window,textvariable=Age_text)
        e5.grid(row=2,column=1)

        Height_text=StringVar()
        e6=Entry(window,textvariable=Height_text)
        e6.grid(row=2,column=3)

        Weight_text=StringVar()
        e7=Entry(window,textvariable=Weight_text)
        e7.grid(row=3,column=1)

        Crime_Committed_text=StringVar()
        e8=Entry(window,textvariable=Crime_Committed_text)
        e8.grid(row=3,column=3)

        list1=Listbox(window,height=10,width=35)
        list1.grid(row=4,column=0,rowspan=10,columnspan=2,pady=4)
        list1.bind('<<ListboxSelect>>',get_selected_row)

        scr=Scrollbar(window)
        scr.grid(row=4,column=2,rowspan=6)

        list1.configure(yscrollcommand=scr.set)
        scr.configure(command=list1.yview)

        b1=Button(window,text="View all",width=12,command=viewcommand)
        b1.grid(row=4,column=3)

        b2=Button(window,text="Search entry",width=12,command=searchcommand)
        b2.grid(row=5,column=3)

        b3=Button(window,text="Add entry",width=12,command=insertcommand)
        b3.grid(row=6,column=3)

        b4=Button(window,text="Update",width=12,command=updatecommand)
        b4.grid(row=7,column=3)

        b5=Button(window,text="Delete",width=12,command=deletecommand)
        b5.grid(row=8,column=3)

        b6=Button(window,text="Close",width=12,command=window.destroy)
        b6.grid(row=9,column=3)
        def ShowList():   #For listing complaints of public in official log in
    	    listrequest = ListComp()

        b6=Button(window,text="List Complaints",width=12,command=ShowList)
        b6.grid(row=9,column=4)

        window.mainloop()

    else :
        print("Access Denied")
        label1=Label(bottomFrame,text="Wrong Password. Try again",fg="black",bg="red")
        label1.grid(row=1,column=1)
colors = ['green','black','purple']
# colors = ['dark red','green','black','red2','gold2','indianred1','sienna1','orange2','darkorchid1','cornflower blue','saddle brown','cornsilk3','steelblue4']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(1000,IntroLabelColorTick)

def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(300,IntroLabelTick)




root = Tk()
root.title("Login Window")
root.geometry("560x530+00+00")
root.configure(background = "dark blue")

topFrame = Frame(root,bg="light blue")
topFrame.pack()
ss = 'Criminal \nFinder\n Application'
count = 0
text = ''
SliderLabel = Label(root,text=ss,font=('Times new roman',17,'italic bold'),relief=RIDGE,borderwidth=0,width=17,bg='light blue')
# SliderLabel = Label(root,text=ss,font=('Times new roman',20,'italic bold'),relief=RIDGE,borderwidth=4,width=18,bg='linen')
SliderLabel.place(x=272,y=20)
IntroLabelTick()
IntroLabelColorTick()

bottomFrame = Frame(root)
bottomFrame.pack(side =BOTTOM)
photo = PhotoImage(file = "police_logo.png")
Label(topFrame ,image = photo).grid(row=1 ,column = 1 ,sticky = W)
# label = Label(topFrame, text="CRIMINAL \n RECORD \n DATABASE ",fg="black",bg="light blue",font=(None, 25)).grid(row=1,column = 3,sticky= E)


# Label(topFrame, text="Enter Password",fg="black",bg="light blue",font=(None, 15)).grid(row=4,column=3)
# textentry = Entry(topFrame , width =30 ,fg="black" ,bg="white",show = "*")
# textentry.grid(row=5, column = 3,sticky=W)
# Button(topFrame ,text="Submit",width=10 ,command = click).grid(row=6,column=3,sticky=W)

# pass_label=Label(root,text="Enter Password",font=('Times new roman',15,'italic bold'),relief=RIDGE,borderwidth=0,width=30,bg='light blue')
# pass_label.place(x=100,y=230)

#Official log in
# SliderLabel = Label(root,text=ss,font=('Times new roman',20,'italic bold'),relief=RIDGE,borderwidth=0,width=17,bg='light blue')

Label(topFrame, text="OFFICIAL LOG IN",bg="light blue",font=('Times new roman',15,'bold')).grid(row=4,column=1,sticky=NW)
# Label(topFrame, text="OFFICIAL LOG IN",fg="black",bg="light blue",font=(,font=('Times new roman',15,'italic bold')).grid(row=4,column=1,sticky=NW)
Label(topFrame, text="Enter Password",bg="light blue",font=('Times new roman',11,'italic')).grid(row=5,column=1,sticky=SW)
textentry = Entry(topFrame , width =15 ,fg="black" ,bg="white",show = "*")
textentry.grid(row=6, column = 1,sticky=W)
Button(topFrame ,text="Log In",width=10 ,command = click).grid(row=7,column=1,sticky=W)

#Public log in
Label(topFrame, text="                  PUBLIC LOG IN",bg="light blue",font=('Times new roman',15,'bold')).grid(row=4,column=2,sticky=NE)
Label(topFrame, text="                  Enter Name",bg="light blue",font=('Times new roman',11,'italic')).grid(row=5,column=2,sticky=S)
# Label(topFrame, text="                  Click below to log in publicly",bg="light blue",font=('Times new roman',11,'italic')).grid(row=5,column=2,sticky=SE)
textentry_public = Entry(topFrame , width =18 ,fg="black" ,bg="white")
textentry_public.grid(row=6, column = 2,sticky=E)

Button(topFrame ,text="Log In",width=10,command = complaint_management).grid(row=7,column=2,sticky=E)


def close():
    exit()
Label(bottomFrame,text="Caution: Information entered  incorrectly by a agency \n representaion  in Database will be reflected on the ultimate \n report. UK Police will make corrections requested by the person \nat any point before the ultimate report is issued.",fg="red",bg="white").grid(row=6 ,column=1,sticky=W)
Button(bottomFrame,text="Click to Exit",width=10,command=close).grid(row = 7,column =1,sticky = S)



root.mainloop()
