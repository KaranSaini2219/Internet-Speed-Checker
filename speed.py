from tkinter import *
import speedtest
def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+" Mbps"
    up= str(round(sp.upload()/(10**6),3))+" Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)    
sp=Tk()
sp.title("INTERNET SPEED TEST")
sp.geometry("500x650")
sp.config(bg="brown4")
lab=Label(sp,text="INTERNET SPEED TEST",font=("Comfortaa",25,"bold"),bg="burlywood",fg="black")
lab.place(x=60,y=40,height=30,width=380)

lab=Label(sp,text="DOWNLOAD SPEED",font=("Time New Roman",20,"bold"),bg="burlywood2",fg="black")
lab.place(x=60,y=130,height=30,width=380)

lab_down=Label(sp,text="00",font=("Time New Roman",20,"bold"),bg="burlywood2",fg="black")
lab_down.place(x=60,y=200,height=30,width=380)

lab=Label(sp,text="UPLOAD SPEED",font=("Time New Roman",20,"bold"),bg="burlywood2",fg="black")
lab.place(x=60,y=290,height=30,width=380)

lab_up=Label(sp,text="00",font=("Time New Roman",20,"bold"),bg="burlywood2",fg="black")
lab_up.place(x=60,y=360,height=30,width=380)

button=Button(sp,text="CHECK SPEED",font=("impact",25,"bold"),relief=RAISED,bg="chocolate1",command=speedcheck)
button.place(x=60,y=460,height=30,width=380)
sp.mainloop()