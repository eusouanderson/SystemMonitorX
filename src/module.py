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
    
    label_cpu.config(text=cpu())
    label_temp.config(text=temp())
    app.after(time, update)


label_cpu = tk.Label(app, text=cpu)
label_cpu.pack()

label_temp = tk.Label(app, text=temp)
label_temp.pack()

update(100)
app.mainloop()