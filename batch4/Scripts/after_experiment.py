# noinspection PyUnusedLocal

# e.www.cameratest.apk
# e.www.cpufactorialtest.apk
# e.www.gpstest.apk
# e.www.writelocaltest.apk
# e.www.httpsrequesttest.apk

# e.www.cameratest.apk
# e.www.cpufactorialtest.apk
# e.www.gpstest.apk
# e.www.writelocaltest.apk
# e.www.httpsrequesttest.apk

# e.www.cameratest.apk
# e.www.cpufactorialtest.apk
# e.www.gpstest.apk
# e.www.writelocaltest.apk
# e.www.httpsrequesttest.apk

# e.www.writeroomtest.apk
# e.www.accelerometertest.apk
# e.www.speakertest.apk
# e.www.ambientlighttest.apk
# e.www.microphonetest.apk

# e.www.writeroomtest.apk
# e.www.baseline.apk
# e.www.magneticfieldtest.apk
# e.www.displaytest.apk
# e.www.gyroscopetest.apk

# e.www.writeroomtest.apk
# e.www.gravitytest.apk


APPS_1 = ['e.www.cameratest',
          'e.www.cpufactorialtest',
          'e.www.gpstest',
          'e.www.writelocaltest',
          'e.www.httpsrequesttest']

APPS_4 = ['e.www.writeroomtest',
          'e.www.accelerometertest',
          'e.www.speakertest',
          'e.www.ambientlighttest',
          'e.www.microphonetest']

APPS_5 = ['e.www.writeroomtest',
          'e.www.baseline',
          'e.www.magneticfieldtest',
          'e.www.displaytest',
          'e.www.gyroscopetest']

APPS_6 = ['e.www.writeroomtest',
          'e.www.gravitytest']
          

def main(device, *args, **kwargs):
    for app in APPS_4:
        device.uninstall(app)
