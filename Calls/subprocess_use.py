#!/usr/bin/env python2

import subprocess

'''
    The following declaration of "lst" runs immediately.
    we use "subprocess.Popen" so that we have access to stdout.
    
    The first arg is the string name of the program in the user $PATH,
    the second, whether we want access to the shell or not.  False is
    a best practice, but True lets this particular program work as intended.
    
    "stdout" is set to subprocess\'s "PIPE", basically, we are taking
    whatever the program printed to stdout in the terminal and making it
    available to our script via the "stdout" variable.    
'''
lst = subprocess.Popen('pacman -Qu', shell=True, stdout=subprocess.PIPE)


'''
    Here we have a relevant example of usage on an Arch Linux system.
    
    We use subprocess.Popen to call "pacman -Qu" which prints a list of
    packages to stdout by default.
    
    We then loop through the stdout output, strip newlines, and append
    the result to "paclist" which holds our list of packages.
    
    This is useful when you want to automate checking for available
    package updates using a cronjob or an event loop timer.  You can then use
    the variable "numupdates" to compare later if you decide to auto-run
    your updates.  In the case of the program that this snippet came from,
    lupdater, I checked "if numupdates >= 1:". 
'''

# List of packages
paclist = []

# Call the package manager, saving stdout
lst = subprocess.Popen('pacman -Qu', shell=True, stdout=subprocess.PIPE)

# Loop through stdout (packages needing updates) and append to a list
for line in lst.stdout:
    line.rstrip('\r\n')
    paclist.append(line)

# Used for comparison later.
numupdates = len(paclist)


'''
    This bit of code is used for calling things that we don't really need
    to interact with, meaning, we don\'t need access to stdout.  It\'s a
    "Fire and forget" type of call.
    
    In this case, we use "subprocess.call".  It takes a list of arguments
    (notice the "[]").  First item in the list is the absolute path to and name of
    the program.  In the original program, I needed the absolute path included.
    The second item in the list is the argument passed to the called program, in this
    case, a string.  The third argument is optional, but explicitly defines the shell
    access.  "False" is normally a sane default and as I\'ve been told, more secure.
'''

subprocess.call(['/usr/bin/notify-send', 'Checking for updates...'], shell=False)

