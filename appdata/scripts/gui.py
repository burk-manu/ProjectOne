import tkinter as tk




root = tk.Tk()
root.title("Master Math")
root.geometry("900x450")

entry = tk.Entry(root)
entry.bind("<Return>", print(5))  # <Return> steht für die Enter-Taste
entry.pack(pady=10)

root.mainloop()