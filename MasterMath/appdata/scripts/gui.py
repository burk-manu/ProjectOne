import tkinter as tk
import Main



root = tk.Tk()
root.title("Master Math")
root.geometry("900x450")

entry = tk.Entry(root)
entry.bind("<Return>", Main.calculate)  # <Return> steht für die Enter-Taste
entry.pack(pady=10)

root.mainloop()