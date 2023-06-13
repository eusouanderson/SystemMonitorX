import psutil


def cpu_freq():

    """
    Retorna a utilização da CPU em percentual para cada núcleo.

    Exemplo:
    >>> cpu_freq()
    '4470.60'
    """

    freq_cpu = psutil.cpu_freq()[0]
    cpuf = '{:.2f}'.format(freq_cpu)
    print(cpuf)
    return cpuf

def cpu_usage():
    
    """
    Retorna a utilização da CPU em percentual para cada núcleo.

    Exemplo:
    >>> cpu_usage()
    
    '1 Cores 25.00 %'
    """

    usage_cpu = psutil.cpu_percent(interval=1, percpu=True)
    number = 0
    for cpu in usage_cpu:
        number += 1
        
        cpu_U = f'{number} Cores {sum(usage_cpu):.2f} % '


    return cpu_U

