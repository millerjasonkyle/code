#!/bin/sh

#Script to turn on the Firewall
#Created by Jason Miller (jmiller@...) on 2013-10-07

# Configure, then enable the application layer firewall
/usr/libexec/ApplicationFirewall/socketfilterfw --setallowsigned on
/usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on

exit 0
