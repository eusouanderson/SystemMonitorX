import tkinter as tk
from tkinter import ttk
from graphic1 import graph
from graphic2 import graph2
from cpu import cpu_freq, cpu_count
from temp_freq import temp_core

app = tk.Tk()

app.configure(bg='#404040')
app.geometry('300x1000')
app.wm_overrideredirect(True)
msto= 100


def update_proc(time=msto):
    label_cpu_usage.config(text=f'{cpu_count()} Cpus')
    label_cpu_usage.configure(bg='#404040', fg='#bfbfbf')
    label_cpu.config(text=f'{cpu_freq()} HZ CPU')
    label_cpu.configure(bg='#404040', fg='#bfbfbf')
    label_temp.config(text=f'{temp_core()} Cº CPU')
    label_temp.configure(bg='#404040', fg='#bfbfbf')
    app.after(time, update_proc)


label_cpu_usage = tk.Label()
label_cpu_usage.pack()

label_cpu = tk.Label()
label_cpu.pack()

label_temp = tk.Label()

label_temp.pack()

def button():
    graph(app)
    graph2(app)

Button_graph = ttk.Button(text='Graphic', command=button)
Button_graph.pack()



Button_exit = ttk.Button(text='Exit', command=app.destroy)
Button_exit.pack()
update_proc()



print(ttk.Style().lookup("TButton", "font"))

if __name__ == '__main__':
    app.mainloop()
    