import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock with Date")
root.geometry("300x100")
root.configure(bg="black")

def update_time_date():
    current_time = strftime('%I:%M:%S %p')  
    current_date = strftime('%A, %d %B %Y')  
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time_date)  


time_label = tk.Label(root, font=('calibri', 30, 'bold'), background='black', foreground='white')
time_label.pack(pady=10)


date_label = tk.Label(root, font=('calibri', 10, 'bold'), background='black', foreground='yellow')
date_label.pack(pady=5)


update_time_date()


root.mainloop()
