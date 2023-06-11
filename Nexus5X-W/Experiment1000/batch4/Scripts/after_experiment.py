# noinspection PyUnusedLocal
APPS = ['e.www.writeroomtest', 'e.www.accelerometertest', 'e.www.speakertest', 'e.www.ambientlighttest', 'e.www.microphonetest']
       
def main(device, *args, **kwargs):
    for app in APPS:
        device.uninstall(app)
