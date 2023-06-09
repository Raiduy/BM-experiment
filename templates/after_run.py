# noinspection PyUnusedLocal
def main(device, *args, **kwargs):
    device.shell('am force-stop {battery_manager_package}')
