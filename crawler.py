import pickle
import codecs
from datetime import datetime


def load_state():
    try:
        state_file = open("crawler_state", "rb")
        apps_downloaded = pickle.load(state_file)
        state_file.close()
        print( "Downloaded = ", len(apps_downloaded) )
        return apps_downloaded
    except IOError:
        print( "A fresh start ..." )
        return []


def save_state():
    state_file = open("crawler_state", "wb")
    pickle.dump(apps_downloaded, state_file)
    state_file.close()

character_encoding = 'utf-8'
def read_json(json_name):
    file_handler = codecs.open(json_name, 'r', character_encoding, buffering=0)
    for line in file_handler.readlines():
        app = json.loads(line)
        print(app['app_url'])




import json
from pprint import pprint

read_json('apps_business')


character_encoding = 'utf-8'
apps_downloaded = load_state()
for app in apps_downloaded:
    print('https://play.google.com' + app)
count_offset = len(apps_downloaded)

print(count_offset)

start_time = datetime.now()



