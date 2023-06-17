import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import psutil



def graph(window):

    bar1, bar2, bar3, bar4, bar5 = [0, 0, 0, 0, 0]

    # Configurações iniciais
    categorias = ['CPU ', 'RAM ', 'DISK', 'CORE ', 'NET ']
    valores = [bar1, bar2, bar3, bar4, bar5]
    
   # Configurando gráfico
    fig, ax = plt.subplots(figsize=(6, 3))
    bar_containers = ax.bar(categorias, valores)
    ax.set_ylim(0, 100)
    #ax.set_xlabel()
    #ax.set_ylabel()

    # Criar um widget de tela de desenho do Matplotlib
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()


    # Função de atualização
    def update(i):
        nonlocal bar_containers

        # Obter o valor da frequência da CPU usando o psutil
        cpu_freq = psutil.cpu_freq().current / 100
        mem_percnt = psutil.virtual_memory().percent 
        dis_usage = psutil.disk_usage('/').used / 1000000000
        
        # Atualizar o valor da barra correspondente
        bar_containers[0].set_height(round(cpu_freq))
        bar_containers[1].set_height(mem_percnt)
        bar_containers[2].set_height(round(dis_usage, 2))
        print(round(dis_usage, 2))
        
        # Redesenhar o gráfico
        ax.relim()
        ax.autoscale_view()
        canvas.draw()

    # Criar uma janela Tkinter
    

    # Atualizar o gráfico a cada segundo
    anim = animation.FuncAnimation(fig, update, interval=1000, cache_frame_data=False)

    def start_animation():
        anim.event_source.start()

    def stop_animation():
        anim.event_source.stop()

    # Adicionar botões para iniciar e parar a animação
    start_button = tk.Button(window, text="Start", command=start_animation)
    start_button.configure(bg='#777')
    start_button.pack()

    stop_button = tk.Button(window, text="Stop", command=stop_animation)
    stop_button.configure(bg='#777')
    stop_button.pack()

    

