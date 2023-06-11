import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from random import randint



def graph(window, value):
    # Configurações iniciais
    categorias = ['A','B', 'C', 'D', 'E']
    valores = [value, 10, 20, 30, 70]

    fig, ax = plt.subplots()
    bar_containers = ax.bar(categorias, valores)

    # Função de atualização
    def update(frame):
        print(value)
        for i, container in enumerate(bar_containers):
            if i == 0:
                container.set_height(randint(value-1, value))
                if value >= 60 :
                    container.set_color('red')
                else:
                    container.set_color('blue')
                     
        # Define a cor da barra se o valor for maior que 60
                

    # Criação da animação
    ani = FuncAnimation(fig, update, frames=range(10), interval=1000)

    # Exibição do gráfico em tempo real
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

plt.close()
