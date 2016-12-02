import csv, os
import urllib.request
import pickle

csvpath = 'C:/Users/Hao/Documents/latest.csv'
csvfile = open(csvpath, 'r')
reader = csv.reader(csvfile, delimiter=',', quotechar='|')
next(reader, None)  # skip the headers
api_key = 'f9be0153fe0d204b6b52acd7822dccbdc95b58a839f4bd58052ad2bcfd570f61'

def load_state():
    try:
        state_file = open("appzoo_state", "rb")
        apps_downloaded = pickle.load(state_file)
        state_file.close()
        print("Downloaded = ", len(apps_downloaded))
        return apps_downloaded
    except IOError:
        print("A fresh start ..." )
        return []

def save_state():
    state_file = open("appzoo_state", "wb")
    pickle.dump(apps_downloaded, state_file)
    state_file.close()

apps_downloaded = load_state()
apk_counts = len(apps_downloaded)
print(str(apk_counts) + ' apps have already been downloaded!')

for row in reader:
    if row[0] not in apps_downloaded:
        print(row[0])
        url = 'https://androzoo.uni.lu/api/download?apikey=' + api_key + '&sha256=' + row[0]
        market = row[-1]
        if '|' in row[-1]:
            market = str(market).split('|')[0]
        output_dir = 'C:/Users/Hao\Documents\output/' + market + '/'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        urllib.request.urlretrieve(url, output_dir + str(row[5]).replace('"', '') + "_" + str(row[6]) + ".apk")
        apps_downloaded.append(row[0])
        apk_counts = apk_counts + 1
        if apk_counts % 10 == 0:
            save_state()