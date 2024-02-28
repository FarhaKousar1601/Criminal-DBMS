from tkinter import *
import back
window=Tk()
pic=PhotoImage(file="logo.gif")
label2=Label(window,image=pic).grid(row=0,column=4,rowspan=7,columnspan=5)
#pic1=PhotoImage(file="NYPD.gif")
#label2=Label(window,image=pic1).grid(row=7,column=4,rowspan=5,columnspan=5)
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

window.mainloop()
