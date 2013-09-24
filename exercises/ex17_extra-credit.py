#! usr/bin/env python
# Extra Credit!
# takes modules from exercise 17 and chains them to one line

from sys import argv
from os.path import exists

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())