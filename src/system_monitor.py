import tkinter as tk
from graphic import graph
from cpu_freq import cpu_freq, cpu_usage
from temp_freq import temp

app = tk.Tk()

app.geometry('300x1000')
app.wm_overrideredirect(True)

def update_proc(time=100):
    label_cpu_usage.config(text=f'{cpu_usage()} Usage')
    label_cpu.config(text=f'{cpu_freq()} HZ CPU')
    label_temp.config(text=f'{temp()} Cº CPU')
    app.after(time, update_proc)
    
label_cpu_usage = tk.Label()
label_cpu_usage.pack()

label_cpu = tk.Label()
label_cpu.pack()

label_temp = tk.Label()
label_temp.pack()


update_proc()
graph(app, 100)

if __name__ == '__main__':
    app.mainloop()