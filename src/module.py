import tkinter as tk
from cpu_freq import cpu
from temp_freq import temp
from graphic import graph
from PIL import Image, ImageTk



app = tk.Tk()

app.geometry('250x1000')
app.wm_overrideredirect(True)


def update(time=1000):

    label_cpu.config(text=f'{cpu()} HZ ')
    label_temp.config(text=f'{temp()} Cº ')
   
    app.after(time, update)
    



label_cpu = tk.Label()
label_cpu.pack()

label_temp = tk.Label()
label_temp.pack()

graph(app)

update()


app.mainloop()