import fnmatch
import os

matches = []

RESOURCE_SRC = 'resources'

print 'Scanning for resources in {0}'.format(RESOURCE_SRC)

for root, dirnames, filenames in os.walk(RESOURCE_SRC):
	for filename in fnmatch.filter(filenames, '*.png'):
		matches.append(os.path.join(root, filename))

print 'Found resource(s): {0} '.format(matches)