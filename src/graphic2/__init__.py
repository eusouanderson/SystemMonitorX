import psutil
import matplotlib.pyplot as plt
from matplotlib import animation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graph2(window):
    # Definir o número de pontos a serem exibidos no gráfico
    num_pontos = 50

    # Criar listas vazias para armazenar os valores de tempo e utilização da CPU
    tempos = []
    utilizacao_cpu = []

    # Configurar o gráfico
    fig, ax = plt.subplots(figsize=(6, 3))
    line, = ax.plot(tempos, utilizacao_cpu)
    ax.set_ylim(0, 100)
    ax.set_xlabel('Tempo (s)')
    ax.set_ylabel('Utilização da CPU (%)')

    # Criar um widget de tela de desenho do Matplotlib
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Atualizar o gráfico em tempo real
    def update(i):
        nonlocal tempos, utilizacao_cpu
        # Obter a utilização da CPU
        cpu_percent = psutil.cpu_percent()

        # Adicionar o valor atual ao final das listas
        tempos.append(i)
        utilizacao_cpu.append(cpu_percent)

        # Limitar as listas ao número de pontos desejado
        tempos = tempos[-num_pontos:]
        utilizacao_cpu = utilizacao_cpu[-num_pontos:]

        # Atualizar os dados do gráfico
        line.set_data(tempos, utilizacao_cpu)
        ax.relim()
        ax.autoscale_view()
        canvas.draw()

    # Atualizar o gráfico a cada segundo
    anim = animation.FuncAnimation(fig, update, interval=10, cache_frame_data=False)

    def start_animation():
        anim.event_source.start()

    def stop_animation():
        anim.event_source.stop()

    # Adicionar botões para iniciar e parar a animação
    start_button = tk.Button(window, text="Start", command=start_animation)
    start_button.pack()

    stop_button = tk.Button(window, text="Stop", command=stop_animation)
    stop_button.pack()


