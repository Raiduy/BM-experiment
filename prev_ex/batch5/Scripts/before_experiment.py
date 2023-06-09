# noinspection PyUnusedLocal
import os


APPS_1 = ['Camera High Frequency',
          'Cpu Medium Frequency',
          'GPS Low Frequency',
          'Local Storage High Frequency',
          'Networking Medium Frequency']

APPS_2 = ['Camera Medium Frequency',
          'Cpu Low Frequency',
          'GPS High Frequency',
          'Local Storage Medium Frequency',
          'Networking Low Frequency']

APPS_3 = ['Camera Low Frequency',
          'Cpu High Frequency',
          'GPS Medium Frequency',
          'Local Storage Low Frequency',
          'Networking High Frequency']

APPS_4 = ['Room Database High Frequency',
          'Accelerometer',
          'Speaker',
          'Ambient Light',
          'Microphone']

APPS_5 = ['Room Database Medium Frequency',
          'Baseline',
          'Magnetic Field',
          'Display',
          'Gyroscope']

APPS_6 = ['Room Database Low Frequency',
          'Gravity']

def main(device, *args, **kwargs):
    path = '/home/radu/VU/GreenLab-TA/android-apps-benchmark/APKs'
    
    for app in APPS_5:
        for apk in os.listdir(path + '/' + app):
            device.install(path + '/' + app + '/' + apk)

    device.install('/home/radu/VU/GreenLab-TA/ar-batterymanager-script/app/build/outputs/apk/debug/app-debug.apk')
