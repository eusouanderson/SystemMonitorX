import tkinter as tk
from tkinter import ttk
from graphic1 import graph
from graphic2 import graph2
from cpu import cpu_freq, cpu_count
from temp_freq import temp_core
from os import getcwd

print(getcwd())
app = tk.Tk()


app.configure(bg='#404040')
# app.geometry('300x1000')
app.wm_overrideredirect(True)
msto = 1000


def update_proc(time=msto):
    label_cpu_usage.config(text=f'{cpu_count()} Cpus')
    label_cpu_usage.configure(bg='#404040', fg='#bfbfbf')
    label_cpu.config(text=f'{cpu_freq()} HZ CPU')
    label_cpu.configure(bg='#404040', fg='#bfbfbf')
    label_temp.config(text=f'{temp_core()} Cº CPU')
    label_temp.configure(bg='#404040', fg='#bfbfbf')
    app.after(time, update_proc)


is_graphic_open = False  # Variável para controlar o estado do gráfico


def open_graphic1():
    graph(app)
    Button_open_graphic1.option_clear()
    Button_open_graphic2.option_clear()

def open_graphic2():
    graph2(app)
    Button_open_graphic1.option_clear()
    Button_open_graphic2.option_clear()


Button_open_graphic1 = ttk.Button(text='Open Graphic1', command=open_graphic1)
Button_open_graphic1.pack(side="bottom")

Button_open_graphic2 = ttk.Button(text='Open Graphic2', command=open_graphic2)
Button_open_graphic2.pack(side="bottom")

label_cpu_usage = tk.Label()
label_cpu_usage.pack()

label_cpu = tk.Label()
label_cpu.pack()

label_temp = tk.Label()

label_temp.pack()


Button_exit = ttk.Button(text='Exit', command=app.destroy)
Button_exit.pack()


update_proc()

print(ttk.Style().lookup('TButton', 'font'))

if __name__ == '__main__':
    app.mainloop()
