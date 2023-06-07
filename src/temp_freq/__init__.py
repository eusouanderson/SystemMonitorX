import psutil


def temp():
    sensor = psutil.sensors_temperatures()
    acpitz = sensor['acpitz'][1][1]

    temp = '{:.2f}'.format(acpitz)
    return temp

temp()


