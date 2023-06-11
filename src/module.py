import tkinter as tk
from cpu_freq import cpu
from temp_freq import temp
from PIL import Image, ImageTk

app = tk.Tk()
#while True:

app.geometry('150x50')
#app.overrideredirect(True)
app.wm_overrideredirect(True)

def update(time=1000):
    
    label_cpu.config(text=f'{cpu()} HZ ')
    label_temp.config(text=f'{temp()} Cº ')
    app.after(time, update)


label_cpu = tk.Label(app, text=f'{cpu} HZ ')
label_cpu.pack()

label_temp = tk.Label(app, text=f'{temp} Cº ')
label_temp.pack()

update(100)
app.mainloop()