import tkinter as tk
from tkinter import *
import tkinter.messagebox

root = tk.Tk()
root.title("Gudnezz Currency Converter")
Tops = Frame(root, bg="#e6e5e5",
             pady=6, width=1800, height=90,
             relief="ridge")
Tops.place(x=0, y=0)

Label_1 = Label(root, font=("lato black", 7, "bold"), text="", padx=2,
                 pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=7, column=0, sticky=W)


headlabel = tk.Label(Tops, font=("lato black", 19, "bold"), text="  Gudnezz Currency Converter ", bg="#e6e5e5", fg="blue")
headlabel.grid(row=1, column=5, padx=20, sticky=W)


variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("currency")
variable2.set("currency")


def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()
    from_currency = variable1.get()
    to_currency = variable2.get()

    if (Amount1_field.get() == ""):
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")
    elif (from_currency == "currency" or to_currency == "currency"):
        tkinter.messagebox.showinfo("Error !!",
                                    "Currency Not Selected.\n Please select FROM and TO Currency form menu.")
    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amount = float("{: 4f}". format(new_amt))
        Amount2_field.insert(0, str(new_amount))


def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)


CurrencyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

root.configure(background="#e6e5e5")
root.geometry("700x400")

Label_1 = Label(root, font=("lato black", 27, "bold"), text="", padx=2,
                pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=1, column=0, sticky=W)


label1 = tk.Label(root, font=("Times New Roman", 15, "bold"), text="\t Amount: ", bg="#e6e5e5",  fg="black")
label1.grid(row=2, column=0, sticky=W)

label1 = tk.Label(root, font=("Times New Roman", 15, "bold"), text="\t From Currency: ", bg="#e6e5e5", fg="black")
label1.grid(row=3, column=0, sticky=W)

label1 = tk.Label(root, font=("Times New Roman", 15, "bold"), text="\t To Currency: ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=W)

label1 = tk.Label(root, font=("Times New Roman", 15, "bold"), text="\t Converted Amount: ", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)


FromCurrency_option = tk.OptionMenu(root, variable1, *CurrencyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrencyCode_list)

FromCurrency_option.grid(row=3, column=1, ipadx=10, sticky=E)
ToCurrency_option.grid(row=4, column=1, ipadx=10, sticky=E)

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=1, ipadx=28, sticky=E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=1, ipadx=31, sticky=E)

Label_9 = Button(root, font=("arial", 15, "bold"), text=" Convert", padx=2, pady=2, bg="light blue", fg="white",
                 command=RealTimeCurrencyConversion)
Label_9.grid(row=6, column=0)


Label_9 = Button(root, font=("arial", 15, "bold"), text=" Clear All", padx=2, pady=2, bg="light blue", fg="white",
                 command=clear_all)
Label_9.grid(row=10, column=0)


root.mainloop()