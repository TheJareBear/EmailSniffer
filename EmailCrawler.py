#!/usr/bin/env python

import requests
import re

master_list = []
master_email_list = []
processed_list = []

href = re.compile('href="([^"]*)')
mailto = re.compile('mailto:([^"]*)')

seed_page = raw_input("What website would you like to spider? ")
seed_keyword = raw_input("What seed keyword would you like to have? ")

fetch = requests.get(seed_page)

match = href.findall(fetch.text)

if(len(match) == 0):
	print "No HREF Tags Found =("
else:
	for site in match:
		master_list.append(site)

while( len(master_list) > 0):
	webpage = master_list.pop();
	
	if(webpage not in processed_list and seed_keyword in webpage):
			try:
				fetch = requests.get(webpage)
				match = href.findall(fetch.text)
				emails = mailto.findall(fetch.text)
				for address in emails:
					if(address not in master_email_list and "subject" not in address):
						print address
						master_email_list.append(address)
				else:
					for site in match:
						master_list.append(site)
				processed_list.append(webpage)

			except:
				random = 5
