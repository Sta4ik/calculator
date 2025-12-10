from tkinter import *
from tkinter.ttk import *
import math

def inputToEntry(entry, inputElement):
    entry.insert(END, inputElement)

def deleteInEntry(entry):
    entry.delete(len(entry.get()) - 1, '')

def calculate(entry):
    expression = entry.get()
    print(expression)

def main():
    root = Tk()
    root.title("Calculator")
    root.resizable(False, False)
    root.geometry("260x420")

    entry = Entry(root)
    entry.place(x=15, y=20, width=230, height=30)

    buttonPow = Button(root, text="^", command=lambda: inputToEntry(entry, "^"))
    buttonPow.place(x=20, y=70, width=40, height=40)

    buttonSqrt = Button(root, text="sqrt", command=lambda: inputToEntry(entry, "sqrt("))
    buttonSqrt.place(x=80, y=70, width=40, height=40)

    buttonFact = Button(root, text="!", command=lambda: inputToEntry(entry, "!"))
    buttonFact.place(x=140, y=70, width=40, height=40)

    buttonOpen = Button(root, text="(", command=lambda: inputToEntry(entry, "("))
    buttonOpen.place(x=200, y=70, width=40, height=40)

    buttonSin = Button(root, text="sin", command=lambda: inputToEntry(entry, "sin("))
    buttonSin.place(x=20, y=120, width=40, height=40)

    buttonCos = Button(root, text="cos", command=lambda: inputToEntry(entry, "cos("))
    buttonCos.place(x=80, y=120, width=40, height=40)

    buttonTan = Button(root, text="tan", command=lambda: inputToEntry(entry, "tan("))
    buttonTan.place(x=140, y=120, width=40, height=40)

    buttonClose = Button(root, text=")", command=lambda: inputToEntry(entry, ")"))
    buttonClose.place(x=200, y=120, width=40, height=40)

    buttonSeven = Button(root, text="7", command=lambda: inputToEntry(entry, 7))
    buttonSeven.place(x=20, y=170, width=40, height=40)

    buttonEight = Button(root, text="8", command=lambda: inputToEntry(entry, 8))
    buttonEight.place(x=80, y=170, width=40, height=40)

    buttonNine = Button(root, text="9", command=lambda: inputToEntry(entry, 9))
    buttonNine.place(x=140, y=170, width=40, height=40)

    buttonDivide = Button(root, text="/", command=lambda: inputToEntry(entry, "/"))
    buttonDivide.place(x=200, y=170, width=40, height=40)

    buttonFour = Button(root, text="4", command=lambda: inputToEntry(entry, 4))
    buttonFour.place(x=20, y=220, width=40, height=40)

    buttonFive = Button(root, text="5", command=lambda: inputToEntry(entry, 5))
    buttonFive.place(x=80, y=220, width=40, height=40)

    buttonSix = Button(root, text="6", command=lambda: inputToEntry(entry, 6))
    buttonSix.place(x=140, y=220, width=40, height=40)

    buttonMultiply = Button(root, text="*", command=lambda: inputToEntry(entry, "*"))
    buttonMultiply.place(x=200, y=220, width=40, height=40)

    buttonOne = Button(root, text="1", command=lambda: inputToEntry(entry, 1))
    buttonOne.place(x=20, y=270, width=40, height=40)

    buttonTwo = Button(root, text="2", command=lambda: inputToEntry(entry, 2))
    buttonTwo.place(x=80, y=270, width=40, height=40)

    buttonThree = Button(root, text="3", command=lambda: inputToEntry(entry, 3))
    buttonThree.place(x=140, y=270, width=40, height=40)

    buttonMinus = Button(root, text="-", command=lambda: inputToEntry(entry, "-"))
    buttonMinus.place(x=200, y=270, width=40, height=40)

    buttonZero = Button(root, text="0", command=lambda: inputToEntry(entry, 0))
    buttonZero.place(x=20, y=320, width=40, height=40)

    buttonDot = Button(root, text=".", command=lambda: inputToEntry(entry, "."))
    buttonDot.place(x=80, y=320, width=40, height=40)

    buttonPi = Button(root, text="pi", command=lambda: inputToEntry(entry, math.pi))
    buttonPi.place(x=140, y=320, width=40, height=40)

    buttonPlus = Button(root, text="+", command=lambda: inputToEntry(entry, "+"))
    buttonPlus.place(x=200, y=320, width=40, height=40)

    buttonEqual = Button(root, text="=", command=lambda: calculate(entry))
    buttonEqual.place(x=200, y=370, width=40, height=40)

    buttonClear = Button(root, text="C", command=lambda: deleteInEntry(entry))
    buttonClear.place(x=20, y=370, width=160, height=40)

    root.mainloop()

if __name__ == "__main__":
    main()