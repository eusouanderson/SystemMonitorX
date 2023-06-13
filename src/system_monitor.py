import tkinter as tk
from graphic1 import graph
from graphic2 import monitor_cpu
from cpu import cpu_freq, cpu_usage
from temp_freq import temp_core

app = tk.Tk()

app.geometry('300x1000')
app.wm_overrideredirect(False)
msto= 100

def update_proc(time=msto):
    #label_cpu_usage.config(text=f'{cpu_usage()} Usage')
    label_cpu.config(text=f'{cpu_freq()} HZ CPU')
    app.after(time, update_proc)


label_cpu_usage = tk.Label()
label_cpu_usage.pack()

label_cpu = tk.Label()
label_cpu.pack()

label_temp = tk.Label()
label_temp.config(text=f'{temp_core()} Cº CPU')
label_temp.pack()

update_proc()
graph(app)
monitor_cpu(app)

Button_exit = tk.Button(text='Exit', command=app.destroy)
Button_exit.pack()

if __name__ == '__main__':
    app.mainloop()
