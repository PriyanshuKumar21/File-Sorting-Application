from tkinter import *

root=Tk()
root.title("Notification App")
root.geometry("600x300+100+100")
root.resizable(True,True)
root.config(bg="#262626")

gender1=Label(root,text="Select gender: ",font=("times new roman",20,"bold"),bg="black",fg="white").pack()

def genderfunc():
    print(gender.get())

gender=StringVar()
male=Radiobutton(root,text="MALE",value="male",variable=gender,font=("times new roman",17,"bold"),bg="black",fg="white").place(x=225,y=50)
female=Radiobutton(root,text="FEMALE",value="female",variable=gender,font=("times new roman",17,"bold"),bg="black",fg="white").place(x=225,y=80)
gender.set("male")
btn3=Button(root,text="Submit",font=("timesnewroman",10,"bold"),command=genderfunc,bg="gray",fg="white",activebackground="Black",activeforeground="white",cursor="hand2").place(x=225,y=120)

root.mainloop()