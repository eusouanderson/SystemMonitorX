import tkinter as tk
from cpu_freq import cpu
from temp_freq import temp
from graphic import graph
from PIL import Image, ImageTk


app = tk.Tk()

float_tmp = float(temp())
float_cpu = float(cpu())

app.geometry('250x1000')
#app.overrideredirect(True)
app.wm_overrideredirect(True)

def update(time=1000):
    float_tmp = float(temp())
    float_cpu = float(cpu())
    
    label_cpu.config(text=f'{cpu()} HZ ')
    label_temp.config(text=f'{temp()} Cº ')
    app.after(time, update)


label_cpu = tk.Label(app, text=f'{cpu} HZ ')
label_cpu.pack()

label_temp = tk.Label(app, text=f'{temp} Cº ')
label_temp.pack()

label_graph = tk.Label(text=graph(app, float_tmp))
label_graph.pack()


update()
app.mainloop()