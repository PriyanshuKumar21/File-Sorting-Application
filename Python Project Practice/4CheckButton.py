from tkinter import *

root=Tk()
root.title("Notification App")
root.geometry("600x300+100+100")
root.resizable(True,True)
root.config(bg="#262626")

def checkfunc():
    print(checkvar.get())

checkvar=IntVar() #can be string var but instead of on and off value being 1 and 0 they will be on and off
check=Checkbutton(root,text="Accept or not.",font=("timesnewroman",10,"bold"),onvalue=1,offvalue=0,variable=checkvar,bg="gray",fg="white").place(x=225,y=80)
checkvar.set("0")
btn=Button(root,text="Submit",font=("timesnewroman",10,"bold"),command=checkfunc,bg="gray",fg="white",activebackground="Black",activeforeground="white",cursor="hand2").place(x=225,y=120) 

root.mainloop()