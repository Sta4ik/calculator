from tkinter import *
from tkinter.ttk import *

def main():
    root = Tk()
    root.title("Calculator")
    root.resizable(False, False)

    screenWidth = root.winfo_screenwidth()
    windowWidth = int(screenWidth * 0.2)
    windowHeight = int(windowWidth * 8 / 9)
    root.geometry(f"{windowWidth}x{windowHeight}")

    entry = Entry(root)
    entry.pack(padx=5, pady=5, fill=X)

    buttons = [
        ["sin", "cos", "tan", "sqrt"],
        ["7", "8", "9", "+", "C"],
        ["4", "5", "6", "-", "pi"],
        ["1", "2", "3", "/", "pow"],
        [".", "0", "(", ")", "="]
    ]

    buttonFrame = Frame(root)
    buttonFrame.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
