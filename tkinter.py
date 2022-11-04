import tkinter as tk
from tkinter import messagebox
root = tk.Tk()


def function1():
    # print("Hello Dr. Umesh Dutta")
    messagebox.showinfo('MRIIC','Welcome Dr. Umesh Dutta')

root.geometry('400x200')

btn1 = tk.Button(root,text="Submit Button",command=function1)
btn1.pack(pady=5)

btn2 = tk.Button(root,text="Exit Button",command=root.destroy)
btn2.pack(pady=10)

root.mainloop()
