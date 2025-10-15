from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, filedialog, messagebox
import os,shutil

class Sorting_App:
    def __init__(self,root):
        self.root=root
        self.root.title("File Sorting Application | Developed By Priyanshu, Kamakshi, Jighyasa")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg="white")
        self.logo_icon=PhotoImage(file="GUI Test\logo1.png")
        self.logo=self.logo_icon.subsample(4,4)
        title=Label(self.root,text="FILE SORTING APPLICATION",image=self.logo,padx=10,compound=LEFT,font=("impact",40),bg="#023548",fg="white").place(x=0,y=0,relwidth=1)
        
        #-----Section 1------
        self.var_foldername=StringVar()
        lbl_select_folder=Label(self.root,text="Select Folder",font=("times new roman",17,"bold"),bg="white",fg="black").place(x=70,y=100)
        txt_folder_name=Entry(self.root,font=("times new roman",14,"bold"),textvariable=self.var_foldername,bg="gray",state='readonly').place(x=225,y=100,width=500)
        btn_browse=Button(self.root,command=self.browse_function,text="BROWSE",font=("times new roman",15,"bold"),bg="#262626",fg="white",activebackground="#262626",activeforeground="white",cursor="hand2").place(x=775,y=100,height=25)
        hr=Label(self.root,bg="black").place(x=50,y=150,height=1,width=1175)

        #------Section2------
        #-----ALL EXTENSIONS-----
        self.image_extensions=["Image Extensions",".png",".jpeg",".avif",".gif"]
        self.audio_extensions=["Audio Extensions",".mp3",".aac"]
        self.video_extensions=["Video Extensions",".mp4",".mpeg4",".avi",".3gp"]
        self.doc_extensions=["Document Extensions",".doc",".docx",".xlsx",".ppt",".pptx",".pdf",".txt",".xls",".zip",".csv","rar"]

        self.folders={
           'videos':self.video_extensions,
           'audios':self.audio_extensions,
           'images':self.image_extensions,
           'documents':self.doc_extensions
           }

        lbl_select_ext=Label(self.root,text="Various Supported Extensions",font=("times new roman",25,"bold"),bg="white",fg="black").place(x=70,y=170)
        self.image_box=ttk.Combobox(self.root,values=self.image_extensions,font=("times new roman",20),state='readonly',justify=CENTER)
        self.image_box.place(x=70,y=230,width=250)
        self.image_box.current(0)

        self.Audio_box=ttk.Combobox(self.root,values=self.audio_extensions,font=("times new roman",20),state='readonly',justify=CENTER)
        self.Audio_box.place(x=350,y=230,width=250)
        self.Audio_box.current(0)

        self.Video_box=ttk.Combobox(self.root,values=self.video_extensions,font=("times new roman",20),state='readonly',justify=CENTER)
        self.Video_box.place(x=630,y=230,width=250)
        self.Video_box.current(0)

        self.Doc_box=ttk.Combobox(self.root,values=self.doc_extensions,font=("times new roman",20),state='readonly',justify=CENTER)
        self.Doc_box.place(x=910,y=230,width=250)
        self.Doc_box.current(0)

        #-------Section3-------
        #-----All Image Icon------
        self.image_icon=PhotoImage(file="GUI Test\imagelogo.png")
        self.imagelogo=self.image_icon.subsample(7,7)

        self.audio_icon=PhotoImage(file="GUI Test\oaudiologo.png")
        self.audiologo=self.audio_icon.subsample(3,3)

        self.video_icon=PhotoImage(file="GUI Test\ovideologo.png")
        self.videologo=self.video_icon.subsample(4,4)

        self.doc_icon=PhotoImage(file="GUI Test\doclogo.png")
        self.doclogo=self.doc_icon.subsample(3,3)

        self.other_icon=PhotoImage(file="GUI Test\otherlogo.png")
        self.otherlogo=self.other_icon.subsample(3,3)

        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=70,y=300,width=1150,height=275)
        self.lbl_total_files=Label(Frame1,text="Total Files: ",font=("times new roman",20),bg="white")
        self.lbl_total_files.place(x=10,y=5)

        self.lbl_image=Label(Frame1,text="Total Images\n0",bd=2,relief=RAISED,image=self.imagelogo,compound=TOP,font=("times new roman",15,"bold"),bg="darkorange",fg="black")
        self.lbl_image.place(x=20,y=50,width=200,height=200)

        self.lbl_audio=Label(Frame1,text="Total Audios\n0",bd=2,relief=RAISED,image=self.audiologo,compound=TOP,font=("times new roman",15,"bold"),bg="lightblue",fg="black")
        self.lbl_audio.place(x=240,y=50,width=200,height=200)

        self.lbl_video=Label(Frame1,text="Total Videos\n0",bd=2,relief=RAISED,image=self.videologo,compound=TOP,font=("times new roman",15,"bold"),bg="purple",fg="black")
        self.lbl_video.place(x=460,y=50,width=200,height=200)

        self.lbl_doc=Label(Frame1,text="Total Documents\n0",bd=2,relief=RAISED,image=self.doclogo,compound=TOP,font=("times new roman",15,"bold"),bg="lightblue",fg="black")
        self.lbl_doc.place(x=680,y=50,width=200,height=200)

        self.lbl_other=Label(Frame1,text="Other Files\n0",bd=2,relief=RAISED,image=self.otherlogo,compound=TOP,font=("times new roman",15,"bold"),bg="coral",fg="black")
        self.lbl_other.place(x=900,y=50,width=200,height=200)

        #--------Section4-------

        #------TEXT------

        self.lbl_status=Label(self.root,text="STATUS",font=("times new roman",23),bg="white",fg="black")
        self.lbl_status.place(x=70,y=580)

        self.lbl_total=Label(self.root,text="",font=("times new roman",21),bg="white",fg="black")
        self.lbl_total.place(x=240,y=580)
        self.lbl_moved=Label(self.root,text="",font=("times new roman",21),bg="white",fg="black")
        self.lbl_moved.place(x=420,y=580)
        self.lbl_left=Label(self.root,text="",font=("times new roman",21),bg="white",fg="black")
        self.lbl_left.place(x=600,y=580)

        #-------BUTTONS------

        self.btn_clear=Button(self.root,command=self.clear,text="CLEAR",font=("times new roman",15,"bold"),bd=3,relief=RAISED,bg="#607d8b",fg="white",activebackground="#262626",activeforeground="white",cursor="hand2") 
        self.btn_clear.place(x=950,y=590,height=30,width=120)
        self.btn_start=Button(self.root,command=self.start_function,state=DISABLED,text="START",font=("times new roman",15,"bold"),bd=3,relief=RAISED,bg="orange",fg="white",activebackground="#ff5722",activeforeground="white",cursor="hand2")
        self.btn_start.place(x=1075,y=590,height=30,width=120)

    def Total_count(self):
        images=0
        audios=0
        videos=0
        documents=0
        others=0  
        self.count=0
        combine_list=[]
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry,i))==True:
                self.count+=1
                ext="."+i.split(".")[-1]
                for folder_name in self.folders.items():
                    for x in folder_name[1]:
                        combine_list.append(x)
                    if ext.lower() in folder_name[1] and folder_name[0]=="images":
                        images+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="audios":
                        audios+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="videos":
                        videos+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="documents":
                        documents+=1

            #This is for Others Folder count            
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directry,i))==True:
                   ext="."+i.split(".")[-1]
                   if ext.lower() not in combine_list:
                       others+=1 
                    
            self.lbl_image.config(text="Total Images\n"+str(images))
            self.lbl_audio.config(text="Total Audios\n3")
            self.lbl_video.config(text="Total Videos\n"+str(videos))
            self.lbl_doc.config(text="Total Documents\n"+str(documents))
            self.lbl_other.config(text="Total Others\n4")
            self.lbl_total_files.config(text="Total Files: "+str(self.count))

    def browse_function(self):
        op=filedialog.askdirectory(title="SELECT FOLDER FOR SORTING")
        if op!=None:
            #print(op)
            self.var_foldername.set(str(op))
            self.directry=self.var_foldername.get()
            self.other_name="others"
            self.rename_folder()
            self.all_files=os.listdir(self.directry)
            length=len(self.all_files)
            count=1
            self.Total_count()
            self.btn_start.config(state=NORMAL)
            # print(self.all_files)
            
    def start_function(self):
        if self.var_foldername.get()!="":
            self.btn_clear.config(state=DISABLED)
            self.btn_start.config(state=NORMAL)
            c=0
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directry,i))==True:
                    c+=1
                    self.create_move(i.split(".")[-1],i)
                    self.lbl_total.config(text="Total: "+str(self.count))
                    self.lbl_moved.config(text="Moved: "+str(c))   
                    self.lbl_left.config(text="Left: "+str(self.count-c))   

                    self.lbl_total.update()
                    self.lbl_moved. update()  
                    self.lbl_left.update()   
                    
            messagebox.showinfo("Success","All Files have moved succesfully")  
            self.btn_start.config(state=DISABLED)
            self.btn_clear.config(state=NORMAL)
        else:
            messagebox.showerror("Error","Please select folder")              


    def rename_folder(self):
        for folder in os.listdir(self.directry):
            if os.path.isdir(os.path.join(self.directry,folder))==True:
                os.rename(os.path.join(self.directry, folder),os.path.join(self.directry,folder.lower()))
    
    def create_move(self,ext,file_name):
        find=FALSE
        for folder_name in self.folders:
            if "."+ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directry):
                    os.mkdir(os.path.join(self.directry,folder_name))
                shutil.move(os.path.join(self.directry,file_name),os.path.join(self.directry,folder_name))
                find=TRUE
                break
        if find!=True:
            if self.other_name not in os.listdir(self.directry):
                os.mkdir(os.path.join(self.directry,self.other_name))
            shutil.move(os.path.join(self.directry,file_name), os.path.join(self.directry,self.other_name))

    def clear(self):
        self.btn_start.config(state=DISABLED)
        self.var_foldername.set("")
        self.lbl_total.config(text="")
        self.lbl_moved.config(text="")
        self.lbl_left.config(text="")
        self.lbl_image.config(text="")
        self.lbl_video.config(text="")
        self.lbl_audio.config(text="")
        self.lbl_doc.config(text="")
        self.lbl_other.config(text="")
        self.lbl_total_files.config(text="Total Files")

            

root=Tk()
obj=Sorting_App(root)

root.mainloop()