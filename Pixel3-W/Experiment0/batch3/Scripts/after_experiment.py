# noinspection PyUnusedLocal
APPS = ['e.www.cameratest', 'e.www.cpufactorialtest', 'e.www.gpstest', 'e.www.writelocaltest', 'e.www.httpsrequesttest']
       
def main(device, *args, **kwargs):
    for app in APPS:
        device.uninstall(app)
