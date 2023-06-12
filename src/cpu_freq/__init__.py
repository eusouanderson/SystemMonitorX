import psutil


def cpu_freq():
    freq_cpu = psutil.cpu_freq()[0]
    cpuf = '{:.2f}'.format(freq_cpu)
    return cpuf

def cpu_usage():

    usage_cpu = psutil.cpu_percent(interval=1, percpu=True)
    number = 0
    for cpu in usage_cpu:
        number += 1
        
        cpu_U = f'{number} Cores {sum(usage_cpu):.2f} % '
    #cpu_U = '{:.2f}'.format(usage_cpu)
    return cpu_U

