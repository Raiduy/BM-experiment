import json
import os


APKS_PATH = '/home/radu/VU/GreenLab-TA/android-apps-benchmark/APKs'
BATTERY_MANAGER_PATH = '/home/radu/VU/GreenLab-TA/ar-batterymanager-script/app/build/outputs/apk/debug/app-debug.apk'
BATTERY_MANAGER_PKG_NAME = 'com.example.batterymanager_utility'


def create_folders(parent, batch):
    if not os.path.exists('./' + parent + '/' + batch):
        os.makedirs('./' + parent + '/' + batch + '/Scripts')


def generate_config(ex, batch, devices, apps, sample_interval):
    with open('templates/config.json', 'r') as f:
        config = json.load(f)

        config['devices'] = devices
        config['apps'] = apps
        config['profilers']['batterymanager']['sample_interval'] = sample_interval

    with open(f'./{ex}/{batch}/config.json', 'w') as f:
        json.dump(config, f, indent=4)


def create_scripts(ex, batch, app_pkg_names, app_folders):
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
            
        with open(f'./{ex}/{batch}/Scripts/' + file, 'w') as f:
            f.write(script)


devices = {
    'Px3': {},
    'Pixel 2': {},
    'Pixel 3': {},
}

experiments = json.load(open('experiments_conf.json'))

def main():
    for experiment, batches in experiments.items():
        for batch, cfg in batches.items():
            create_folders(experiment, batch)
            create_scripts(experiment, batch, cfg['apps'], cfg['pkg_names'])
            generate_config(experiment, batch, devices, cfg['apps'], cfg['sample_interval'])

main()    
    