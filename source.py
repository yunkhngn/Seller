import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.font import BOLD

TITLE = "Phần Mềm Bán Hàng"

root = tk.Tk()
root.geometry("895x400")
root.title(TITLE)
root.resizable(False, False)

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)

# Pack a big frame so, it behaves like the window background
big_frame = ttk.Frame(root)
big_frame.pack(fill="both", expand=True)

inside_frame = ttk.Frame(big_frame)
inside_frame.pack(fill="both", expand=True, padx=10, pady=10)
# Set the initial theme
root.tk.call("source", "sun-valley.tcl")
root.tk.call("set_theme", "light")

def change_theme():
    # NOTE: The theme's real name is sun-valley-<mode>
    if root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
        # Set light theme
        root.tk.call("set_theme", "light")
    else:
        # Set dark theme
        root.tk.call("set_theme", "dark")

a=0
b=0
c=0
d=0
e=0
cc =0

def okkhoga():
    global a
    if var1.get() == 1:
        chickenSpin.config(state =NORMAL)
        a=1
    if var1.get() == 0:
        chickenSpin.delete(0,END)
        chickenSpin.config(state =DISABLED)
        a=0
def okkhobo():
    global b
    if var2.get() == 1:
        beefSpin.config(state =NORMAL)
        a=1
    if var2.get() == 0:
        beefSpin.delete(0,END)
        beefSpin.config(state =DISABLED)
        a=0
def okmucrim():
    global c
    if var3.get() == 1:
        squidSpin.config(state =NORMAL)
        a=1
    if var3.get() == 0:
        squidSpin.delete(0,END)
        squidSpin.config(state =DISABLED)
        a=0
def okgherim():
    global d
    if var4.get() == 1:
        gheSpin.config(state =NORMAL)
        a=1
    if var4.get() == 0:
        gheSpin.delete(0,END)
        gheSpin.config(state =DISABLED)
        a=0
def okkhoheo():
    global e
    if var5.get() == 1:
        PorkSpin.config(state =NORMAL)
        a=1
    if var5.get() == 0:
        PorkSpin.delete(0,END)
        PorkSpin.config(state =DISABLED)
        a=0
def delete():
    global cc
    cc = 0
    chickenSpin.delete(0,END)
    beefSpin.delete(0,END)
    squidSpin.delete(0,END)
    gheSpin.delete(0,END)
    PorkSpin.delete(0,END)
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    chickenSpin.config(state =DISABLED)
    beefSpin.config(state =DISABLED)
    squidSpin.config(state =DISABLED)
    gheSpin.config(state =DISABLED)
    PorkSpin.config(state =DISABLED)
title = ttk.Label(inside_frame, text="Phần mềm bán hàng vip pzo", font=("Arial", 20, BOLD))
title.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=(130,0))

changeLanguageButton = ttk.Button(inside_frame, text="Ngôn ngữ")
changeLanguageButton.grid(row=0, column=4, sticky="nsew", padx=10, pady=10)

changeThemeButton = ttk.Button(inside_frame, text="Theme", style="Accent.TButton", command=change_theme)
changeThemeButton.grid(row=0, column=5, sticky="nsew", padx=10, pady=10)

#Tab Cart
Cart = ttk.LabelFrame(inside_frame, text="Giỏ hàng")
Cart.grid(row=2, column=0, columnspan=2, sticky="nsew")

tabControl = ttk.Notebook(Cart)
tabControl.pack(fill="both", expand=True, padx=10, pady=10)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text ='Đồ ăn')
tabControl.add(tab2, text ='Đồ uống')
tabControl.pack(expand = 1, fill ="both")

#button
AddButton = ttk.Button(Cart, text="Thêm", width=10, style="Accent.TButton")
AddButton.pack(side="left", padx=10, pady=(0,10))

ClearButton = ttk.Button(Cart, text="Xóa", width=10, command=delete)
ClearButton.pack(side="left", padx=10, pady=(0,10))

HelpButton = ttk.Button(Cart, text="Trợ giúp", width=10)
HelpButton.pack(side="left", padx=10, pady=(0,10))

#Đồ ăn
food = ttk.Frame(tab1)
food.pack(fill="both", expand=True, padx=10, pady=10)

chickenFrame = ttk.Frame(food)
chickenFrame.pack(fill=X, expand=False, padx=10, pady=2)
chicken = ttk.Label(chickenFrame, text="Khô gà MIXI")
chicken.grid(row=0, column=0, sticky="nsew")
chickenSpin = ttk.Spinbox(chickenFrame, width=10, from_=0, to=100, state=DISABLED)
chickenSpin.grid(row=0, column=2, sticky=tk.NE, padx=(20,5))
chickenCheck = ttk.Checkbutton(chickenFrame, variable=var1, command=okkhoga)
chickenCheck.grid(row=0, column=3, sticky=tk.NE)

beefFrame = ttk.Frame(food)
beefFrame.pack(fill=X, expand=False, padx=10, pady=2)
beef = ttk.Label(beefFrame, text="Khô bò MIXI")
beef.grid(row=0, column=0, sticky="nsew")
beefSpin = ttk.Spinbox(beefFrame, width=10, from_=0, to=100, state=DISABLED)
beefSpin.grid(row=0, column=2, sticky=tk.NE, padx=(20,5))
beefCheck = ttk.Checkbutton(beefFrame, variable=var2, command=okkhobo)
beefCheck.grid(row=0, column=3, sticky=tk.NE)

squidFrame = ttk.Frame(food)
squidFrame.pack(fill=X, expand=False, padx=10, pady=2)
squid = ttk.Label(squidFrame, text="Mực rim MIXI")
squid.grid(row=0, column=0, sticky="nsew")
squidSpin = ttk.Spinbox(squidFrame, width=10, from_=0, to=100, state=DISABLED)
squidSpin.grid(row=0, column=2, sticky=tk.NE, padx=(20,5))
squidCheck = ttk.Checkbutton(squidFrame, variable=var3, command=okmucrim)
squidCheck.grid(row=0, column=3, sticky=tk.NE)

gheFrame = ttk.Frame(food)
gheFrame.pack(fill=X, expand=False, padx=10, pady=2)
ghe = ttk.Label(gheFrame, text="Ghẹ rim MIXI")
ghe.grid(row=0, column=0, sticky="nsew")
gheSpin = ttk.Spinbox(gheFrame, width=10, from_=0, to=100, state=DISABLED)
gheSpin.grid(row=0, column=2, sticky=tk.NE, padx=(20,5))
gheCheck = ttk.Checkbutton(gheFrame, variable=var4, command=okgherim)
gheCheck.grid(row=0, column=3, sticky=tk.NE)

PorkFrame = ttk.Frame(food)
PorkFrame.pack(fill=X, expand=False, padx=10, pady=2)
Pork = ttk.Label(PorkFrame, text="Khô heo MIXI")
Pork.grid(row=0, column=0, sticky="nsew")
PorkSpin = ttk.Spinbox(PorkFrame, width=10, from_=0, to=100, state=DISABLED)
PorkSpin.grid(row=0, column=2, sticky=tk.NE, padx=(20,5))
PorkCheck = ttk.Checkbutton(PorkFrame, variable=var5, command=okkhoheo)
PorkCheck.grid(row=0, column=3, sticky=tk.NE)

drink = ttk.Frame(tab2)
drink.pack(fill="both", expand=True, padx=10, pady=10)

milkTeaFrame = ttk.Frame(drink)
milkTeaFrame.pack(fill="both", expand=True, padx=10, pady=2)
milkTea = ttk.Label(milkTeaFrame, text="Trà sữa")
milkTea.grid(row=0, column=0, sticky="nsew")
milkTeaCheck = ttk.Checkbutton(milkTeaFrame, onvalue=1, offvalue=0)
milkTeaCheck.grid(row=0, column=3, sticky=tk.NE)
milkTeaSpin = ttk.Spinbox(milkTeaFrame, width=10, from_=0, to=100)
milkTeaSpin.grid(row=0, column=2, sticky=tk.NE, padx=(20,5))

#Tab Payment
Payment = ttk.LabelFrame(inside_frame, text="Thanh toán")
Payment.grid(row=2, column=2,columnspan=5, sticky="nsew", padx=10)

Table = ttk.Treeview(Payment, height=10, columns=("one", "two", "three", "four"))
Table.pack(fill="both", expand=True, padx=10, pady=10)

Table.column("#0", width=50)
Table.heading("#0", text="STT")
Table.column("one", width=100)
Table.heading("one", text="Tên")
Table.column("two", width=100)
Table.heading("two", text="Số lượng")
Table.column("three", width=100)
Table.heading("three", text="Đơn giá")
Table.column("four", width=100)
Table.heading("four", text="Thành tiền")


root.mainloop()