from tkinter import *
from translate import Translator
def convert():
    v1=lang1.get()
    v2=lang2.get()
    v3=var1.get()
    T=Translator(from_lang=v1,to_lang=v2)
    output=T.translate(v3)
    var2.set(output)

root=Tk()
root.title("Language Translator")

Label(root,text="WELCOME TO MY TRANSLATOR",font="comicsans 25 bold",fg="white",bg="red").pack(side=TOP,fill=X)
f1=Frame(root,bg="blue",padx=45,pady=15,relief=RAISED)
f1.pack(side=TOP,pady=10)
Label(f1,text="Translator App",fg="red",font="arial 12 bold",relief=GROOVE,borderwidth=2,bg="yellow").grid(row=0,column=1,padx=2,pady=2,ipadx=2,ipady=2)
Label(f1,text="Select A Language",fg="red",font="arial 10 bold",bg="aqua",pady=5).grid(row=1,column=0,pady=5)
Label(f1,text="Select A Language",fg="red",font="arial 10 bold",bg="aqua",pady=5).grid(row=1,column=2,pady=5)
lang1=StringVar()
lang2=StringVar()
lang1.set("Choose")
lang2.set("Choose")
choices=["English", "German", "French", "Bengali" ,"Hindi","Spanish"]
menu1=OptionMenu(f1,lang1,*choices)
menu1.grid(row=2,column=0)
menu2=OptionMenu(f1,lang2,*choices)
menu2.grid(row=2,column=2)

Label(f1,text="Enter Text",font="arial 10 bold",fg="red",bg="aqua").grid(row=3,column=0,padx=5,pady=5,ipadx=3,ipady=3)
Label(f1,text="Output Text",font="arial 10 bold",fg="red",bg="aqua").grid(row=3,column=2,padx=5,pady=5,ipadx=3,ipady=3)

var1=StringVar()
var2=StringVar()
Entry(f1,textvariable=var1).grid(row=4,column=0)
Entry(f1,textvariable=var2).grid(row=4,column=2)
Button(f1,text="Submit",fg="red",bg="white",command=convert).grid(row=5,column=1,padx=2,pady=3,ipadx=2,ipady=2)


root.mainloop()