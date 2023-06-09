# noinspection PyUnusedLocal
import os

APPS = {app_folder_names}

def main(device, *args, **kwargs):
    path = '{apks_folder_path}'
    
    for app in APPS:
        for apk in os.listdir(path + '/' + app):
            device.install(path + '/' + app + '/' + apk)

    device.install('{battery_manager_apk_path}')
