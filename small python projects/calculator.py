import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.entry = tk.Entry(master, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(master, text=text, padx=20, pady=10, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        self.current = ""

    def button_click(self, value):
        if value == "=":
            try:
                result = eval(self.current)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.current = str(result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.current = ""
        else:
            self.current += value
            self.entry.insert(tk.END, value)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
