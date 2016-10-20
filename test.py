import codecs, json

character_encoding = 'utf-8'

def openResultFiles(all_categories):
    fileHandlers = {}
    for category in all_categories:
        fileHandler = codecs.open( '_'.join( ["apps", category.lower()] ), 'ab', character_encoding, buffering = 0 )
        fileHandlers[category] = fileHandler
    return fileHandlers

categories = ['BOOKS_AND_REFERENCE', 'BUSINESS', 'COMICS', 'COMMUNICATION', 'EDUCATION', 'ENTERTAINMENT', 'FINANCE',
              'HEALTH_AND_FITNESS', 'LIBRARIES_AND_DEMO', 'LIFESTYLE', 'APP_WALLPAPER', 'MEDIA_AND_VIDEO', 'MEDICAL',
              'MUSIC_AND_AUDIO', 'NEWS_AND_MAGAZINES', 'PERSONALIZATION', 'PHOTOGRAPHY', 'PRODUCTIVITY', 'SHOPPING',
              'SOCIAL', 'SPORTS', 'TOOLS', 'TRANSPORTATION', 'TRAVEL_AND_LOCAL', 'WEATHER', 'ARCADE', 'BRAIN', 'CARDS',
              'CASUAL', 'GAME_WALLPAPER', 'RACING', 'SPORTS_GAMES', 'GAME_WIDGETS']

fileHandlers = openResultFiles(categories)

if 'xxx' not in fileHandlers:
    fileHandlers['xxx'] = codecs.open('_'.join(["apps", 'xxx']), 'ab',
                                                        character_encoding, buffering=0)
fileHandler = fileHandlers['xxx']
try:
    fileHandler.write(json.dumps('xxx') + "\n")
except Exception as e:
    print(e)

