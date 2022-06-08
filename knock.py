import sys
import requests

print('''
    ██╗  ██╗███╗   ██╗ ██████╗  ██████╗██╗  ██╗██╗    ██╗  ██╗███╗   ██╗ ██████╗  ██████╗██╗  ██╗██╗
    ██║ ██╔╝████╗  ██║██╔═══██╗██╔════╝██║ ██╔╝██║    ██║ ██╔╝████╗  ██║██╔═══██╗██╔════╝██║ ██╔╝██║
    █████╔╝ ██╔██╗ ██║██║   ██║██║     █████╔╝ ██║    █████╔╝ ██╔██╗ ██║██║   ██║██║     █████╔╝ ██║
    ██╔═██╗ ██║╚██╗██║██║   ██║██║     ██╔═██╗ ╚═╝    ██╔═██╗ ██║╚██╗██║██║   ██║██║     ██╔═██╗ ╚═╝
    ██║  ██╗██║ ╚████║╚██████╔╝╚██████╗██║  ██╗██╗    ██║  ██╗██║ ╚████║╚██████╔╝╚██████╗██║  ██╗██╗
    ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝    ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝
    ---------------------------------------------------------------------------------------------------------------                                                   
    Script By: DL28 (NavidNaf)
    Github: github.com/NavidNaf
    Version: 1.0
    ---------------------------------------------------------------------------------------------------------------                                        
      ''')

help = "h"
counting = 0
verb = "v"
anotherCount = 0

if sys.argv[1] == help.casefold():
    print('''
            Usage: python3 knock.py [Wordlist] [URL] [SubDomain/Directory]
          ''')
    exit()

type = ["SubDomain", "Directory"]

try:
    with open(sys.argv[1], "r") as forEnum:
        file = forEnum.read()
        Enum = file.splitlines()
    total = len(Enum)
    website = sys.argv[2]

    if sys.argv[3].casefold() == type[0].casefold():
        # In case of sub domain, check connection error
        print("Knocking Sub Domains!")
        print(f"Total Knocks {total}")
        for i in Enum:
            fullsite = 'http://' + i + '.' + website
            counting = counting + 1
            try:
                print(f"Knock {counting}")
                connection = requests.get(fullsite)
            except requests.ConnectionError:
                pass
            else:
                print(fullsite + " Valid Domain")
                anotherCount = anotherCount + 1
        print(f"Sub Domain Found: {anotherCount}")
    elif sys.argv[3].casefold() == type[1].casefold():
        # In case of sub domain, check status code
        print("Knocking Directories!")
        print(f"Total Knocks {total}")
        for i in Enum:
            counting = counting + 1
            print(f"Knock {counting}")
            fullsite = "http://" + website + '/' + i + ".html"
            res = requests.get(fullsite)
            if res.status_code == 404:
                pass
            else:
                print(fullsite + " Valid Directory")
                anotherCount = anotherCount + 1
        print(f"Directory Found: {anotherCount}")

    else:
        pass
except:
    exit()
