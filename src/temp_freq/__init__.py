import psutil

sensor = psutil.sensors_temperatures()

"""
{'acpitz': [shwtemp(label='', current=6.8, high=18.8, critical=18.8), shwtemp(label='', current=27.8, high=119.0, critical=119.0), shwtemp(label='', current=29.8, high=119.0, critical=119.0)]
, 'coretemp': [shwtemp(label='Package id 0', current=45.0, high=80.0, critical=100.0), shwtemp(label='Core 0', current=45.0, high=80.0, critical=100.0), shwtemp(label='Core 1', current=45.0, high=80.0, critical=100.0), shwtemp(label='Core 2', current=43.0, high=80.0, critical=100.0), shwtemp(label='Core 3', current=44.0, high=80.0, critical=100.0)],
'nouveau': [shwtemp(label='', current=43.0, high=95.0, critical=130.0)],
 'amdgpu': [shwtemp(label='edge', current=32.0, high=94.0, critical=94.0)]}"""


def temp_acpitz():

    acpitz = sensor['acptiz'][0][1]
    temp = '{:.2f}'.format(acpitz)
    return temp


def temp_core():

    coretemp = sensor['coretemp'][0][1]
    temp = '{:.2f}'.format(coretemp)
    return temp


def temp_nouveau():

    nouveau = sensor['nouveau'][0][1]
    temp = '{:.2f}'.format(nouveau)
    return temp


def temp_amdgpu():

    amdgpu = sensor['amdgpu'][0][1]
    temp = '{:.2f}'.format(amdgpu)

    return temp
