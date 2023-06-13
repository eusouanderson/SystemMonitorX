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


def cpu_usage():
    """
    Retorna a soma da CPU em percentual de todos os núcleo.

    Exemplo:
    >>> cpu_usage()

    '4 Cores 50.00 %'
    """

    usage_cpu = psutil.cpu_percent(interval=1, percpu=True)
    number = 0
    for cpu in usage_cpu:
        number += 1

        cpu_U = f'{number} Cores {sum(usage_cpu):.2f} % '

    return cpu_U

