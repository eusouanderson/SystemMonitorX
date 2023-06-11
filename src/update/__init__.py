from cpu_freq import cpu
from temp_freq import temp



def update_proc(time, proce, proce1, window):

    proce.config(text=f'{cpu()} HZ ')
    proce1.config(text=f'{temp()} Cº ')
   
    window.after(time, update_proc)