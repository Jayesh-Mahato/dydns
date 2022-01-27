# Code written by Jayesh Mahato
# Courtsey: www.jayeshmahato.com

import json

def get_stored_ip():
	#read json file
	with open("ip.txt") as ip_check:
		data = json.load(ip_check)
	return data

def check_ip(ipnew):
	ipstored = get_stored_ip()
	if ipstored["ipv6"] == ipnew:
		return 1
	else:
		return 0

def store_ip(ipnew):
	ipstored = get_stored_ip()
	ipstored["ipv6"] = ipnew
	#write to json file
	with open("ip.txt","w") as f1:
		json.dump(ipstored, f1)

