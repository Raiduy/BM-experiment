# noinspection PyUnusedLocal
APPS = {app_package_names}
       
def main(device, *args, **kwargs):
    for app in APPS:
        device.uninstall(app)
