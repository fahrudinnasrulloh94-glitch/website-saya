import tkinter as tk
from time import strftime
import random

# Warna teks yang akan dipilih secara acak
warna_list = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'white', 'orange']

# Membuat jendela utama
root = tk.Tk()
root.title("Jam Digital Transparan")

# Mengatur jendela: tanpa border, transparan, selalu di atas
root.overrideredirect(True)  # hilangkan border window
root.wm_attributes("-topmost", True)  # selalu di atas
root.wm_attributes("-transparentcolor", "black")  # warna hitam jadi transparan

# Atur posisi awal jendela
root.geometry("+100+100")

# Label untuk menampilkan jam
label = tk.Label(root, font=('Consolas', 48, 'bold'), fg='cyan', bg='black')
label.pack()

def update_jam():
    waktu = strftime('%H:%M:%S')
    warna = random.choice(warna_list)
    label.config(text=waktu, fg=warna)
    root.after(1000, update_jam)

offset_x = 0
offset_y = 0

def click_mouse(event):
    global offset_x, offset_y
    offset_x = event.x
    offset_y = event.y

def drag_mouse(event):
    x = root.winfo_pointerx() - offset_x
    y = root.winfo_pointery() - offset_y
    root.geometry(f'+{x}+{y}')

label.bind("<Button-1>", click_mouse)
label.bind("<B1-Motion>", drag_mouse)

update_jam()

root.mainloop()
