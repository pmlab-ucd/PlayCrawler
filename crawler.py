import pickle
from datetime import datetime

def loadState():
    try:
        state_file = open( "state_dump", "rb" )
        apps_discovered = pickle.load( state_file )
        apps_pending = pickle.load( state_file )
        #apps_count = pickle.load( state_file )
        state_file.close()
        print( "Pending = ", len( apps_pending ), " Discovered = ", len( apps_discovered ) )
        return apps_discovered, apps_pending
    except IOError:
        print( "A fresh start ..." )
        return [], []

character_encoding = 'utf-8'
apps_discovered, apps_pending = loadState()
for app in apps_discovered:
    print('https://play.google.com' + app)
    print(app['price'])
count_offset = len( apps_discovered )

print(count_offset)

start_time = datetime.now()

categories = ['BOOKS_AND_REFERENCE', 'BUSINESS', 'COMICS', 'COMMUNICATION', 'EDUCATION', 'ENTERTAINMENT', 'FINANCE',
              'HEALTH_AND_FITNESS', 'LIBRARIES_AND_DEMO', 'LIFESTYLE', 'APP_WALLPAPER', 'MEDIA_AND_VIDEO', 'MEDICAL',
              'MUSIC_AND_AUDIO', 'NEWS_AND_MAGAZINES', 'PERSONALIZATION', 'PHOTOGRAPHY', 'PRODUCTIVITY', 'SHOPPING',
              'SOCIAL', 'SPORTS', 'TOOLS', 'TRANSPORTATION', 'TRAVEL_AND_LOCAL', 'WEATHER', 'ARCADE', 'BRAIN', 'CARDS',
              'CASUAL', 'GAME_WALLPAPER', 'RACING', 'SPORTS_GAMES', 'GAME_WIDGETS', 'GAME']
app_types = ['free', 'paid']

def getApps( url ):
    previous_apps = []
    previous_skipped_apps = []
    start_idx = 0
    size = 100
    while(True):
        apps, skipped_apps = getTopAppsData( url, start_idx, size, app_type )
        if apps == previous_apps and skipped_apps == previous_skipped_apps: break
        for app in apps:
            if app['category'].upper() not in fileHandlers:
                fileHandlers[app['category'].upper()] = codecs.open( '_'.join( ["apps", app['category'].lower()] ), 'ab', character_encoding, buffering = 0 )
            fileHandler = fileHandlers[app['category'].upper()]
            try:
                fileHandler.write( json.dumps( app ) + "\n" )
            except Exception as e:
                print( e )
        previous_apps = apps
        previous_skipped_apps = skipped_apps
        start_idx += size
        saveState()

'''
fileHandlers = openResultFiles(categories)

for category, app_type in [( x, y ) for x in categories for y in app_types]:
    print("Type = ", app_type, " Cateory = ", category)
    url = 'https://play.google.com/store/apps/category/' + category + '/collection/topselling_' + app_type
    print(url)
    applist = open(category + "_list.txt", 'a')
    getApps(url)
    applist.close()
'''