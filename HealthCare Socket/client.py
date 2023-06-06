import customtkinter as ctk
from PIL import Image
import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
msg = s.recv(1024)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("800x500")

def login():
    
    username = entry1.get()
    password = entry2.get()
    for widgets in frame.winfo_children():
      widgets.destroy()
    data = str([1,username,password])
    data = data.encode()
    s.send(data)
    ans = s.recv(1024)
    new_text = ctk.CTkLabel(master = frame, text= ans.decode())
    new_text.pack(pady=12, padx=10)
    if(ans.decode() == '1'):
      new_text = ctk.CTkLabel(master = frame, text= "logged in")
      new_text.pack(pady=12, padx=10)
    else:
      new_text = ctk.CTkLabel(master = frame, text= "wrong id/pass")
      new_text.pack(pady=12, padx=10)

frame = ctk.CTkFrame(master = root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
image1 = ctk.CTkImage(dark_image=Image.open(os.path.join("image1.png")), size=(150,150))
heading1 = ctk.CTkLabel(master = frame, image=image1, text='')
heading1.pack(pady=12, padx=10)
entry1 = ctk.CTkEntry(master = frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = ctk.CTkEntry(master = frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)
    
button = ctk.CTkButton(master = frame, text = "Login", command=login)
button.pack(pady=12, padx=10)

signup1 = ctk.CTkLabel(master = frame, text='New to the platform?')
signup2 = ctk.CTkLabel(master = frame, text='Sign up', cursor="hand2" , text_color="blue")
signup2.bind("<Button-1>", lambda e: login)
signup1.pack(pady=4, padx=10)
signup2.pack(pady=2, padx=10)
root.mainloop()