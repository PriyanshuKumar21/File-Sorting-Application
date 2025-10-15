# import tkinter
from tkinter import *

root=Tk()
root.title("Notification App")
root.geometry("800x500+100+100")
root.resizable(True,True)
root.config(bg="#262626")
def getname():
    result.config(text=str(ent.get()))
def getname2():
   copydescription.set(str(description.get('1.0',END)))
   result1.config(text=str(copydescription.get()))

#------GRID system-------
#lbl=Label(root,text="Grid").grid(row=0,column=0)

#------PACK system-------
lbl1=Label(root,text="Notification App",font=("timesnewroman",20,"bold"),bg="lightgreen",fg="darkgreen").pack(fill=X,padx=40)
lbl2=Label(root,text="For Your Daily Needs",font=("timesnewroman",15,"bold"),bg="lightgreen",fg="darkgreen",bd=10,relief=RAISED).pack(pady=20)
ent=Entry(root,font=("timesnewroman",15,"bold"),bg="white",fg="black")
ent.pack()

copydescription=StringVar() #creating a variable to store description data of Text class

btn=Button(root,text="Show",font=("timesnewroman",10,"bold"),bg="gray",fg="white",activebackground="Black",activeforeground="white",cursor="hand2",command=getname).pack(pady=10)
btn2=btn=Button(root,text="Submit",font=("timesnewroman",10,"bold"),bg="gray",fg="white",activebackground="Black",activeforeground="white",cursor="hand2",command=getname2).pack(pady=10)

description=Text(root)
description.place(x=325,y=300,width="150",height="50")

result=Label(root,font=("timesnewroman",20,"bold"),bg="white",fg="black")
result.pack()

result1=Label(root,font=("timesnewroman",15,"italic"),bg="white",fg="black")
result1.place(x=325,y=400,width="150",height="50")

root.mainloop()