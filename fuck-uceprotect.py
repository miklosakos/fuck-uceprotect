#!/bin/python3
import requests
import json
import sys
import os
print("Trying to download known UCEProtect IP ranges from https://uceprotect.wtf...")
url = 'https://uceprotect.wtf/uceprotect.json'
header={'User-Agent':'miklosakos/fuck-uceprotect'}
try:
    dl = requests.get(url, allow_redirects=True,headers=header)
except Exception as e:
    sys.exit(e)

print("Downloaded known IP ranges")

#--- START CONFIG ---
processedlst='/tmp/processed.lst'
knownlst='/tmp/uceprotect.json'
#--- END CONFIG ---

open(knownlst,'w').write(dl.text)
lst = open(knownlst,'r')
uceips=[]
data = json.load(lst)
print("The following data has been processed: ")
for i in data['ip_ranges']:
    if i['description'] != 'RBL Servers' and i['description'] != 'uceprotect.net real IP':
        uceips.append(i['range'])
        print(i['range'])
with open(processedlst,'w') as processed:
        for ip in uceips:
            processed.write("%s\n" % ip)

os.remove(knownlst)
