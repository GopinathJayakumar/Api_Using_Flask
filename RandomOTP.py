from tkinter import messagebox
from tkinter import *
import random

root = Tk()
root.title('OTP Generator')
root.geometry('300x200')
root.config(bg = "black")

def fetch_otp():
    messagebox.showinfo(title="OTP", message=f'your OTP is :{random.randint(1000, 999)}')


label = Label(root, text='-----Click to Generate OTP-----', font=('arial', 10, "bold"))
label.pack(fill=X,pady=5)

button =Button(root, text="Generate", font=("arial", 10, "bold"), command=fetch_otp)
button.pack()

root.mainloop()