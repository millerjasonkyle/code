#!/usr/bin/python

#Quick setup of tools I may need

import urllib2
import tempfile
import os

download_apps = tempfile.mkdtemp

os.chdir(download_apps)


dl_iterm = urllib2.urlopen(
    'https://iterm2.com/downloads/stable/iTerm2-3_1_5.zip' ).read()

dl_dropbox = urllib2.urlopen('https://www.dropbox.com/download?os=mac').read()