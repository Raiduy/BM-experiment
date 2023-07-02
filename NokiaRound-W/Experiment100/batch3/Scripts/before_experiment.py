# noinspection PyUnusedLocal
import os

APPS = ['Camera Low Frequency', 'Cpu High Frequency', 'GPS Medium Frequency', 'Local Storage Low Frequency', 'Networking High Frequency']

def main(device, *args, **kwargs):
    path = '/home/radu/usb/android-apps-benchmark/APKs'
    
    for app in APPS:
        for apk in os.listdir(path + '/' + app):
            device.install(path + '/' + app + '/' + apk)

    device.install('/home/radu/usb/com.example.batterymanager_utility.apk')
