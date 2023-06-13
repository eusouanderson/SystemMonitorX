import importlib
import subprocess


try:
    nome_arquivo ='requirements.txt'  # Substitua pelo nome do seu arquivo


    with open(nome_arquivo, 'r') as arquivo:
        
        linhas = arquivo.readlines()

    linhas = [linha.strip() for linha in linhas]

    pacotes = linhas

except FileNotFoundError:
    print('O arquivo requirements.txt não foi instalado , pip install -r requirements.txt')

# Função para verificar se um pacote está instalado
def verificar_pacote(pacote):
    
    try:
        importlib.import_module(pacote)
        print(f"{pacote} está instalado.")
    except ImportError:
        print(f"{pacote} não está instalado.")
        print('~'* 10)
        print(f'Instalando {pacote}')
        subprocess.run(['pip', 'install', pacote])
        if pacote in pacotes:
            print(f'{len(pacote)} instalados com sucesso!  ')

        print('~'* 10)
# Verificar todos os pacotes da lista
for pacote in pacotes:
    verificar_pacote(pacote)
         
