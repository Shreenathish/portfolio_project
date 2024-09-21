import tkinter as tk
from tkinter import messagebox
import time
import random
from essential_generators import DocumentGenerator

gen = DocumentGenerator()
words = gen.sentence()

def show_message():
    end_time = time.time()  
    accuracy = []

    lenght_of_text = typed_text.get("1.0", 'end-1c')

    for i in range(min(len(sample_text), len(lenght_of_text))):
        if sample_text[i] == lenght_of_text[i]:
            accuracy.append(sample_text[i])
        else:
            continue

    time_taken = end_time - start_time
    time_taken_minutes = time_taken / 60

    if time_taken_minutes == 0:
        wpm = 0
    else:
        words_typed = len(lenght_of_text.split())
        wpm = words_typed / time_taken_minutes

    accuracy_time = (len(accuracy) / len(sample_text)) * 100

    messagebox.showinfo("Type Testing Details", f"You typed at a speed of {wpm:.2f} words per minute.\nYour Accuracy is {accuracy_time:.2f}.")

if __name__ == "__main__":
    sample_text = words[:55]

    root = tk.Tk()
    root.title("Typing Speed")
    root.configure(bg="yellow")
    root.geometry("500x350")

    label = tk.Label(root, text="Type Testing",bg="grey")
    label.pack()

    text = tk.Label(root, text=words)
    text.pack()

    start_time = time.time()
    typed_text = tk.Text(root, height=3, width=40)
    typed_text.pack()

    tk.Button(root, text="Show Information", command=show_message,bg="grey").pack(side=tk.BOTTOM)
    root.mainloop()
