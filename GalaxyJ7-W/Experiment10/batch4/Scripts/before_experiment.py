# noinspection PyUnusedLocal
import os

APPS = ['Room Database High Frequency', 'Accelerometer', 'Speaker', 'Ambient Light', 'Microphone']

def main(device, *args, **kwargs):
    path = '/home/radu/VU/GreenLab/android-apps-benchmark/APKs'
    
    for app in APPS:
        for apk in os.listdir(path + '/' + app):
            device.install(path + '/' + app + '/' + apk)

    device.install('/home/radu/VU/GreenLab/ar-batterymanager-script/app/build/outputs/apk/debug/app-debug.apk')
