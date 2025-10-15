from tkinter import *

root=Tk()
root.title("Notification App")
root.geometry("500x300+100+100")
root.resizable(True,True)
root.config(bg="#262626")

def getname2():
    print(description.get('1.0',END)) 
    vardata.set(str(description.get('1.0',END))) #can only store the data of text class in another variable
    print(vardata.get()) # will show error if text class is directly used
    result.config(text=str(vardata.get())) # will show error if text class(description) is directly used
    

vardata=StringVar()
btn2=Button(root,text="Submit",font=("timesnewroman",10,"bold"),bg="gray",fg="white",activebackground="Black",activeforeground="white",cursor="hand2",command=getname2).pack(pady=10)
description=Text(root)
description.place(x=210,y=150,width="150",height="50")

result=Label(root,font=("timesnewroman",20,"bold"),bg="white",fg="black")
result.pack()


root.mainloop()