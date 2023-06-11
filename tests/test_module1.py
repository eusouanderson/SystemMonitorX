import psutil
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import itertools

# Função para obter o uso da CPU
def get_cpu_usage():
    return psutil.cpu_percent(interval=None)

# Função para atualizar o gráfico
def update_plot(frame):
    # Obtém o uso da CPU
    cpu_percent = get_cpu_usage()

    # Adiciona os dados ao gráfico
    x_data.append(frame)
    y_data.append(cpu_percent)

    # Limita o número de pontos mostrados no gráfico
    if len(x_data) > 100:
        x_data.pop(0)
        y_data.pop(0)

    # Limpa o gráfico
    ax.clear()

    # Plota os dados atualizados
    ax.plot(x_data, y_data)

    # Configurações de exibição do gráfico
    ax.set_xlabel('Tempo')
    ax.set_ylabel('Uso da CPU (%)')
    ax.set_title('Uso da CPU em Tempo Real')

# Criação da janela do aplicativo
app = tk.Tk()
app.title('Monitor de Uso da CPU')
app.geometry('800x600')

# Criação da figura e do objeto de eixos
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)

# Criação do gráfico
x_data = []
y_data = []
line, = ax.plot([], [])

# Criação do objeto de animação
ani = FuncAnimation(fig, update_plot, frames=itertools.count(), interval=1000, cache_frame_data=False)

# Criação do objeto de exibição do gráfico na interface tkinter
canvas = FigureCanvasTkAgg(fig, master=app)
canvas.get_tk_widget().pack()

# Função para fechar o aplicativo
def close_app():
    app.quit()

# Botão de fechar
button = tk.Button(app, text='Fechar', command=close_app)
button.pack()

# Início do loop principal do aplicativo
app.mainloop()
