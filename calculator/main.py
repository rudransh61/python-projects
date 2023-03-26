import tkinter as tk


def press(num):
    global exp
    exp = exp + str(num)
    ans.set(exp)
exp = ""

root=tk.Tk()
root.title("Calculator")
root.geometry("480x340")


def equal():
    try:
        global exp
        exp = eval(exp)
        ans.set(exp)
    except:
        exp = ""
        ans.set("error")

def clear():
    global exp
    exp = ""
    ans.set(exp)


ans = tk.StringVar()

eqn = tk.Entry(root,textvariable=ans)
eqn.grid(columnspan=4,ipadx=190,ipady=10)

b1 = tk.Button(root,text=1,height=3,width=10,command=lambda : press(1))
b1.grid(row=2,column=0)
b2 = tk.Button(root,text=2,height=3,width=10,command=lambda : press(2))
b2.grid(row=2,column=1)
b3 = tk.Button(root,text=3,height=3,width=10,command=lambda : press(3))
b3.grid(row=2,column=2)

b4 = tk.Button(root,text=4,height=3,width=10,command=lambda : press(4))
b4.grid(row=3,column=0)
b5 = tk.Button(root,text=5,height=3,width=10,command=lambda : press(5))
b5.grid(row=3,column=1)
b6 = tk.Button(root,text=6,height=3,width=10,command=lambda : press(6))
b6.grid(row=3,column=2)

b7 = tk.Button(root,text=7,height=3,width=10,command=lambda : press(7))
b7.grid(row=4,column=0)
b8 = tk.Button(root,text=8,height=3,width=10,command=lambda : press(8))
b8.grid(row=4,column=1)
b9 = tk.Button(root,text=9,height=3,width=10,command=lambda : press(9))
b9.grid(row=4,column=2)
b0 = tk.Button(root,text=0,height=3,width=10,command=lambda : press(0))
b0.grid(row=5,column=1)
be = tk.Button(root,text="=",height=3,width=10,command=lambda : equal())
be.grid(row=6,column=1)
bp = tk.Button(root,text="+",height=3,width=10,command=lambda : press("+"))
bp.grid(row=2,column=3)
bs = tk.Button(root,text="-",height=3,width=10,command=lambda : press("-"))
bs.grid(row=3,column=3)
bd = tk.Button(root,text="/",height=3,width=10,command=lambda : press("/"))
bd.grid(row=4,column=3)
bm = tk.Button(root,text="x",height=3,width=10,command=lambda : press("*"))
bm.grid(row=5,column=3)
bc = tk.Button(root,text="clear",height=3,width=10,command=lambda : clear())
bc.grid(row=6,column=3)


# print(b9["text"])


root.mainloop()