import codecs

character_encoding = 'utf-8'

def openResultFiles(all_categories):
    fileHandlers = {}
    for category in all_categories:
        fileHandler = codecs.open( '_'.join( ["apps", category.lower()] ), 'ab', character_encoding, buffering = 0 )
        fileHandlers[category] = fileHandler
    return fileHandlers

fileHandlers = openResultFiles(categories)

