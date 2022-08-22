# The number of characters shown on the result window is limited to 29
from tkinter import *
from math import sqrt

lst_1 = []
equal_cond = True
sqrt_cond = True
pwr_cond = True

class Labels:
    def blank(self):
        Label(root, padx=282, font=("Lato", 25)).grid(row=0, column=0, columnspan=4)

    def text(self, text):
        Label(root, text=text, font=("Lato", 25)).grid(row=0, column=0, columnspan=4)

class Nums_Symbls:
    def __init__(self, x):
        self.x = x

    def numFunc(self):
        global lst_1, equal_cond
        if len(lst_1) < 29:
            # If 'equal' wasn't clicked before
            if equal_cond == True:
                Labels().blank()
                lst_1.append(self.x)
                Labels().text("".join(lst_1))
            # If 'equal' was clicked before
            else:
                if len(lst_1) > 0 and lst_1[-1] in ("+", "-", "*", "/"):
                    pass
                else:
                    lst_1 = []
                Labels().blank()
                lst_1.append(self.x)
                Labels().text("".join(lst_1))
                equal_cond = True
        else:
            pass

    def symblFunc(self):
        if len(lst_1) < 28:
            if len(lst_1) > 1 and lst_1[-1] in ("+", "-") and self.x in ("+", "-", "*", "/"):
                lst_1.pop()
            if len(lst_1) > 1 and lst_1[-1] in ("*", "/") and self.x in ("+", "-"):
                pass
            elif len(lst_1) > 1 and lst_1[-1] in ("*", "/") and self.x in ("*", "/"):
                lst_1.pop()
            lst_1.append(self.x)
            Labels().blank()
        else:
            pass

def sqr():
    global sqrt_cond, lst_1
    Labels().blank()
    try:
        # If 'equal' wasn't clicked before
        if sqrt_cond == True:
            # If input is a single negative number
            if lst_1.count("-") == 1 and lst_1[0] == "-" and lst_1.count("+") == 0 and lst_1.count("*") == 0 and lst_1.count("/") == 0:
                Labels().text("Error")
                lst_1 = []
            # If input isn't a single negative number
            else:
                lst_2 = []
                for i in reversed(lst_1):
                    if i not in ("+", "-", "*", "/"):
                        lst_2.append(i)
                        lst_1.pop()
                    else:
                        break
                try:
                    result = str(round(sqrt(float("".join(reversed(lst_2)))), 3))
                    for j in result:
                        lst_1.append(j)
                    Labels().text(eval("".join(lst_1)))
                except ValueError:
                    Labels().text("Error")
        # If 'equal' was clicked before
        else:
            try:
                result = str(round(sqrt(eval("".join(lst_1))), 3))
                lst_1 = []
                for k in result:
                    lst_1.append(k)
                Labels().text(result)
                sqrt_cond = True
            except ValueError:
                Labels().text("Error")
    except SyntaxError:
        Labels().text("Error")

def pwr():
    global pwr_cond, lst_1
    Labels().blank()
    try:
        # If 'equal' wasn't clicked before
        if pwr_cond == True:
            # If input is a single negative number
            if lst_1.count("-") == 1 and lst_1[0] == "-" and lst_1.count("+") == 0 and lst_1.count("*") == 0 and lst_1.count("/") == 0:
                result = str(round(float("".join(lst_1))**2, 3))
                lst_1 = []
                for k in result:
                    lst_1.append(k)
                Labels().text(result)
            # If input isn't a single negative number
            else:
                lst_2 = []
                for i in reversed(lst_1):
                    if i not in ("+", "-", "*", "/"):
                        lst_2.append(i)
                        lst_1.pop()
                    else:
                        break
                # Checking if a number the func is used on has a plus or minus at the beginning
                if len(lst_1) > 2 and (lst_1[-1] in ("+", "-") and lst_1[-2] in ("*", "/")):
                    lst_1.pop()
                else:
                    pass
                try:
                    result = str(round(float(("".join(reversed(lst_2))))**2, 3))
                    for j in result:
                        lst_1.append(j)
                    Labels().text(eval("".join(lst_1)))
                except OverflowError:
                    Labels().text("Too large result")
                except ValueError:
                    Labels().text("Error")
        # If 'equal' was clicked before
        else:
            try:
                result = str(round(eval("".join(lst_1))**2, 3))
                lst_1 = []
                for l in result:
                    lst_1.append(l)
                if len(lst_1) < 29:
                    Labels().text(result)
                else:
                    Labels().text("Too large result")
                pwr_cond = True
            except ValueError:
                Labels().text("Error")
    except SyntaxError:
        Labels().text("Too large result")

def equal():
    global equal_cond, sqrt_cond, pwr_cond
    Labels().blank()
    try:
        Labels().text(eval("".join(lst_1)))
        equal_cond = False
        sqrt_cond = False
        pwr_cond = False
    except SyntaxError:
        Labels().text("Error")

def clean():
    global lst_1, equal_cond, sqrt_cond, pwr_cond
    Labels().blank()
    lst_1 = []
    equal_cond = True
    sqrt_cond = True
    pwr_cond = True

root = Tk()
root.geometry("586x197")
root.resizable(False, False)
root.title("Calculator")
root.iconbitmap("C:/Users/Admin/PycharmProjects/tkinter/calc_icon.ico")

class Buttons:
    def __init__(self, text, cmd, r, c):
        self.text = text
        self.cmd = cmd
        self.r = r
        self.c = c
    def buttonCreate(self):
        Button(root, text=self.text, padx=61.5, borderwidth=0, font="Lato", command=self.cmd).grid(row=self.r, column=self.c)

Label(root, text="", font=("Lato", 25)).grid(row=0, column=0, columnspan=4)

# 1st row of buttons
Buttons("C", clean, 1, 0).buttonCreate()
Buttons("x²", pwr, 1, 1).buttonCreate()
Buttons("√x", sqr, 1, 2).buttonCreate()
Buttons("÷", Nums_Symbls("/").symblFunc, 1, 3).buttonCreate()

# 2nd row of buttons
Buttons("7", Nums_Symbls("7").numFunc, 2, 0).buttonCreate()
Buttons("8", Nums_Symbls("8").numFunc, 2, 1).buttonCreate()
Buttons("9", Nums_Symbls("9").numFunc, 2, 2).buttonCreate()
Buttons("×", Nums_Symbls("*").symblFunc, 2, 3).buttonCreate()

# 3rd row of buttons
Buttons("4", Nums_Symbls("4").numFunc, 3, 0).buttonCreate()
Buttons("5", Nums_Symbls("5").numFunc, 3, 1).buttonCreate()
Buttons("6", Nums_Symbls("6").numFunc, 3, 2).buttonCreate()
Buttons("-", Nums_Symbls("-").symblFunc, 3, 3).buttonCreate()

# 4th row of buttons
Buttons("1", Nums_Symbls("1").numFunc, 4, 0).buttonCreate()
Buttons("2", Nums_Symbls("2").numFunc, 4, 1).buttonCreate()
Buttons("3", Nums_Symbls("3").numFunc, 4, 2).buttonCreate()
Buttons("+", Nums_Symbls("+").symblFunc, 4, 3).buttonCreate()

# 5th row of buttons
Buttons(".", Nums_Symbls(".").numFunc, 5, 0).buttonCreate()
Buttons("0", Nums_Symbls("0").numFunc, 5, 1).buttonCreate()
Button(root, text="=", padx=61.5, borderwidth=0, font="Lato", command=equal).grid(row=5, column=2, columnspan=2)

if __name__ == "__main__":
    root.mainloop()
