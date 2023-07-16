import tkinter as tk
import webbrowser as wb

root = tk.Tk()
def display_snapchat():
    user_enq = enq.get()
    print(user_enq)
    if user_enq: 
        l2.config(text="python course")
        wb.open("https://www.snapchat.com/results?q")
    else:
        l2.config(text=" Enter Query")


def display_instagram():
        user_enq = enq.get()
        print(user_enq)
        if user_enq: 
            l2.config(text="python course")
            wb.open("https://instagram.com/only.python?q")
        else:
            l2.config(text="python course")

def display_youtube():
    user_enq = enq.get()
    print(user_enq)
    if user_enq:
        l2.config(text="python course")
        wb.open("https://www.youtube.com/results?search_query")
    else:
        l2.config(text="Python course")



enq = tk.Entry(root, 
               font=("Times New Roman", 20),
               width=30)
enq.grid(row=0,column=1)

l1 = tk.Label(root, 
              text="Enter information:", 
              font=("Times New Roman", 25))
l1.grid(row=0,column=0)

l2 = tk.Label(root, 
              font=("Times New Roman", 25))
l2.grid()

youtube = tk.Button(root, 
               text="YouTube", 
               font=("Times New Roman", 20),
               width=10,
               bg="red", 
               activebackground="sky blue", 
               command=display_youtube)
youtube.grid()

instagram = tk.Button(root, 
               text="Instagram", 
               font=("Times New Roman", 20),
               width=10,
               bg="pink", 
               activebackground="navy blue", 
               command=display_instagram)
instagram.grid()

snapchat = tk.Button(root, 
               text="Snapchat", 
               font=("Times New Roman", 20),
               width=10,
               bg="yellow", 
               activebackground="dark blue", 
               command=display_snapchat)
snapchat.grid()


root.mainloop()
