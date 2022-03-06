from tkinter import *
from tkinter import Tk, StringVar

root = Tk()
root.title('UNIT CONVERTER')
root.geometry("700x600+100+100")
root.configure(bg='light blue')
l = Label(root, text='UNIT CONVERTER', bg='pink', font=("Arial", 30, "bold"), fg="blue", justify=CENTER)
l.place(x=170, y=40)

widget = Button(None, text="QUIT", bg="black", fg="red", font=("Arial", 14, "bold"), relief=RAISED, bd=5,
                justify=CENTER, highlightbackground="red", overrelief=GROOVE, activebackground="red",
                activeforeground="black", command=root.destroy).place(x=500, y=500)


def CurrencyConverter():
    converter = Tk()
    converter.geometry("600x400")
    converter.configure(bg='gold')

    converter.title("Currency Converter")

    OPTIONS = {
        "Argentine Peso": 1.234599, "Australian Dollar": 0.017754, "Bahraini Dinar": 0.005125,
        "Botswana Pula": 0.149950, "Brazilian Real": 0.078075, "British Pound": 0.009850, "Bruneian Dollar": 0.018391,
        "Bulgarian Lev": 0.022476, "Canadian Dollar": 0.017233, "Chilean Peso": 10.008672,
        "Chinese Yuan Renminbi": 0.088937, "Colombian Peso": 49.170048, "Croatian Kuna": 0.087087,
        "Czech Koruna": 0.303361, "Danish Krone": 0.085459, "Emirati Dirham": 0.050062, "Euro": 0.011492,
        "Hong Kong Dollar": 0.105912, "Hungarian Forint": 4.223630, "Icelandic Krona": 1.745779,
        "Indonesian Rupiah": 195.759343, "Iranian Rial": 573.067264, "Israeli Shekel": 0.045497,
        "Japanese Yen": 1.483707, "Kazakhstani Tenge": 5.727210, "Kuwaiti Dinar": 0.004131, "Libyan Dinar": 0.060513,
        "Malaysian Ringgit": 0.055966, "Mauritian Rupee": 0.548480, "Mexican Peso": 0.291094,
        "Nepalese Rupee": 1.607500, "New Zealand Dollar": 0.019061, "Norwegian Krone": 0.116024,
        "Omani Rial": 0.005241, "Pakistani Rupee": 2.142744, "Philippine Peso": 0.663882, "Polish Zloty": 0.052782,
        "Qatari Riyal": 0.049619, "Romanian New Leu": 0.056160, "Russian Ruble": 1.014714,
        "Saudi Arabian Riyal": 0.051118, "Singapore Dollar": 0.018391, "South African Rand": 0.211037,
        "South Korean Won": 15.549720, "Sri Lankan Rupee": 2.676137, "Swedish Krona": 0.116788,
        "Swiss Franc": 0.012746, "Taiwan New Dollar": 0.384896, "Thai Baht": 0.419998, "Trinidadian Dollar": 0.092502,
        "Turkish Lira": 0.105402, "US Dollar": 0.013632, "Venezuelan Bolivar": 0.136145}

    def ok():
        try:
            price = rupees.get()
            answer = variable.get()
            DICT = OPTIONS.get(answer, None)
            if DICT is None:
                result.delete(1.0, END)
                result.insert(INSERT, "ERROR")
                return
            converted = float(DICT) * float(price)
            result.delete(1.0, END)
            result.insert(INSERT, "Price In ", INSERT, answer, INSERT, " = ", INSERT, converted)
        except:
            result.delete(1.0, END)
            result.insert(INSERT, "ERROR")

    appName = Label(converter, text="Currency", font=("arial", 25, "bold", "underline"), bg="orange", fg="dark red")
    appName.grid(row=0, column=0)
    appName = Label(converter, text="Converter", font=("arial", 25, "bold", "underline"), bg="orange", fg="dark red")
    appName.grid(row=0, column=2)

    india = Label(converter, text="Indian Rupees (Rs.):", font=("arial", 10, "bold"), fg="red")
    india.grid(row=1, column=0)
    rupees = Entry(converter, font=("calibri", 20))
    rupees.grid(row=1, column=1)
    choice = Label(converter, text="Choose Country:", font=("arial", 10, "bold"), fg="red")
    choice.grid(row=2, column=0)
    result = Text(converter, height=5, width=50, font=("arial", 10, "bold"), bd=5)
    result.grid(row=3, columnspan=10, padx=3)
    variable = StringVar(converter)
    variable.set(None)
    option = OptionMenu(converter, variable, *OPTIONS)
    option.grid(row=2, column=1, sticky="ew")
    button = Button(converter, text="Convert", fg="green", font=("calibri", 20), bg="powder blue", command=ok)
    button.grid(row=2, column=2)

    mainloop()


def WeightConverter():
    rootW = Tk()
    rootW.geometry("650x400")
    rootW['bg'] = 'grey'
    rootW.title("Weight Converter")
    unit_dict = {"Gram": 1.0, "Kilogram": 1000.0, "Quintal": 100000.0, "Tonne": 1000000.0, "Pounds": 453.592,
                 "Ounce": 28.34949, }
    weights = ["Kilogram", "Gram", "Quintal", "Tonne", "Pounds", "Ounce", ]

    def ok():
        try:
            inp = float(inputentry.get())
            inp_unit = inputopt.get()
            out_unit = outputopt.get()

            cons = [inp_unit in weights and out_unit in weights]

            if any(cons):  # If both the units are of same type, do the conversion
                outputentry.delete(0, END)
                outputentry.insert(0, round(inp * unit_dict[inp_unit] / unit_dict[out_unit], 5))
        except:
            outputentry.delete(0, END)
            outputentry.insert(0, "ERROR")

    appName = Label(rootW, text="Weight", font=("arial", 25, "bold", "underline"), bg="silver", fg="dark red")
    appName.grid(row=0, column=0)
    appName = Label(rootW, text="Converter", font=("arial", 25, "bold", "underline"), bg="silver", fg="dark red")
    appName.grid(row=0, column=3)

    inputlabel = Label(rootW, text="Enter the Weight:", font=("arial", 10, "bold"), fg="red")
    inputlabel.grid(row=2, column=0)
    inputentry = Entry(rootW, font=("calibri", 20))
    inputentry.grid(row=2, column=1)
    choice = Label(rootW, text="Choose Unit:", font=("arial", 10, "bold"), fg="red")
    choice.grid(row=2, column=2)
    inputopt = StringVar(rootW)
    inputopt.set('Select Unit')
    inputmenu = OptionMenu(rootW, inputopt, *weights)
    inputmenu.grid(row=2, column=3, sticky="ew")
    outputlabel = Label(rootW, text="Result:", font=("arial", 10, "bold"), fg="red")
    outputlabel.grid(row=3, column=0)
    outputentry = Entry(rootW, font=("calibri", 20))
    outputentry.grid(row=3, column=1)
    choice = Label(rootW, text="Choose Unit:", font=("arial", 10, "bold"), fg="red")
    choice.grid(row=3, column=2)
    outputopt = StringVar(rootW)
    outputopt.set('Select Unit')
    outputmenu = OptionMenu(rootW, outputopt, *weights)
    outputmenu.grid(row=3, column=3, sticky="ew")
    convertbtn = Button(rootW, text="CONVERT", command=ok, padx=80, pady=2)
    convertbtn.grid(row=4, column=1, columnspan=2, pady=50)

    rootW.mainloop()


def TemperatureConverter():
    rootT = Tk()
    rootT.geometry("750x400")
    rootT['bg'] = 'orange'
    rootT.title("Temperature Converter")
    temps = ["Celsius", "Fahrenheit", "Kelvin", ]

    def ok():
        try:
            inp = float(inputentry.get())
            inp_unit = inputopt.get()
            out_unit = outputopt.get()

            cons = [inp_unit in temps and out_unit in temps]

            if any(cons):  # If both the units are of same type, do the conversion
                if inp_unit == "Celsius" and out_unit == "Fahrenheit":
                    outputentry.delete(0, END)
                    outputentry.insert(0, (inp * 1.8) + 32)
                elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
                    outputentry.delete(0, END)
                    outputentry.insert(0, (inp - 32) * (5 / 9))
                elif inp_unit == "Celsius" and out_unit == "Kelvin":
                    outputentry.delete(0, END)
                    outputentry.insert(0, inp + 273.15)
                elif inp_unit == "Fahrenheit" and out_unit == "Kelvin":
                    outputentry.delete(0, END)
                    outputentry.insert(0, (inp - 32) * (5 / 9) + 273.15)
                elif inp_unit == "Kelvin" and out_unit == "Celsius":
                    outputentry.delete(0, END)
                    outputentry.insert(0, inp - 273.15)
                elif inp_unit == "Kelvin" and out_unit == "Fahrenheit":
                    outputentry.delete(0, END)
                    outputentry.insert(0, (inp - 273.15) * (9 / 5) + 32)
                else:
                    outputentry.delete(0, END)
                    outputentry.insert(0, inp)
        except:
            outputentry.delete(0, END)
            outputentry.insert(0, "ERROR")

    appName = Label(rootT, text="Temperature", font=("arial", 25, "bold", "underline"), bg="yellow", fg="dark red")
    appName.grid(row=0, column=0)
    appName = Label(rootT, text="Converter", font=("arial", 25, "bold", "underline"), bg="yellow", fg="dark red")
    appName.grid(row=0, column=3)

    inputlabel = Label(rootT, text="Enter the Temperature:", font=("arial", 10, "bold"), fg="red")
    inputlabel.grid(row=2, column=0)
    inputentry = Entry(rootT, font=("calibri", 20))
    inputentry.grid(row=2, column=1)
    choice = Label(rootT, text="Choose Unit:", font=("arial", 10, "bold"), fg="red")
    choice.grid(row=2, column=2)
    inputopt = StringVar(rootT)
    inputopt.set('Select Unit')
    inputmenu = OptionMenu(rootT, inputopt, *temps)
    inputmenu.grid(row=2, column=3, sticky="ew")
    outputlabel = Label(rootT, text="Result:", font=("arial", 10, "bold"), fg="red")
    outputlabel.grid(row=3, column=0)
    outputentry = Entry(rootT, font=("calibri", 20))
    outputentry.grid(row=3, column=1)
    choice = Label(rootT, text="Choose Unit:", font=("arial", 10, "bold"), fg="red")
    choice.grid(row=3, column=2)
    outputopt = StringVar(rootT)
    outputopt.set('Select Unit')
    outputmenu = OptionMenu(rootT, outputopt, *temps)
    outputmenu.grid(row=3, column=3, sticky="ew")
    convertbtn = Button(rootT, text="CONVERT", command=ok, padx=80, pady=2)
    convertbtn.grid(row=4, column=1, columnspan=2, pady=50)

    rootT.mainloop()


def LengthConverter():
    rootL = Tk()
    rootL.geometry("650x400")
    rootL['bg'] = 'silver'
    rootL.title("Length Converter")
    unit_dict = {"Meter": 1.0, "Kilometer": 1000, "Nautical Mile": 1852.0003, "Feet": 0.3048, "Mile": 1609.344,
                 "Inch": 0.0254, "Yard": 0.9144}
    lengths = ["Meter", "Kilometer", "Nautical Mile", "Feet", "Mile", "Inch", "Yard"]

    def ok():
        try:
            inp = float(inputentry.get())
            inp_unit = inputopt.get()
            out_unit = outputopt.get()

            cons = [inp_unit in lengths and out_unit in lengths]

            if any(cons):  # If both the units are of same type, do the conversion
                outputentry.delete(0, END)
                outputentry.insert(0, round(inp * unit_dict[inp_unit] / unit_dict[out_unit], 5))
        except:
            outputentry.delete(0, END)
            outputentry.insert(0, "ERROR")

    appName = Label(rootL, text="Length", font=("arial", 25, "bold", "underline"), bg="grey", fg="dark red")
    appName.grid(row=0, column=0)
    appName = Label(rootL, text="Converter", font=("arial", 25, "bold", "underline"), bg="grey", fg="dark red")
    appName.grid(row=0, column=3)

    inputlabel = Label(rootL, text="Enter the Length:", font=("arial", 10, "bold"), fg="red")
    inputlabel.grid(row=2, column=0)
    inputentry = Entry(rootL, font=("calibri", 20))
    inputentry.grid(row=2, column=1)
    choice = Label(rootL, text="Choose Unit:", font=("arial", 10, "bold"), fg="red")
    choice.grid(row=2, column=2)
    inputopt = StringVar(rootL)
    inputopt.set('Select Unit')
    inputmenu = OptionMenu(rootL, inputopt, *lengths)
    inputmenu.grid(row=2, column=3, sticky="ew")
    outputlabel = Label(rootL, text="Result:", font=("arial", 10, "bold"), fg="red")
    outputlabel.grid(row=3, column=0)
    outputentry = Entry(rootL, font=("calibri", 20))
    outputentry.grid(row=3, column=1)
    choice = Label(rootL, text="Choose Unit:", font=("arial", 10, "bold"), fg="red")
    choice.grid(row=3, column=2)
    outputopt = StringVar(rootL)
    outputopt.set('Select Unit')
    outputmenu = OptionMenu(rootL, outputopt, *lengths)
    outputmenu.grid(row=3, column=3, sticky="ew")
    convertbtn = Button(rootL, text="CONVERT", command=ok, padx=80, pady=2)
    convertbtn.grid(row=4, column=1, columnspan=2, pady=50)

    rootL.mainloop()


widget1 = Button(root, text="Currency converter", bg="gold", fg="green", font=("Arial", 14, "bold", "italic"),
                 relief=RAISED, bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE,
                 activebackground="green", activeforeground="blue", command=CurrencyConverter).place(x=100, y=200)
widget2 = Button(root, text="Weight Converter", bg="grey", fg="black", font=("Arial", 14, "bold", "italic"),
                 relief=RAISED, bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE,
                 activebackground="green", activeforeground="blue", command=WeightConverter).place(x=100, y=260)
widget3 = Button(root, text="Temperature Converter", bg="orange", fg="red", font=("Arial", 14, "bold", "italic"),
                 relief=RAISED, bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE,
                 activebackground="green", activeforeground="blue", command=TemperatureConverter).place(x=100, y=320)
widget4 = Button(root, text="Length converter", bg="silver", fg="brown", font=("Arial", 14, "bold", "italic"),
                 relief=RAISED, bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE,
                 activebackground="green", activeforeground="blue", command=LengthConverter).place(x=100, y=380)
root.mainloop()
