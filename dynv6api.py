# Code written by Jayesh Mahato
# Courtsey: www.jayeshmahato.com

import requests
import getip
import checkip
import parameters

ip6 = getip.ip6
# exit the program if here is no change in IP
if checkip.check_ip(ip6):
	exit()

# update IP at dynv6 and store IP locally, if updated
params_ip6 = parameters.parameters
params_ip6["ipv6"] = ip6

response = requests.get("https://dynv6.com/api/update", params=params_ip6)

if response.status_code == 200:
	checkip.store_ip(ip6)
