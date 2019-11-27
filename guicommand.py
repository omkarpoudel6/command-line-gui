from tkinter import *
root=Tk()
root.title("Command Gui")
root.geometry("650x600")
root.resizable(0,0)
root.config(background="black")

lbl1=Label(root,text="#######################################################################",background="black",fg="yellow",padx=10,pady=10,font="TkFixedFont")
lbl1.pack(fill=X)

credir=Button(root,text="Create Directory",fg="white",background="black",padx=10, pady=10,font="TkFixedFont")
credir.pack(fill=X)

lbl2=Label(root,text="***********************************************************************",font="TkFixedFont",background="black",fg="green",padx=10,pady=10)
lbl2.pack(fill=X)

test=Button(root,text="Test Connection",background="black", fg="white", padx=10, pady=10,font="TkFixedFont")
test.pack(fill=X)

lbl3=Label(root,text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",background="black",fg="red",padx=10,pady=10,font="TkFixedFont")
lbl3.pack(fill=X)

checkip=Button(root,text="Find Your IP",background="black", fg="white", padx=10, pady=10,font="TkFixedFont")
checkip.pack(fill=X)

lbl4=Label(root,text="$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",background="black",fg="blue",padx=10,pady=10,font="TkFixedFont")
lbl4.pack(fill=X)

traceip=Button(root,text="Find IP Information",background="black", fg="white", padx=10, pady=10,font="TkFixedFont")
traceip.pack(fill=X)

lbl4=Label(root,text="!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",background="black",fg="pink",padx=10,pady=10,font="TkFixedFont")
lbl4.pack(fill=X)

openurl=Button(root,text="Visit Website",background="black", fg="white", padx=10, pady=10,font="TkFixedFont")
openurl.pack(fill=X)

lbl5=Label(root,text="<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>",font="TkFixedFont",background="black",fg="violet",padx=10,pady=10)
lbl5.pack(fill=X)

urlip=Button(root,text="Find IP of any URL",background="black", fg="white", padx=10, pady=10,font="TkFixedFont")
urlip.pack(fill=X)

lbl2=Label(root,text="++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",font="TkFixedFont",background="black",fg="purple",padx=10,pady=10)
lbl2.pack(fill=X)

terminal=Button(root,text="Open Terminal",background="black", fg="white", padx=10, pady=10,font="TkFixedFont")
terminal.pack(fill=X)

root.mainloop()