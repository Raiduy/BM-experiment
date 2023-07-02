# noinspection PyUnusedLocal
import os

APPS = ['Camera Medium Frequency', 'Cpu Low Frequency', 'GPS High Frequency', 'Local Storage Medium Frequency', 'Networking Low Frequency']

def main(device, *args, **kwargs):
    path = '/home/radu/usb/android-apps-benchmark/APKs'
    
    for app in APPS:
        for apk in os.listdir(path + '/' + app):
            device.install(path + '/' + app + '/' + apk)

    device.install('/home/radu/usb/com.example.batterymanager_utility.apk')
