#!/usr/bin/python

import os
import urllib2
import shutil
import subprocess
import tempfile
import pwd
import zipfile
import errno

#grabbed current logged in user
logged_in_user = pwd.getpwuid(os.getuid()).pw_name

#create a temp directory for brew.sh zip
brew_temp_dir = tempfile.mkdtemp()

#changing directory to new created temp directory
os.chdir(brew_temp_dir)

#downloading brew.sh from github version 1.4.3
homebrew_url = urllib2.urlopen('https://github.com/Homebrew/brew/archive/1.4.3.zip')
homebrew_zip = homebrew_url.read()

#Writing data to disk
with open ("brew.zip", "w") as f:
    f.write(homebrew_zip)

unzip = zipfile.ZipFile('brew.zip', "r")
unzip.extractall(brew_temp_dir)
unzip.close()

#Create Homebrew directory
def createFolder('/usr/local/test/Homebrew')
    try:
        if not os.path.exists('/usr/local/test/Homebrew')
            os.makedirs('/usr/local/test/Homebrew')
    except OSError:
        print ('Error: Creating directory.' + '/usr/local/test/Homebrew')

createFolder('/usr/local/test/Homebrew')

brew_home = ('/usr/local/test/Homebrew')

def brew_copy(brew_temp_dir, brew_home):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)

brew_copy(brew_temp_dir, brew_home)

#cleaning up
#shutil.rmtree(brew_temp_dir)

#used for testing
#print brew_temp_dir