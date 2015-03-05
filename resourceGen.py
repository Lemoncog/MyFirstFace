import fnmatch
import os
import json

matches = []

RESOURCE_SRC = 'resources'
APP_INFO_SRC = 'appinfo.json'

print 'Scanning for resources in {0}'.format(RESOURCE_SRC)

for root, dirnames, filenames in os.walk(RESOURCE_SRC):
	for filename in fnmatch.filter(filenames, '*.png'):
		matches.append(os.path.join(root, filename))

print 'Found resource(s): {0} '.format(matches)

appInfoJSON = {}

with open(APP_INFO_SRC) as inFile:
	appInfoJSON = json.load(inFile)

resourcesArray = appInfoJSON['resources']['media']
del resourcesArray[:]

for match in matches:
	resourcesArray.append({
        "type": "png",
        "name": match.split('/')[-1].upper(),
        "file": match
    })

print 'resourcesArray {0}'.format(resourcesArray)

with open(APP_INFO_SRC, 'w') as outfile:
	json.dump(appInfoJSON, outfile, indent=4)