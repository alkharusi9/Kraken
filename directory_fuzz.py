# Written by: Alsalt Alkharosi
#!/usr/bin/python

import sys,requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


target = sys.argv[1]
file_name = sys.argv[2]
wordlist = open(file_name,'r')
output = open('targets.vcs','w')

for x in wordlist.readlines():
    try:
        directory = x.strip('\n')
        url = 'http://'+str(target)+'/'+directory+'/'
        r = requests.get(url)
        if r.status_code==200:
            print(bcolors.OKGREEN+'[+]'+url+':'+'\n'+bcolors.ENDC)
            output.write(bcolors.OKGREEN+'[+]'+url+'\n'+bcolors.ENDC)
        else:
            print(bcolors.FAIL+'[-]'+url+bcolors.ENDC)
    except Exception as e:
        print(e)

