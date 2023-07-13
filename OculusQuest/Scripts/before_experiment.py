# noinspection PyUnusedLocal
import os

APPS = ['Camera High Frequency', 'Cpu Medium Frequency', 'GPS Low Frequency', 'Local Storage High Frequency', 'Networking Medium Frequency']

def main(device, *args, **kwargs):
    device.install('/home/radu/usb/com.example.batterymanager_utility.apk')
