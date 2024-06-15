import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.resizable(0, 0)
        
        self.expression = ""
        
        self.display = tk.Entry(self, font=("Arial", 24), borderwidth=2, relief="ridge")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            if button != '=':
                tk.Button(self, text=button, width=5, height=2, command=action).grid(row=row_val, column=col_val, padx=5, pady=5)
            else:
                tk.Button(self, text=button, width=5, height=2, command=action, bg="lightblue").grid(row=row_val, column=col_val, padx=5, pady=5, rowspan=2, sticky="nsew")

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        tk.Button(self, text="C", width=5, height=2, command=self.clear_display, bg="lightcoral").grid(row=5, column=0, padx=5, pady=5, columnspan=4, sticky="nsew")
    
    def click_event(self, key):
        if key == '=':
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += str(key)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)
    
    def clear_display(self):
        self.expression = ""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
