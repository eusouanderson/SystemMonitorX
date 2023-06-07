import psutil

#number_cpu = psutil.cpu_count()


def cpu():
    freq_cpu = psutil.cpu_freq()[0]
    cpu = '{:.2f}'.format(freq_cpu)
    return cpu

