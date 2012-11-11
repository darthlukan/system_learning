#!/usr/bin/env python2

import os
import sys
import time
import shutil
import logging


'''
    Here we get the size of a file passed as a
    command line argument to our program.
    
    sys.argv[0] = the name of our program
    sys.argv[1] = the first argument after our program
    
    os.path.getsize(file) returns the size of our file in bytes.
'''

file = sys.argv[1]
print(os.path.getsize(file))
# Output: filesize in bytes


'''
    Here we check if the provided "val" points to a directory.
    
    NOTE: This is included here as directories are just files
    in Linux.
'''

val = '/home/username'

os.path.isdir(val)
# Output: True


'''
    Here we move a file. The behavior is the same as:
    
    $ mv ~/test.txt ~/docs
'''

filename = '/home/darthlukan/test.txt'

destpath = '/home/darthlukan/docs'

shutil.move(filename, destpath)


'''
    Logging:
    
    First we have to setup the basicConfig.  This method takes the
    absolute path and name of the file to be used as the log, and the logging
    level (DEBUG, INFO, etc), though, I have not found this (level) to be important.
    
    Next, when we want to actually write to the log, we call logging.info
    with our desired information.  In this case, we want the time of the call
    to be printed first, then the as a string.
'''
# If the file doesn't exist, it does now assuming we have write access to /tmp
# Place this at the top of the script/program and then forget about it.
logging.basicConfig(filename='/tmp/lupdater.log', level=logging.DEBUG)

# Actually does the writing.
logging.info(time.ctime() + ': Log message goes here.')


'''
    Writing to files.
    
    First we create a file object with the "open" command.
    This command takes the absolute path and file name of the file, as
    well as the "mode".  "w" = write, "r" = readonly, etc
    
    This object now as various methods available, one being "write(str)".
    
    Calling "f.close()" will close the file and free any resources associated with it.
'''

f = open('/path/to/file', 'w')

f.write('string we want written to file.')

f.close()