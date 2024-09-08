import tkinter as tk
from tkinter import font

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("350x450")
        self.root.resizable(False, False)
        root.configure(bg="#D90166")


        self.display_var = tk.StringVar()
        self.create_display()

        self.create_buttons()

    def create_display(self):
        display = tk.Entry(self.root, textvariable=self.display_var, font=("Arial", 20), 
                           borderwidth=2, relief="ridge", justify="right", bg="#99c9dd")
        display.pack(pady=20, padx=10, fill="both")

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

    
        buttons = [
            ('7', 1, 0, 1), ('8', 1, 1, 1), ('9', 1, 2, 1), ('/', 1, 3, 1),
            ('4', 2, 0, 1), ('5', 2, 1, 1), ('6', 2, 2, 1), ('*', 2, 3, 1),
            ('1', 3, 0, 1), ('2', 3, 1, 1), ('3', 3, 2, 1), ('-', 3, 3, 1),
            ('0', 4, 0, 1), ('.', 4, 1, 1), ('C', 4, 2, 1), ('+', 4, 3, 1),
            ('=', 5, 0, 4)  
        ]

        for (text, row, col, colspan) in buttons:
            button = tk.Button(button_frame, text=text, width=5, height=2, font=("Arial", 14), 
                               relief="flat", bg="#99c9dd", fg="#333",
                               activebackground="#99c9dd", activeforeground="#000")
            button.grid(row=row, column=col, padx=5, pady=5, columnspan=colspan)
            button.bind("<Button-1>", self.on_button_click)

    def on_button_click(self, event):
        button_text = event.widget.cget("text")
        if button_text == "=":
            self.calculate_expression()
        elif button_text == "C":
            self.clear_expression()
        else:
            self.append_to_expression(button_text)

    def append_to_expression(self, text):
        current_text = self.display_var.get()
        if text == '.' and (not current_text or current_text[-1] in "*/+-"):
            text = '0.'
        self.display_var.set(current_text + text)

    def clear_expression(self):
        self.display_var.set("")

    def calculate_expression(self):
        try:
            result = eval(self.display_var.get())
            self.display_var.set(result)
        except Exception:
            self.display_var.set("Error")


if __name__ == "__main__":
    root = tk.Tk()
    app = ModernCalculator(root)
    root.mainloop()
