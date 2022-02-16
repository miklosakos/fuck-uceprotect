#!/bin/python3

import requests
import json
import sys
import os

print("Trying to download known UCEProtect IP ranges from https://uceprotect.wtf...")

url = 'https://uceprotect.wtf/uceprotect.json'

header={'User-Agent':'miklosakos@github/fuck-uceprotect'}

try:
    dl = requests.get(url, allow_redirects=True,headers=header)
except Exception as e:
    sys.exit(e)

print("Downloaded known IP ranges")

#--- START CONFIG ---

tmpdir='/tmp'

processedlst=tmpdir+'/processed.lst'

postfix_fuck-uceprotect_dir='/etc/postfix/fuck-uceprotect'
postfix_restricted_senders=postfix_fuck-uceprotect_dir + '/senders'
postfix_restricted_recipients=postfix_fuck-uceprotect_dir + '/recipients'
postfix_recipient_bounce_message="Sorry, the person you tried to reach uses UCEProtect, try reaching them through other means."
postfix_sender_bounce_message="Sorry, the person you tried to reach uses a mail server that is configured to NOT deliver e-mails from UCEProtect customers."

#--- END CONFIG ---

if not os.path.exists(postfix_fuck-uceprotect_dir):
    os.makedirs(postfix_fuck-uceprotect_dir)

#--- START VARIABLES DON'T TOUCH ---

open(knownlst,'w').write(dl.text)
lst = open(knownlst,'r')
protecteddomains=[]
data = json.load(lst)

#--- END VARIABLES DON'T TOUCH ---
print("The following data has been processed: ")

for i in data['customers']:
    tmp = i['url'].split('/')
    tmp = tmp[2].split('.')
    protecteddomains.append(tmp[1])

with open(postfix_restricted_senders,'w') as senders:
        for domain in protecteddomains:
            #senders.write("@%s.* REJECT Sorry, this mail server has been configured to NOT receive emails from UCEProtect \"protected\" senders. We don't apologize for the inconvenience. Try to reach your recipient through other means and notify them that the systems administrator is blocking your emails ever arriving to their mailbox. We are not willing to support an extortion \"organization\" that makes up false claims and demands ransom for unlisting. We recommend you to ditch them as well.\n" % domain)
            senders.write("{}.* REJECT 550 {}\n".format(domain, postfix_sender_bounce_message))
with open(postfix_restricted_recipients,'w') as recipients:
    for domain in protecteddomains:
        #recipients.write("@%s.* REJECT Sorry, this mail server has been configured to NOT deliver emails to UCEProtect \"protected\" recipients. We apologize for the inconvenience. Try to reach your recipient through other means and notify them that they will never see a response from your mailbox. We are not willing to pay for an extortion \"organization\"'s ransom.\n" % domain)
        recipients.write("{}.* REJECT 550 {}\n".format(domain, postfix_recipient_bounce_message))

os.system('postmap hash:{}'.format(postfix_restricted_senders))
os.system('postmap hash:{}'.format(postfix_restricted_recipients))
os.remove(knownlst)
