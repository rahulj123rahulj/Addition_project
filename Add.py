from tkinter import *
root=Tk()
root.title("Addition and multiplication")
root.geometry('330x290')
root.wm_minsize(width=330,height=290)
root.wm_maxsize(width=330,height=290)

def sum():
    a=int(e1.get())
    b=int(e2.get())
    s=a+b
    l4.config(text="sum of %d and %d is %d" % (a,b,s))

def mul():
    a=int(e1.get())
    b=int(e2.get())
    m=a*b
    l4.config(text="Multiplication of %d and %d is %d"%(a,b,m))

l1=Label(root,font=('calibri',15,'bold'))
l1.config(text='Addition of two Number')
l1.place(x=62,y=10)

l2=Label(root,text='first Number ',font=('calibri',12))
l2.place(x=10,y=80)
e1=Entry(root,font=('calibri',12),borderwidth=2,relief='solid')
e1.place(x=140,y=80)

l3=Label(root,text='second Number',font=('calibri',12))
l3.place(x=10,y=120)
e2=Entry(root,font=('calibri',12),borderwidth=2,relief='solid')
e2.place(x=140,y=120)

b1=Button(root,text="ADD",font=('calibri',10),bg='white',borderwidth=2,relief='solid',command=sum)
b1.place(x=100,y=170,width=80,height=30)

b2=Button(root,text="MULTIPLY",font=('calibri',10),bg='white',borderwidth=2,relief='solid',command=mul)
b2.place(x=200,y=170,width=80,height=30)

l4=Label(root,text='Result will soon',font=('calibri',12))
l4.place(x=20,y=240)

root.mainloop()
