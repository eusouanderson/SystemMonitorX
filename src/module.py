import tkinter as tk
from graphic import graph
from cpu_freq import cpu
from temp_freq import temp

app = tk.Tk()

app.geometry('250x1000')
app.wm_overrideredirect(True)

def update(time=1000):

    label_cpu.config(text=f'{cpu()} HZ CPU')
    label_temp.config(text=f'{temp()} Cº CPU')
   
    app.after(time, update)

label_cpu = tk.Label()
label_cpu.pack()

label_temp = tk.Label()
label_temp.pack()

update()
graph(app)

app.mainloop()