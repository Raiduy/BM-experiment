# noinspection PyUnusedLocal
def main(device, *args, **kwargs):
    device.shell('am start -n "{battery_manager_package}/{battery_manager_package}.MainActivity" -a android.intent.action.MAIN -c android.intent.category.LAUNCHER')
