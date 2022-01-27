# Code written by Jayesh Mahato
# Courtsey: www.jayeshmahato.com

import netifaces as ni
ni.ifaddresses('eth0')
ip6 = ni.ifaddresses('eth0')[ni.AF_INET6][0]['addr']

