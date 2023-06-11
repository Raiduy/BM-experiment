# noinspection PyUnusedLocal
APPS = ['e.www.writeroomtest', 'e.www.gravitytest', 'e.intervalapp.cameratest', 'e.intervalapp.cpufactorialtest', 'e.intervalapp.displaytest']
       
def main(device, *args, **kwargs):
    for app in APPS:
        device.uninstall(app)
