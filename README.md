# fuck-uceprotect
### Repo name says it all


fuck-uceprotect requires requests and Python 3.x.
Installation:
Clone the repo, make the scripts (fuck-uceprotect.py and fuck-uceprotect.sh) executable.
Setup your crontab to run the script every 24 hours and at reboot:
```cron
0 0 * * * /usr/bin/fuck-uceprotect.sh
@reboot /usr/bin/fuck-uceprotect.sh
```
I recommend you running the script from a separate user account with limited sudo priveleges to the script and iptables. I tried my best on not spamming your iptables rules, mileage may vary.

Example setup:
/etc/sudoers.d/fuck-uceprotect
```
fuce ALL=NOPASSWD: /sbin/iptables
fuce ALL=NOPASSWD: /usr/bin/fuck-uceprotect.sh
fuce ALL=NOPASSWD: /usr/bin/fuck-uceprotect.py
```

If you are an ISP feel free to clone the repo, use it as you wish, modify the script, I don't care. Just make sure your customers don't hit ANY spam traps operated by this "organiztion". Integration to any system should be easy (hopefully).

Special thanks to the fine soul who owns https://uceprotect.wtf without them this small hackjob wouldn't exist. <3
