#!/usr/bin/python

import os
import urllib2
import shutil
import subprocess
import tempfile
import pwd
import zipfile
import errno
import sys
from SystemConfiguration import SCDynamicStoreCopyConsoleUser


#verify script is running as root
if not os.geteuid()==0:
    sys.exit("\nYou must be root to run this script, please use sudo and try again.\n") 

#grabbed current logged in user in Apple approved way
# def logged_in_user():
# 	username = (SCDynamicStoreCopyConsoleUser(None, None, None) or [None])[0]
# 	username = [username,""][username in [u"loginwindow", None, u""]]
# 	return username
# print logged_in_user()

def logged_in_user():
    user = (SCDynamicStoreCopyConsoleUser(None, None, None) or [None])
    user = [user,""][user[0] in [u"loginwindow", None, u""]]
    return user

username, uid, gid = logged_in_user

#logged_in_user = pwd.getpwuid(os.getuid()).pw_name

#create a temp directory for brew.sh zip
brew_temp_dir = tempfile.mkdtemp()

#changing directory to new created temp directory
os.chdir(brew_temp_dir)

#downloading brew.sh from github version the current version from Master
homebrew_zip = urllib2.urlopen(
    'https://github.com/Homebrew/brew/archive/master.zip').read()

#Writing data to disk
with open ("brew.zip", "w") as f:
    f.write(homebrew_zip)

with zipfile.ZipFile('brew.zip', 'r') as fobj:
    fobj.extractall(brew_temp_dir)

#store homebrew folder locations
#brew_directory = os.listdir(brew_temp_dir)

#print brew_directory

#Create Homebrew directory
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory.' + directory)

brew_home = ('/usr/local/bin/Homebrew')

brew_files = ['bin', 'completions', 'Library', 'manpages']
for i in brew_files:
    source = os.path.join(brew_temp_dir, 'brew-master', i)
    shutil.copytree(source, os.path.join('/usr/local/bin/Homebrew', i))

# def brew_copy(brew_temp_dir, brew_home):
#     try:
#         shutil.copytree(brew_temp_dir, brew_home)
#     except OSError as e:
#         # If the error was caused because the source wasn't a directory
#         if e.errno == errno.ENOTDIR:
#             shutil.copy(brew_temp_dir, brew_home)
#         else:
#             print('Directory not copied. Error: %s' % e)

# brew_copy(brew_temp_dir, brew_home)

#cleaning up
shutil.rmtree(brew_temp_dir)