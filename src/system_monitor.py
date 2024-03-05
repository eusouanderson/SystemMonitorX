import tkinter as tk
from tkinter import ttk
from cpu import cpu_freq, cpu_count
from temp_freq import temp_core
from os import getcwd

app = tk.Tk()


app.configure(bg='#404040')
#app.geometry('300x300')
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



label_cpu_usage = tk.Label()
label_cpu_usage.pack()

label_cpu = tk.Label()
label_cpu.pack()

label_temp = tk.Label()

label_temp.pack()


Button_exit = ttk.Button(text='Exit', command=app.destroy)
Button_exit.pack()


update_proc()

#Print TButon

print(ttk.Style().lookup('TButton', 'font'))

if __name__ == '__main__':
    app.mainloop()
