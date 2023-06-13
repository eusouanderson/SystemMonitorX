import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from random import randint


def graph(window, value, interval):
 
    # Configurações iniciais
    
    categorias = ['CPU ', 'RAM ', 'DISK', 'CORE ', 'NET ']
    valores = [100, 0, 0, 0, 0]
   
    fig, ax = plt.subplots()
    bar_containers = ax.bar(categorias, valores)

    # Função de atualização
    def update(frame):
        
        for i, container in enumerate(bar_containers):
            
            if i == 0 or 1 or 2 or 3 or 4:
                container.set_height(randint(0, 10 % value))
                
                if value >= 6000 :
                    container.set_color('red')
                else:
                    container.set_color('blue')


    # Criação da animação
    ani = FuncAnimation(fig, update, frames=range(10), interval=interval)
    

    # Exibição do gráfico em tempo real
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

plt.close()
