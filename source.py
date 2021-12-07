import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.font import BOLD

TITLE = "Bán Hàng"

root = tk.Tk()
root.geometry("895x400")
root.title(TITLE)
root.resizable(False, False)

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

title = ttk.Label(inside_frame, text="Phần mềm bán hàng vip pzo", font=("Arial", 20, BOLD))
title.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=(130,0))

changeLanguageButton = ttk.Button(inside_frame, text="Ngôn ngữ")
changeLanguageButton.grid(row=0, column=4, sticky="nsew", padx=10, pady=10)

changeThemeButton = ttk.Button(inside_frame, text="Theme", style="Accent.TButton")
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

ClearButton = ttk.Button(Cart, text="Xóa", width=10)
ClearButton.pack(side="left", padx=10, pady=(0,10))

HelpButton = ttk.Button(Cart, text="Trợ giúp", width=10)
HelpButton.pack(side="left", padx=10, pady=(0,10))

#Đồ ăn
food = ttk.Frame(tab1)
food.pack(fill="both", expand=True, padx=10, pady=10)

chickenFrame = ttk.Frame(food)
chickenFrame.pack(fill="both", expand=True, padx=10, pady=2)
chicken = ttk.Label(chickenFrame, text="Khô gà Mí Xì")
chicken.grid(row=0, column=0, sticky="nsew")
chickenCheck = ttk.Checkbutton(chickenFrame, onvalue=1, offvalue=0)
chickenCheck.grid(row=0, column=3, sticky="nsew")
chickenSpin = ttk.Spinbox(chickenFrame, width=10, from_=0, to=100)
chickenSpin.grid(row=0, column=2, sticky="nsew", padx=(20,5))

drink = ttk.Frame(tab2)
drink.pack(fill="both", expand=True, padx=10, pady=10)

milkTeaFrame = ttk.Frame(drink)
milkTeaFrame.pack(fill="both", expand=True, padx=10, pady=2)
milkTea = ttk.Label(milkTeaFrame, text="Trà sữa")
milkTea.grid(row=0, column=0, sticky="nsew")
milkTeaCheck = ttk.Checkbutton(milkTeaFrame, onvalue=1, offvalue=0)
milkTeaCheck.grid(row=0, column=3, sticky="nsew")
milkTeaSpin = ttk.Spinbox(milkTeaFrame, width=10, from_=0, to=100)
milkTeaSpin.grid(row=0, column=2, sticky="nsew", padx=(20,5))

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