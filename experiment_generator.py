import json
import os


APKS_PATH = '/home/radu/usb/android-apps-benchmark/APKs'
BATTERY_MANAGER_PATH = '/home/radu/usb/com.example.batterymanager_utility.apk'
BATTERY_MANAGER_PKG_NAME = 'com.example.batterymanager_utility'


def create_folders(device, parent, batch):
    if not os.path.exists('./' + device + '/' + parent + '/' + batch):
        os.makedirs('./' + device + '/' + parent + '/' + batch + '/Scripts')


def generate_config(dev, ex, batch, device, apps, sample_interval):
    with open('templates/config.json', 'r') as f:
        config = json.load(f)

        config['devices'] = device
        config['apps'] = apps
        config['profilers']['batterymanager']['sample_interval'] = sample_interval

    with open(f'./{dev}/{ex}/{batch}/config.json', 'w') as f:
        json.dump(config, f, indent=4)


def create_scripts(dev, ex, batch, app_pkg_names, app_folders):
    for file in os.listdir('templates'):
        with open('templates/' + file, 'r') as f:
            if file == 'config.json':
                continue
            
            script = f.read()
            if file == 'before_experiment.py':
                script = script.format(app_folder_names=app_folders, 
                                        apks_folder_path=APKS_PATH,
                                        battery_manager_apk_path=BATTERY_MANAGER_PATH)
            elif file == 'after_experiment.py':
                script = script.format(app_package_names=app_pkg_names)
            elif file == 'after_run.py' or file == 'before_run.py':
                script = script.format(battery_manager_package=BATTERY_MANAGER_PKG_NAME)
            
        with open(f'./{dev}/{ex}/{batch}/Scripts/' + file, 'w') as f:
            f.write(script)


devices = {
    'Pixel3-W': {},
    'Nexus5X-W': {},
    'GalaxyJ7-W': {},
    'NokiaLong-W': {},
    'NokiaRound-W': {}
}


def main():
    experiments = json.load(open('./experiments_config.json'))
    for device in devices:
        for experiment, batches in experiments.items():
            for batch, cfg in batches.items():
                create_folders(device, experiment, batch)
                create_scripts(device, experiment, batch, cfg['pkg_names'], cfg['apps'])
                generate_config(device, experiment, batch, {f'{device}':{}}, cfg['pkg_names'], cfg['sample_interval'])

main()    
