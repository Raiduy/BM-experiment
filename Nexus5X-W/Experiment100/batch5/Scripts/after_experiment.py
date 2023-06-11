# noinspection PyUnusedLocal
APPS = ['e.www.writeroomtest', 'e.www.baseline', 'e.www.magneticfieldtest', 'e.www.displaytest', 'e.www.gyroscopetest']
       
def main(device, *args, **kwargs):
    for app in APPS:
        device.uninstall(app)
