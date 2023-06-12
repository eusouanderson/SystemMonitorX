import importlib

# Lista dos pacotes a serem verificados
pacotes = ['tkinter', 'contourpy', 'cycler', 'fonttools', 'kiwisolver', 'matplotlib', 'numpy', 'packaging', 'Pillow', 'psutil', 'pyparsing', 'python-dateutil', 'six' ]


# Função para verificar se um pacote está instalado
def verificar_pacote(pacote):
    try:
        importlib.import_module(pacote)
        print(f"{pacote} está instalado.")
    except ImportError:
        print(f"{pacote} não está instalado.")
        print('~'* 10)
        print(f'pip install {pacote}')
        print('~'* 10)
# Verificar todos os pacotes da lista
for pacote in pacotes:
    verificar_pacote(pacote)
