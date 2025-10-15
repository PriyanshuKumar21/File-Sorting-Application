from tkinter import *

root=Tk()
root.title("User Entry Form")
root.geometry("300x300+450+150")
root.resizable(False,False)
root.config(bg="white")

lbl1=Label(root,text="User Entry Form",font=("timesneroman",10),bg="white",fg="red",bd=10,borderwidth=3,relief=SOLID).pack(fill=X)

def show():
 if confirmcheck.get()==1:
    lblresult="Username: "+showlbl.get()+","+"\nEmail: "+showeml.get()+","+"\nGender: "+showgen.get()
    result.config(text=str(lblresult))
    print(confirmcheck.get())
    print(showlbl.get())
    print(showeml.get())
    print(showgen.get())
 else:
   result.config(text="Please Accept our \nTerms and Conditions to continue")
   

showlbl=StringVar()
showeml=StringVar()
showgen=StringVar()

userlbl=Label(root,text="Username",font=("timesneroman",10,"bold"),bg="white",fg="black")
userlbl.place(x=50,y=30)
userent=Entry(root,font=("timesneroman",10),textvariable=showlbl,bg="white",fg="black")
userent.place(x=120,y=32)

emllbl=Label(root,text="Email",font=("timesneroman",10,"bold"),bg="white",fg="black").place(x=50,y=75)
emlent=Entry(root,font=("timesneroman",10),textvariable=showeml,bg="white",fg="black")
emlent.place(x=120,y=77)

genlbl=Label(root,text="Gender",font=("timesneroman",10,"bold"),bg="white",fg="black").place(x=50,y=120)
male=Radiobutton(root,text="Male",value="male",font=("timesneroman",10),bg="white",fg="black",variable=showgen).place(x=120,y=120)
female=Radiobutton(root,text="Female",value="female",font=("timesneroman",10),bg="white",fg="black",variable=showgen).place(x=180,y=120)


confirmcheck=IntVar()
acpt=Checkbutton(root,text="Accept our Terms and Conditions",font=("timesneroman",10),onvalue=1,offvalue=0,variable=confirmcheck,bg="white",fg="black").place(x=50,y=160)
confirmcheck.set("0")

btn=Button(root,text="SHOW",font=("timesneroman",10,"bold"),bd=2,relief=SOLID,bg="lightGray",fg="black",command=show).place(x=120,y=200)

result=Label(root,text="",font=("timesneroman",10,"bold"),bg="Black",fg="White")
result.place(x=40,y=230)

root.mainloop()