import psutil


def cpu_freq():
    """
    Retorna a utilização da CPU em percentual para cada núcleo.

    Exemplo:
    >>> cpu()
    '4470.60'
    """

    freq_cpu = psutil.cpu_freq()[0]
    cpuf = '{:.2f}'.format(freq_cpu)
    return cpuf


def cpu_count():
    """
    Retorna a soma da CPU .

    Exemplo:
    >>> cpu_cont():

    '4'
    """
    count_cpu = psutil.cpu_count()
    
    
    

    return cpu_count

