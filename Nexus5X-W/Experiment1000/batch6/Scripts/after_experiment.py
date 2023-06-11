# noinspection PyUnusedLocal
APPS = ['e.www.writeroomtest', 'e.www.gravitytest', 'x.intervalapp.cameratest', 'x.intervalapp.cpufactorialtest', 'x.intervalapp.displaytest']
       
def main(device, *args, **kwargs):
    for app in APPS:
        device.uninstall(app)
