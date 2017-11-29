#!/usr/bin/python
import os

print "Hello, Python!"
print "Testing"
#os.listdir('.')
dirs = os.listdir('.')
for f in dirs:
	print ("Dirs are " + f)
#dirs = os.listdir('.')
from pprint import pprint
pprint(dirs)
