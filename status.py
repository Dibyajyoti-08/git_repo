#!/usr/bin/python3

import os

def ping(mysite):
	myping = ("ping -c 1 %s > /dev/null" %  mysite)
	status = os.system(myping)
	return status

with open("sites.txt") as file:
	mysites = file.readlines()
	print(mysites)

for site in mysites:
	print("site" + site)
	mystatus = ping(site.strip())
	if mystatus == 0: print(site.strip() + " is fine")
	if mystatus != 0: print(site.strip() + " is down")
	
	print("----------------------")
