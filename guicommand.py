from tkinter import *
import socket
import os

def test1():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(("google.com",80))
        return 1;
    except:
        return 0;

def credir():
    def prints(a,b):
        print(a,b)

    credir=Toplevel(root)
    credir.title("Create Directory")
    credir.geometry("400x300")
    credir.resizable(0,0)
    credir.config(background="black")
    path=StringVar()
    name=StringVar()

    design=Label(credir,text=" ############################################",background="black",fg="Yellow",font="TkFixedFont")
    design.pack(fill =X)

    label1 = Label(credir, text="  Enter Path  ", background="black", fg="yellow", font="TkFixedFont")
    label1.pack(fill=X)

    entry1 = Entry(credir, background="black", fg="yellow", font="TkFixedFont", textvariable=path)
    entry1.pack(fill=X)

    label2 = Label(credir, text=" ", background="black")
    label2.pack(fill=X)

    label3 = Label(credir, text="Directory Name", background="black", fg="yellow", font="TkFixedFont")
    label3.pack(fill=X)

    entry2 = Entry(credir, background="black", fg="yellow", font="TkFixedFont", textvariable=name)
    entry2.pack(fill=X)

    label4 = Label(credir, text=" ", background="black")
    label4.pack(fill=X)

    but = Button(credir, text=" Create ", background="white", fg="red", font="TkFixedFont",command=lambda: prints(path.get(), name.get()))
    but.pack()

    credir.mainloop()


def test():
    print("this will test internet connection")
    connection=StringVar()
    x=test1()
    if x==1:
        connection="There is internet access"
    else:
        connection="There is no internet access"

    test=Toplevel(root)
    test.geometry("250x200")
    test.title("Test Connection")
    test.config(background="black")

    label1=Label(test,text="*******************************" ,fg="green",background="black",font="TkFixedFont")
    label1.pack(fill=X)

    label2=Label(test,text=" ",background="black")
    label2.pack(fill=X)

    label3=Label(test,text=connection,background="black",fg="green",font="TkFixedFont")
    label3.pack(fill=X)

    label4 = Label(test, text=" ", background="black")
    label4.pack(fill=X)

    but1=Button(test,text="Ok",fg="green",font="TkFixedFont",command=lambda: test.destroy())
    but1.pack()

    test.mainloop()


def checkip():
    print("Checks the ip address of the device")
    checkip=Toplevel(root)
    checkip.geometry("250x200")
    checkip.title("Check Ip")
    checkip.config(background="black")

    label1=Label(checkip,text="~~~~~~~~~~~~~~~~~~~~~~~~~~~",background="black",fg="red",font="TkFixedFont")
    label1.pack(fill=X)

    label2=Label(checkip,text=" ",background="black")
    label2.pack(fill=X)

    label3=Label(checkip,text="Your Ip : ",background="black",fg="red",font="TkFixedFont")
    label3.pack(fill=X)

    label4=Label(checkip,text=" ",background="black")
    label4.pack(fill=X)

    but=Button(checkip,text="Ok",fg="red",font="TkFixedFont",command=lambda: checkip.destroy())
    but.pack()

    checkip.mainloop()

def traceip():
    traceip=Toplevel(root)
    traceip.geometry("400x400")
    traceip.title("Find Ip Information")
    traceip.config(background="black")

    label1=Label(traceip,text="$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",background="black",fg="blue",font="TkFixedFont")
    label1.pack(fill=X)

    label2=Label(traceip,text=" ",background="black")
    label2.pack(fill=X)

    label3 = Label(traceip, text="Enter IP here", background="black", fg="blue", font="TkFixedFont")
    label3.pack(fill=X)

    ent = Entry(traceip, background="black", fg="blue", font="TkFixedFont")
    ent.pack(fill=X)

    label4 = Label(traceip, text=" ", background="black")
    label4.pack(fill=X)

    but1 = Button(traceip, text="Find", fg="blue", font="TkFixedFont")
    but1.pack()

    traceip.mainloop()

def openurl():
    openurl=Toplevel(root)
    openurl.geometry("300x300")
    openurl.title("Visit Website")
    openurl.config(background="black")

    label1=Label(openurl,text="!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", background="black",fg="pink",font="TkFixedFont")
    label1.pack(fill=X)

    label2=Label(openurl,text=" ",background="black")
    label2.pack(fill=X)

    label3 = Label(openurl, text="Enter URL Here", background="black", fg="pink", font="TkFixedFont")
    label3.pack(fill=X)

    ent = Entry(openurl, background="black", fg="pink", font="TkFixedFont")
    ent.pack(fill=X)

    label4 = Label(openurl, text=" ", background="black")
    label4.pack(fill=X)

    but = Button(openurl, text="OK", fg="pink", command=lambda: openurl.destroy(), background="black")
    but.pack()

    openurl.mainloop()

def urlip():
    urlip=Toplevel(root)
    urlip.geometry("300x300")
    urlip.title("Ip of URL")
    urlip.config(background="black")

    label1=Label(urlip,text="<><><><><><><><><><><><><><><><><>",background="black",fg="violet",font="TkFixedFont")
    label1.pack(fill=X)

    label2=Label(urlip,text=" ",background="black")
    label2.pack(fill=X)

    label3 = Label(urlip, text="Enter URL here", background="black", fg="violet", font="TkFixedFont")
    label3.pack(fill=X)

    label4 = Label(urlip, text=" ", background="black")
    label4.pack(fill=X)

    ent = Entry(urlip, background="black", fg="violet", font="TkFixedFont")
    ent.pack(fill=X)

    label5 = Label(urlip, text=" ", background="black")
    label5.pack(fill=X)

    label6 = Label(urlip, text="IP: ", background="black", fg="violet", font="TkFixedFont")
    label6.pack(fill=X)

    label7 = Label(urlip, text=" ", background="black")
    label7.pack(fill=X)

    but = Button(urlip, text="OK", fg="violet", font="TkFixedFont", command=lambda: urlip.destroy())
    but.pack()

    urlip.mainloop()


def openterminal():
    print("This will open the terminal")

root=Tk()
root.title("Command Gui")
root.geometry("650x600")
root.resizable(0,0)
root.config(background="black")

lbl1=Label(root,text="#######################################################################",background="black",fg="yellow",padx=10,pady=10,font="TkFixedFont")
lbl1.pack(fill=X)

credir=Button(root,text="Create Directory",fg="white",background="black",padx=10, pady=10,font="TkFixedFont",command=credir)
credir.pack(fill=X)

lbl2=Label(root,text="***********************************************************************",font="TkFixedFont",background="black",fg="green",padx=10,pady=10)
lbl2.pack(fill=X)

test=Button(root,text="Test Connection",background="black", fg="white", padx=10, pady=10,font="TkFixedFont", command=test)
test.pack(fill=X)

lbl3=Label(root,text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",background="black",fg="red",padx=10,pady=10,font="TkFixedFont")
lbl3.pack(fill=X)

checkip=Button(root,text="Find Your IP",background="black", fg="white", padx=10, pady=10,font="TkFixedFont",command=checkip)
checkip.pack(fill=X)

lbl4=Label(root,text="$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",background="black",fg="blue",padx=10,pady=10,font="TkFixedFont")
lbl4.pack(fill=X)

traceip=Button(root,text="Find IP Information",background="black", fg="white", padx=10, pady=10,font="TkFixedFont",command=traceip)
traceip.pack(fill=X)

lbl4=Label(root,text="!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",background="black",fg="pink",padx=10,pady=10,font="TkFixedFont")
lbl4.pack(fill=X)

openurl=Button(root,text="Visit Website",background="black", fg="white", padx=10, pady=10,font="TkFixedFont",command=openurl)
openurl.pack(fill=X)

lbl5=Label(root,text="<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>",font="TkFixedFont",background="black",fg="violet",padx=10,pady=10)
lbl5.pack(fill=X)

urlip=Button(root,text="Find IP of any URL",background="black", fg="white", padx=10, pady=10,font="TkFixedFont",command=urlip)
urlip.pack(fill=X)

lbl2=Label(root,text="++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",font="TkFixedFont",background="black",fg="purple",padx=10,pady=10)
lbl2.pack(fill=X)

terminal=Button(root,text="Open Terminal",background="black", fg="white", padx=10, pady=10,font="TkFixedFont",command=openterminal)
terminal.pack(fill=X)

root.mainloop()
