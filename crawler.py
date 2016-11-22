import pickle
import codecs
import os, subprocess
import json
import shutil


def run_cmd(cmd):
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    result = True
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        if b'Failure' in line or b'Error' in line:
            result = False
    return result


def load_state():
    try:
        state_file = open("crawler_state", "rb")
        apps_downloaded = pickle.load(state_file)
        state_file.close()
        print("Downloaded = ", len(apps_downloaded))
        return apps_downloaded
    except IOError:
        print("A fresh start ..." )
        return []


def save_state():
    state_file = open("crawler_state", "wb")
    pickle.dump(apps_downloaded, state_file)
    state_file.close()


def download_apk(app_url, out_base_dir, category):
    global apk_counts
    output_dir = out_base_dir + '/' + category + '/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    pkg_name = str(app_url).split('id=')[1]
    cmd = 'java -jar googleplaycrawler-0.3.jar -f crawler.conf download ' + pkg_name
    if run_cmd(cmd):
        if os.path.exists(pkg_name + '.apk'):
            apk_counts = apk_counts + 1
            apps_downloaded.append(app_url)
            shutil.move(pkg_name + '.apk', output_dir + pkg_name + '.apk')
            if apk_counts % 10 == 0:
                save_state()


def read_json(json_name):
    file_handler = codecs.open(json_name, 'r', character_encoding, buffering=0)
    for line in file_handler.readlines():
        app = json.loads(line)
        if app['app_url'] not in apps_downloaded:
            print(app['app_url'], app['category'])
            download_apk(app['app_url'], 'F:\PlayApps', app['category'])


character_encoding = 'utf-8'
apps_downloaded = load_state()
apk_counts = len(apps_downloaded)
print(str(apk_counts) + ' apps have already been downloaded!')

games = ['action', 'adventure', 'strategy', 'role playing', 'racing', 'puzzle', 'arcade', 'board', 'casino']


for root, dirs, files in os.walk('.', topdown=False):
    for name in files:
       if 'apps_' in name and name.replace('apps_', '') not in games:
            read_json(name)






